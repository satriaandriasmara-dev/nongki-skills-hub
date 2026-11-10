"""Bandingkan teks dua versi laporan .docx untuk memastikan hanya perubahan yang disetujui yang masuk.

Pemakaian:
  python banding_docx.py "Laporan (Draf v3).docx" "Laporan (Draf v4).docx" [--lebar 220]

Label paragraf (P012) diabaikan saat membandingkan, sehingga sisipan paragraf tidak membuat
seluruh sisa dokumen terlihat berubah. Baris "-" = teks lama, "+" = teks baru.
"""
import argparse
import difflib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _teks_docx import units  # noqa: E402


def baris(path):
    _, U = units(path)
    out = []
    for u in U:
        lv = f'[n{u["num"][0]}.{u["num"][1]}] ' if u['num'] else ''
        lok = 'sel ' if u['jenis'] == 'sel' else ''
        out.append(f'{lok}{lv}{u["teks"]}')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lama')
    ap.add_argument('baru')
    ap.add_argument('--lebar', type=int, default=220)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    A, B = baris(a.lama), baris(a.baru)
    n = 0
    for x in difflib.unified_diff(A, B, lineterm='', n=0):
        if x.startswith(('---', '+++', '@@')):
            if x.startswith('@@'):
                print()
            continue
        n += 1
        print(x[:a.lebar])
    print(f'\nBaris berubah: {n}')


if __name__ == '__main__':
    main()
