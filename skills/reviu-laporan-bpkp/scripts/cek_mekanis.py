"""Pemeriksaan mekanis otomatis atas draf laporan .docx.

Pemakaian:
  python cek_mekanis.py laporan.docx [--maks 12] [--maks-kata 50] [--izinkan BPKP,APIP]

Hasilnya adalah DAFTAR KANDIDAT, bukan vonis. Setiap butir harus ditriase:
judul, kutipan peraturan, nama resmi/produk, dan nomor naskah sering memicu
positif palsu. Label lokasi (P012, T03R02C01) sama dengan dump_docx.py.
"""
import argparse
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _teks_docx import units, runs, is_judul  # noqa: E402

IZIN_AKRONIM = {
    'BPKP', 'RI', 'NKRI', 'DIY', 'DKI', 'NIP', 'NIK', 'KTP', 'PNS', 'ASN', 'TNI', 'POLRI', 'COVID', 'UUD', 'OK', 'PT', 'CV',
    'UD', 'TK', 'SD', 'SMP', 'SMA', 'RT', 'RW', 'HP', 'PC', 'BLM', 'DPR', 'DPRD', 'MPR', 'KPK', 'BPK', 'BUMN', 'BUMD',
}
KATA_TUGAS = {'dan', 'di', 'ke', 'dari', 'yang', 'untuk', 'dalam', 'pada', 'atau', 'dengan', 'terhadap', 'oleh', 'tentang',
              'serta', 'tetapi', 'sebagai', 'per', 'bagi', 'atas', 'antara', 'sejak', 'hingga', 'sampai', 'karena', 'agar'}
TIDAK_BAKU = [
    (r'\bdi-?input\b', 'dicatat/dimasukkan'), (r'\bdimana\b', 'di mana/yang'), (r'\bdisini\b', 'di sini'),
    (r'\bdisana\b', 'di sana'), (r'\bdiantara(nya)?\b', 'di antara(nya)'), (r'\bkedepan(nya)?\b', 'ke depan(nya)'),
    (r'\bkemana\b', 'ke mana'), (r'\bpraktek\b', 'praktik'), (r'\bresiko\b', 'risiko'), (r'\banalisa\b', 'analisis'),
    (r'\bmerubah\b', 'mengubah'), (r'\baktifitas\b', 'aktivitas'), (r'\befektifitas\b', 'efektivitas'),
    (r'\bproduktifitas\b', 'produktivitas'), (r'\bkwitansi\b', 'kuitansi'), (r'\bsistim\b', 'sistem'), (r'\bijin\b', 'izin'),
    (r'\bsekedar\b', 'sekadar'), (r'\bnopember\b', 'November'), (r'\btehnis\b', 'teknis'), (r'\bobyek\b', 'objek'),
    (r'\bsubyek\b', 'subjek'), (r'\bhutang\b', 'utang'), (r'\bhimbau(an)?\b|\bmenghimbau\b', 'imbau/imbauan/mengimbau'),
    (r'\bs/d\b', 's.d.'), (r'\bdll(?!\.)\b', 'dll.'), (r'\bdsb(?!\.)\b', 'dsb.'), (r'\bnon\s+(?=[a-z])', 'non- ditulis serangkai (nontunai)'),
    (r'\bpasca\s+(?=[a-z])', 'pasca- ditulis serangkai'), (r'\bantar\s+(?=[a-z])', 'antar- ditulis serangkai (kecuali verba "antar")'),
    (r'\badalah merupakan\b', 'pilih salah satu'), (r'\bagar supaya\b', 'pilih salah satu'), (r'\bdemi untuk\b', 'pilih salah satu'),
    (r'\bdan serta\b|\bserta dan\b', 'pilih salah satu'), (r'\bberasal-usul\b', 'dengan asal-usul'),
    (r'(?<=[a-z,]) namun\b', '"namun" di tengah kalimat: pakai "tetapi"'),
]
ISTILAH_ASING = ['cut off', 'cut-off', 'entry meeting', 'exit meeting', 'early warning', 'real time', 'real-time', 'bottom up',
                 'bottom-up', 'top down', 'top-down', 'cut and fill', 'cash management system', 'mark up', 'mark-up', 'overlap',
                 'database', 'upload', 'download', 'update', 'stakeholder', 'follow up', 'deadline', 'sharing', 'online',
                 'offline', 'output', 'outcome', 'input', 'website', 'dashboard', 'link', 'gap']
