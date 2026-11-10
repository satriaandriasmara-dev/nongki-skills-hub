"""Pemeriksaan tata letak PDF hasil render laporan.

Pemakaian:
  python cek_tata_letak.py laporan.pdf
  python cek_tata_letak.py laporan.pdf --cari "Kas Seharusnya" "1.396.876.285" --keluar cek.png
  python cek_tata_letak.py laporan.pdf --halaman 9,14,31 --keluar cek.png

Yang diperiksa per halaman:
  - judul atau label butir yang tertinggal di bawah halaman (isinya di halaman berikutnya)
  - kalimat pengantar berakhir titik dua di bawah halaman (terpisah dari tabel/rincian)
  - baris "Sumber:" di puncak halaman (terpisah dari tabel/grafiknya)
  - ruang kosong besar di bawah halaman (selain halaman terakhir)
  - label nomor list yang miring/berwarna/berukuran beda dari teks isi
  - baris berisi 1 sampai 3 huruf kecil saja (kata terpotong di kolom tabel sempit, mis. "Pake/t")
--cari / --halaman menyusun gambar halaman berdampingan (PNG) untuk dilihat langsung.
"""
import argparse
import re
import statistics
import sys

import fitz  # PyMuPDF

LABEL = re.compile(r'^\s*(\(?[a-z]\)|[a-z]\.|\d{1,2}[.)])\s*$')
JUDUL = re.compile(r'^([A-Z]\.|[a-z]\.|\d{1,2}[.)]|[a-z]\)|[IVX]+\.)\s')
KATA_PENDEK = {'dan', 'di', 'ke', 'ini', 'itu', 'ada', 'per', 'tak', 'pun', 'kas', 'ya', 'dll', 'atas', 'rp', 'no', 'jan',
               'feb', 'mar', 'apr', 'mei', 'jun', 'jul', 'agu', 'sep', 'okt', 'nov', 'des', 'tbk', 'thn', 'tgl', 'org', 'unit', 'm', 'ha'}


