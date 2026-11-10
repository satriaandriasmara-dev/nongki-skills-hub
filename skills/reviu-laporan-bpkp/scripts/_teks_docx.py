"""Utilitas bersama: membaca .docx menjadi unit teks berlabel.

Label dipakai sama oleh dump_docx.py dan cek_mekanis.py:
  P001, P002, ...   paragraf badan naskah yang berisi teks atau gambar
  T01R02C03         sel tabel ke-1, baris ke-2, kolom ke-3
"""
from docx import Document
from docx.oxml.ns import qn

W_T = qn('w:t')
MERAH = {'FF0000', 'C00000', 'EE0000', 'E00000'}


def teks(el):
    return ''.join(t.text or '' for t in el.iter(W_T))


def numpr(p):
    """(numId, ilvl) bila paragraf memakai numbering Word, selain itu None."""
    ppr = p.find(qn('w:pPr'))
    if ppr is None:
        return None
    n = ppr.find(qn('w:numPr'))
    if n is None:
        return None
    nid = n.find(qn('w:numId'))
    il = n.find(qn('w:ilvl'))
    return (nid.get(qn('w:val')) if nid is not None else '?', il.get(qn('w:val')) if il is not None else '0')


def gaya(p):
    ppr = p.find(qn('w:pPr'))
    st = ppr.find(qn('w:pStyle')) if ppr is not None else None
    return st.get(qn('w:val')) if st is not None else ''


def _on(rpr, tag):
    if rpr is None:
        return False
    e = rpr.find(qn(tag))
    return e is not None and e.get(qn('w:val')) not in ('0', 'false', 'none')


def runs(p):
    """Daftar (teks, miring, tebal, merah) per run. Hanya format langsung pada run yang terbaca."""
    out = []
    for r in p.iter(qn('w:r')):
        t = ''.join(x.text or '' for x in r.findall(W_T))
        if not t:
            continue
        rpr = r.find(qn('w:rPr'))
        col = rpr.find(qn('w:color')) if rpr is not None else None
        merah = col is not None and (col.get(qn('w:val')) or '').upper() in MERAH
        out.append((t, _on(rpr, 'w:i'), _on(rpr, 'w:b'), merah))
    return out


def units(path):
    """Kembalikan (doc, daftar unit). Unit = dict(id, jenis, teks, num, el, gambar, gaya, tabel)."""
    doc = Document(path)
    out = []
    n_p = 0
    n_t = 0
    for el in doc.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            t = teks(el)
            pic = bool(list(el.iter(qn('w:drawing'))))
            if not t.strip() and not pic:
                continue
            n_p += 1
            out.append(dict(id=f'P{n_p:03d}', jenis='p', teks=t, num=numpr(el), el=el, gambar=pic, gaya=gaya(el), tabel=None))
        elif tag == 'tbl':
            n_t += 1
            for ri, tr in enumerate(el.findall(qn('w:tr')), 1):
                for ci, tc in enumerate(tr.findall(qn('w:tc')), 1):
                    for p in tc.findall(qn('w:p')):
                        t = teks(p)
                        if t.strip():
                            out.append(dict(id=f'T{n_t:02d}R{ri:02d}C{ci:02d}', jenis='sel', teks=t, num=numpr(p), el=p,
                                            gambar=False, gaya=gaya(p), tabel=n_t))
    return doc, out


def is_judul(u):
    """Heuristik judul: paragraf badan pendek tanpa tanda baca akhir, bernomor/tebal/kapital/gaya Heading."""
    if u['jenis'] != 'p' or u['gambar']:
        return False
    t = u['teks'].strip()
    if not t or len(t) > 150 or t.endswith(('.', ';', ':', ',', '; dan', '; atau', ', dan', ', atau')):
        return False
    rr = runs(u['el'])
    tebal = bool(rr) and all(b for t_, _i, b, _m in rr if t_.strip())
    huruf = [c for c in t if c.isalpha()]
    kapital = bool(huruf) and sum(c.isupper() for c in huruf) / len(huruf) > 0.8
    return bool(u['num']) or tebal or kapital or 'heading' in u['gaya'].lower() or 'judul' in u['gaya'].lower()
