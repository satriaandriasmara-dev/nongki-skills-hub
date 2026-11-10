"""Ekstrak seluruh teks laporan .docx untuk dibaca utuh.

Pemakaian:
  python dump_docx.py laporan.docx > teks.txt

Keluaran:
  P012 [n3.0] teks paragraf {MERAH} {GAMBAR}
    [n3.0]   = paragraf memakai numbering Word (numId 3, level 0)
    {MERAH}  = ada teks berwarna merah (biasanya placeholder)
    {GAMBAR} = paragraf berisi gambar/grafik
  [T05] lalu baris tabel: R01 | sel 1 | sel 2   (paragraf dalam satu sel dipisah " / ")
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx.oxml.ns import qn  # noqa: E402
from _teks_docx import teks, numpr, runs  # noqa: E402
from docx import Document  # noqa: E402


def main(path):
    sys.stdout.reconfigure(encoding='utf-8')
    doc = Document(path)
    n_p = n_t = 0
    for el in doc.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            t = teks(el)
            pic = bool(list(el.iter(qn('w:drawing'))))
            if not t.strip() and not pic:
                continue
            n_p += 1
            num = numpr(el)
            lv = f'[n{num[0]}.{num[1]}] ' if num else ''
            merah = ' {MERAH}' if any(m for *_, m in runs(el)) else ''
            gb = ' {GAMBAR}' if pic else ''
            print(f'P{n_p:03d} {lv}{t}{merah}{gb}')
        elif tag == 'tbl':
            n_t += 1
            print(f'  [T{n_t:02d}]')
            for ri, tr in enumerate(el.findall(qn('w:tr')), 1):
                cells = []
                for tc in tr.findall(qn('w:tc')):
                    cells.append(' / '.join(teks(p) for p in tc.findall(qn('w:p'))).strip())
                print(f'   R{ri:02d} | ' + ' | '.join(cells))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