ACR = re.compile(r'(?<![\w/.\-])([A-Z][A-Za-z]*[A-Z][A-Za-z]*)(?![\w/\-])(?!\.\d)')


def konteks(t, a, b, w=55):
    return ('...' if a > w else '') + t[max(0, a - w):b + w].replace('\n', ' ') + ('...' if b + w < len(t) else '')


def dalam_kutipan(t, pos):
    return t.rfind('“', 0, pos) > t.rfind('”', 0, pos) or t[:pos].count('"') % 2 == 1


class Laporan:
    def __init__(self, maks):
        self.maks = maks
        self.blok = []

    def tambah(self, judul, item, catatan=''):
        self.blok.append((judul, item, catatan))

    def cetak(self):
        print('RINGKASAN')
        for j, it, _ in self.blok:
            print(f'  {len(it):4d}  {j}')
        for j, it, cat in self.blok:
            if not it:
                continue
            print(f'\n== {j} ({len(it)})' + (f'\n   catatan: {cat}' if cat else ''))
            for x in it[:self.maks]:
                print('   ' + x)
            if len(it) > self.maks:
                print(f'   ... {len(it) - self.maks} lainnya')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('--maks', type=int, default=12, help='contoh per pemeriksaan')
    ap.add_argument('--maks-kata', type=int, default=50, help='batas kata per kalimat')
    ap.add_argument('--izinkan', default='', help='akronim tambahan yang tidak perlu dieja, dipisah koma')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    izin = IZIN_AKRONIM | {x.strip() for x in a.izinkan.split(',') if x.strip()}
    _, U = units(a.docx)
    L = Laporan(a.maks)
    badan = [u for u in U if u['teks'].strip()]
    judul_ids = {u['id'] for u in badan if is_judul(u)}

    # 1. Akronim belum dieja lengkap pada kemunculan pertama (judul dan teks kapital semua dilewati)
    urut = []
    for u in badan:
        t = u['teks']
        huruf = [c for c in t if c.isalpha()]
        if u['id'] in judul_ids or (huruf and sum(c.isupper() for c in huruf) / len(huruf) > 0.8):
            continue
        urut.append(u)
    pertama, definisi = {}, {}
    for idx, u in enumerate(urut):
        t = u['teks']
        for m in ACR.finditer(t):
            k = m.group(1)
            if k in izin or re.fullmatch(r'[IVXLC]+', k) or dalam_kutipan(t, m.start()):
                continue
            pertama.setdefault(k, (idx, u, m.start(), m.end()))
        for m in re.finditer(r'\(([A-Z][A-Za-z\-]*[A-Z][A-Za-z]*)\s*[);,]', t):
            definisi.setdefault(m.group(1), (idx, u, m.start()))
    item = []
    for k, (idx, u, s, e) in sorted(pertama.items(), key=lambda kv: (kv[1][0], kv[1][2])):
        d = definisi.get(k)
        if d is None:
            item.append(f'{k:10} belum pernah dieja | {u["id"]}: {konteks(u["teks"], s, e)}')
        elif (d[0], d[2]) > (idx, s + 5):
            item.append(f'{k:10} dieja sesudah dipakai ({d[1]["id"]}) | pertama {u["id"]}: {konteks(u["teks"], s, e)}')
    L.tambah('Akronim belum dieja lengkap pada kemunculan pertama', item,
             'abaikan kutipan, nama dokumen, kode, dan akronim yang lazim; tambahkan --izinkan bila perlu')

    # 2. Tanda baca dan spasi
    pola_tb = [('spasi ganda', r'\S  +\S'), ('spasi sebelum tanda baca', r' [,.;:)](?!\.)'), ('spasi setelah kurung buka', r'\( '),
               ('tanpa spasi setelah koma', r',(?=[A-Za-z])'), ('titik ganda', r'(?<!\.)\.\.(?!\.)'),
               ('tanda pisah panjang (em/en dash)', r'[—–]|\s--\s'), ('tanda hubung berspasi dipakai sebagai pisah', r'\w - \w'),
               ('tanda kutip lurus', r'"'), ('asterisk', r'\*')]
    for nama, pat in pola_tb:
        item = [f'{u["id"]}: {konteks(u["teks"], m.start(), m.end(), 40)!r}' for u in badan for m in re.finditer(pat, u['teks'])]
        L.tambah(f'Tanda baca: {nama}', item)

    # 3. Angka dan satuan
    pola_angka = [('Rp berspasi/bertitik', r'Rp[ .]\s?\d'), ('Rp diakhiri ,-', r'Rp[\d.]+,-'),
                  ('desimal titik pada persen', r'\d+\.\d+\s?%'), ('spasi sebelum %', r'\d\s%'),
                  ('Rp tanpa pemisah ribuan', r'Rp\d{4,}(?![\d.,])'), ('TA tanpa spasi', r'\bTA\d{4}\b'),
                  ('tahun anggaran ditulis T.A.', r'\bT\.A\.')]
    for nama, pat in pola_angka:
        item = [f'{u["id"]}: {konteks(u["teks"], m.start(), m.end(), 40)!r}' for u in badan for m in re.finditer(pat, u['teks'])]
        L.tambah(f'Angka: {nama}', item)

    # 4. Kata tidak baku dan pilihan kata
    item = []
    for u in badan:
        for pat, saran in TIDAK_BAKU:
            for m in re.finditer(pat, u['teks'], re.I if not pat.startswith('(?<=') else 0):
                if not dalam_kutipan(u['teks'], m.start()):
                    item.append(f'{u["id"]}: {m.group(0)!r} -> {saran} | {konteks(u["teks"], m.start(), m.end(), 40)}')
    L.tambah('Kata tidak baku / pilihan kata', item)

    # 5. Kata berulang tidak sengaja
    item = [f'{u["id"]}: {konteks(u["teks"], m.start(), m.end(), 35)!r}' for u in badan
            for m in re.finditer(r'\b([A-Za-z]{3,})\s+\1\b', u['teks'], re.I)]
    L.tambah('Kata berulang', item)

    # 6. Koma serial (EYD V: koma sebelum "dan"/"atau" pada perincian tiga unsur atau lebih)
    item = [f'{u["id"]}: {konteks(u["teks"], m.start(), m.end(), 30)!r}' for u in badan
            for m in re.finditer(r'(?<![\w,]) ?\b([A-Za-z]+), ([a-z]+) (dan|atau) ([a-z]+)\b', u['teks'])]
    L.tambah('Koma serial kemungkinan kurang', item, 'heuristik: periksa apakah memang perincian tiga unsur')

    # 7. Huruf kapital jabatan tanpa nama orang/wilayah
    item = []
    for u in badan:
        t = u['teks']
        for m in re.finditer(r'\b(Kepala Desa|Sekretaris Desa|Perangkat Desa|Kepala Dinas|Kepala Daerah)\b(?!\s+[A-Z])', t):
            awal = m.start() == 0 or t[:m.start()].rstrip().endswith(('.', ':'))
            if not awal and not dalam_kutipan(t, m.start()) and u['id'] not in judul_ids:
                item.append(f'{u["id"]}: {konteks(t, m.start(), m.end(), 40)!r}')
    L.tambah('Huruf kapital jabatan yang tidak merujuk orang/wilayah tertentu', item, 'kapital hanya bila diikuti nama atau dipakai sebagai sapaan')

    # 8. Penulisan judul
    item = []
    for u in badan:
        if u['id'] not in judul_ids:
            continue
        t = u['teks'].strip()
        huruf = [c for c in t if c.isalpha()]
        if huruf and sum(c.isupper() for c in huruf) / len(huruf) > 0.8:
            continue
        kata = re.findall(r"[A-Za-z][\w'/-]*", t)
        kecil = [w for i, w in enumerate(kata) if i and w.lower() not in KATA_TUGAS and w[0].islower()]
        tugas = [w for i, w in enumerate(kata) if i and w.lower() in KATA_TUGAS and w[0].isupper()]
        if kecil or tugas:
            item.append(f'{u["id"]}: {t[:110]!r}' + (f' | huruf kecil: {kecil[:4]}' if kecil else '') + (f' | kata tugas kapital: {tugas}' if tugas else ''))
    L.tambah('Judul: huruf kapital tidak konsisten', item, 'judul memakai huruf kapital tiap kata kecuali kata tugas; abaikan judul yang memang berbentuk kalimat')

    # 9. Daftar bernomor: konsistensi awal dan tanda baca akhir (EYD V)
    grup = defaultdict(list)
    for u in badan:
        if u['jenis'] == 'p' and u['num'] and u['id'] not in judul_ids:
            grup[u['num']].append(u)
    item = []
    for (nid, il), g in grup.items():
        if len(g) < 2:
            continue
        def jenis_awal(t):
            w = (t.strip().split() or [''])[0]
            if ACR.fullmatch(w.strip('(),;')) or (len(w) > 1 and w.isupper()):
                return 'A'  # diawali akronim/nama: netral
            return 'K' if w[:1].isupper() else 'k'
        awal = ''.join(jenis_awal(x['teks']) for x in g)
        akhir = []
        for x in g:
            s = x['teks'].rstrip()
            akhir.append('; dan' if s.endswith('; dan') else '; atau' if s.endswith('; atau') else s[-1:] or '?')
        catat = []
        if 'K' in awal and 'k' in awal:
            catat.append('awal butir campur kapital/kecil')
        tengah = akhir[:-1]
        if '.' in tengah and any(e.startswith(';') for e in tengah):
            catat.append('akhir butir campur titik/titik koma')
        if 'K' not in awal and 'k' in awal and '.' in tengah:
            catat.append('frasa (huruf kecil) diakhiri titik sebelum butir terakhir')
        if len(g) >= 3 and all(e.startswith(';') for e in tengah[:-1]) and tengah[-1] == ';':
            catat.append('butir kedua terakhir tanpa "dan"/"atau"')
        if catat:
            item.append(f'n{nid}.{il} mulai {g[0]["id"]}: awal={awal} akhir={akhir} -> {"; ".join(catat)} | {g[0]["teks"][:60]!r}')
    L.tambah('Daftar bernomor: pola awal/akhir butir', item,
             'frasa lanjutan kalimat pengantar: huruf kecil, ";" dan "; dan", titik di butir terakhir; kalimat lengkap: kapital dan titik')

    # 10. Penomoran diketik manual (bukan numbering Word)
    item = [f'{u["id"]}: {u["teks"][:80]!r}' for u in badan
            if u['jenis'] == 'p' and not u['num'] and re.match(r'^\s*(\(?[a-z]\)|[a-z]\.|\d{1,2}[.)])\s*\t?\S', u['teks'])
            and not re.match(r'^\s*\d{1,2}\.\d', u['teks'])]
    L.tambah('Penomoran diketik manual', item, 'utamakan numbering Word asli agar indentasi dan urutan rapi')

    # 11. Istilah asing tidak dimiringkan
    item = []
    for u in badan:
        rr = runs(u['el'])
        teks_gabung = ''.join(t for t, *_ in rr)
        miring = []
        for t, i, *_ in rr:
            miring.extend([i] * len(t))
        for istilah in ISTILAH_ASING:
            for m in re.finditer(r'\b' + re.escape(istilah) + r'\b', teks_gabung, re.I):
                if not all(miring[m.start():m.end()]):
                    item.append(f'{u["id"]}: {m.group(0)!r} | {konteks(teks_gabung, m.start(), m.end(), 35)}')
    L.tambah('Istilah asing belum dimiringkan', item, 'abaikan nama produk (mis. "Siskeudes Online") dan istilah yang sudah diserap; miring dari gaya paragraf tidak terbaca')

    # 12. Placeholder dan teks merah
    item = []
    for u in badan:
        merah = ''.join(t for t, _i, _b, m in runs(u['el']) if m)
        if merah.strip():
            item.append(f'{u["id"]}: teks merah {merah.strip()[:70]!r}')
        for m in re.finditer(r'\(\s*\.\s*\)|\.{3,}|…|\bx{3,}\b|\[\s*\.\.\.\s*\]|<[^<>]{2,40}>', u['teks']):
            item.append(f'{u["id"]}: {konteks(u["teks"], m.start(), m.end(), 35)!r}')
    L.tambah('Placeholder / teks merah yang belum diisi', item)

    # 13. Kalimat terlalu panjang
    item = []
    for u in badan:
        if u['jenis'] != 'p':
            continue
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z“])', u['teks']):
            n = len(s.split())
            if n > a.maks_kata:
                item.append(f'{u["id"]}: {n} kata | {s[:110]!r}')
    L.tambah(f'Kalimat lebih dari {a.maks_kata} kata', item)

    # 14. Informasi berulang: kemiripan himpunan kata isi antarkalimat.
    #     Kalimat yang mirip dengan 2 kalimat lain atau lebih dianggap pola baku (mis. paragraf per desa) dan dipisahkan.
    henti = set('yang dan di ke dari pada dengan untuk dalam atau tersebut ini itu telah sudah belum sebagai oleh karena '
                'sehingga akan juga serta tetapi namun bahwa adalah yaitu antara lain masih hanya lebih tidak ada'.split())
    kal = []
    for u in badan:
        if u['jenis'] != 'p':
            continue
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z“])', u['teks']):
            w = {x for x in re.findall(r'[a-z]+', s.lower()) if x not in henti and len(x) > 2}
            if len(w) >= 6:
                kal.append((u['id'], s, w))
    indeks = defaultdict(set)
    for i, (_, _, w) in enumerate(kal):
        for x in w:
            indeks[x].add(i)
    mitra = defaultdict(set)
    pasangan = []
    for i, (_, _, w) in enumerate(kal):
        cnt = defaultdict(int)
        for x in w:
            for j in indeks[x]:
                if j > i:
                    cnt[j] += 1
        for j, c in cnt.items():
            jac = c / len(w | kal[j][2])
            if jac >= 0.6 and kal[i][0] != kal[j][0]:
                pasangan.append((i, j, jac))
                mitra[i].add(j)
                mitra[j].add(i)
    item, pola = [], {}
    for i, j, jac in sorted(pasangan, key=lambda x: -x[2]):
        if len(mitra[i]) >= 2 or len(mitra[j]) >= 2:
            akar = min({i} | mitra[i])
            pola.setdefault(akar, {i} | mitra[i])
            continue
        item.append(f'{kal[i][0]} ~ {kal[j][0]} ({jac:.0%}): {kal[i][1][:80]!r} || {kal[j][1][:80]!r}')
    L.tambah('Informasi yang sama di dua tempat (kemungkinan pengulangan)', item, 'putuskan tempat paling relevan; sisanya dirujuk atau dihapus')
    item = [f'{len(g)} kalimat, mis. {kal[a_][0]}: {kal[a_][1][:90]!r}' for a_, g in pola.items()]
    L.tambah('Pola kalimat berulang (biasanya disengaja, cek variasinya)', item)

    L.cetak()


if __name__ == '__main__':
    main()