def blok_isi(pg):
    h = pg.rect.height
    bl = [b for b in pg.get_text('blocks') if b[4].strip() and 45 < b[1] < h - 45 and not re.fullmatch(r'\s*\d{1,3}\s*', b[4])]
    return sorted(bl, key=lambda b: (b[1], b[0]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--gap', type=float, default=250, help='ambang ruang kosong bawah (pt)')
    ap.add_argument('--cari', nargs='*', default=[], help='teks yang halamannya ingin dilihat')
    ap.add_argument('--halaman', default='', help='nomor halaman dipisah koma')
    ap.add_argument('--keluar', default='cek_halaman.png', help='nama berkas PNG gabungan')
    ap.add_argument('--dpi', type=int, default=62)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    d = fitz.open(a.pdf)

    ukuran = []
    for pg in d:
        for b in pg.get_text('dict')['blocks']:
            for ln in b.get('lines', []):
                for s in ln['spans']:
                    if len(s['text'].strip()) > 20:
                        ukuran.append(round(s['size'], 1))
    modus = statistics.mode(ukuran) if ukuran else 12

    temuan = []
    for i, pg in enumerate(d):
        no = i + 1
        bl = blok_isi(pg)
        if not bl:
            continue
        atas, bawah = bl[0][4].strip(), bl[-1][4].strip()
        sisa = pg.rect.height - bl[-1][3]
        if len(bawah) < 120 and JUDUL.match(bawah) and not bawah.endswith(('.', ';', ',')):
            temuan.append((no, 'judul/butir tertinggal di bawah halaman', bawah[-90:]))
        elif bawah.endswith(':'):
            temuan.append((no, 'kalimat pengantar (titik dua) di bawah halaman', bawah[-90:]))
        if atas.startswith('Sumber'):
            gambar_di_atas = any(im['bbox'][3] <= bl[0][1] + 5 for im in pg.get_image_info())
            if not gambar_di_atas:
                temuan.append((no, 'baris "Sumber" di puncak halaman', atas[:90]))
        if sisa > a.gap and no < d.page_count:
            temuan.append((no, f'ruang kosong {sisa:.0f} pt di bawah halaman', bawah[-70:]))
        semua = []
        for b in pg.get_text('dict')['blocks']:
            for ln in b.get('lines', []):
                txt = ''.join(s['text'] for s in ln['spans']).strip()
                if txt:
                    semua.append((ln['bbox'], txt))
                s0 = ln['spans'][0]
                if LABEL.match(s0['text']):
                    if 'Italic' in s0['font'] or 'Oblique' in s0['font'] or s0['color'] != 0 or abs(s0['size'] - modus) > 0.4:
                        temuan.append((no, 'label nomor tidak seragam (miring/berwarna/ukuran beda)', f'{s0["text"].strip()} font={s0["font"]} ukuran={s0["size"]:.1f}'))
        # potongan kata: baris diawali 1-3 huruf kecil (bukan kata utuh) tepat di bawah baris sempit yang berakhir huruf
        for (fx0, fy0, fx1, fy1), ft in semua:
            m = re.match(r'([a-z]{1,3})(?:\s|$)', ft)
            if not m or m.group(1) in KATA_PENDEK:
                continue
            for (px0, py0, px1, py1), pt in semua:
                if pt == ft and (px0, py0) == (fx0, fy0):
                    continue
                if -4 <= fy0 - py1 <= 3 and fx0 >= px0 - 15 and fx1 <= px1 + 15 and px1 - px0 < 150 and pt[-1:].isalpha():
                    temuan.append((no, 'kata terpotong di kolom sempit', f'{pt[-25:]!r} + {ft!r}'))
                    break

    # tabel terbelah di dekat akhir halaman: baris judul tabel berulang di puncak halaman berikutnya
    for i in range(d.page_count - 1):
        pg, nx = d[i], d[i + 1]
        h = pg.rect.height
        isi = blok_isi(pg)
        bawah = {' '.join(b[4].split()): b for b in isi if b[1] > 0.6 * h}
        for b in blok_isi(nx)[:4]:
            t = ' '.join(b[4].split())
            if len(t) > 3 and t in bawah and not t.startswith(('Sumber', 'Catatan')):
                hb = bawah[t]
                baris = {round(x[1] / 4) for x in isi if x[1] >= hb[3] - 1 and not x[4].startswith(('Sumber', 'Catatan'))}
                if len(baris) <= 2:
                    temuan.append((i + 1, f'tabel terbelah, hanya {len(baris)} baris data tersisa di bawah halaman', t[:70]))
                break

    print(f'Halaman: {d.page_count} | ukuran huruf isi (modus): {modus}')
    if not temuan:
        print('Tidak ada masalah tata letak yang terdeteksi.')
    for no, jenis, isi in temuan:
        print(f'  hal. {no:3d} | {jenis} | {isi}')

    halaman = [int(x) for x in a.halaman.split(',') if x.strip()]
    for kunci in a.cari:
        k1 = ' '.join(kunci.split())
        hit = [i + 1 for i, pg in enumerate(d) if k1 in ' '.join(pg.get_text().split())]
        print(f'  cari {kunci!r}: halaman {hit if hit else "tidak ditemukan"}')
        halaman.extend(hit[:1])
    halaman = list(dict.fromkeys(h for h in halaman if 1 <= h <= d.page_count))
    if halaman:
        from PIL import Image
        for g in range(0, len(halaman), 3):
            ims = []
            for n in halaman[g:g + 3]:
                pix = d[n - 1].get_pixmap(dpi=a.dpi)
                ims.append(Image.frombytes('RGB', (pix.width, pix.height), pix.samples))
            out = Image.new('RGB', (sum(im.width for im in ims), max(im.height for im in ims)), 'white')
            x = 0
            for im in ims:
                out.paste(im, (x, 0))
                x += im.width
            nama = a.keluar if len(halaman) <= 3 else a.keluar.replace('.png', f'_{g // 3 + 1}.png')
            out.save(nama)
            print(f'  gambar: {nama} (halaman {halaman[g:g + 3]})')


if __name__ == '__main__':
    main()
