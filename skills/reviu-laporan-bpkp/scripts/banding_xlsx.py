"""Bandingkan dua versi kertas kerja (KKE) .xlsx sel demi sel. Hanya membaca, tidak pernah menyimpan.

Pemakaian:
  python banding_xlsx.py KKE_lama.xlsx KKE_baru.xlsx [--maks 80] [--sheet "4_1 Kas Opname"]

Yang dibandingkan adalah nilai tersimpan (hasil rumus terakhir yang disimpan Excel), bukan rumusnya.
Teks dinormalkan (spasi berlebih diabaikan) dan angka dibulatkan 6 desimal.
"""
import argparse
import sys
import warnings

import openpyxl

warnings.filterwarnings('ignore')


def grid(ws):
    g = {}
    for row in ws.iter_rows():
        for c in row:
            if c.value not in (None, ''):
                g[c.coordinate] = c.value
    return g


def norm(v):
    if isinstance(v, float):
        return round(v, 6)
    if isinstance(v, str):
        return ' '.join(v.split())
    return v


def kunci(k):
    huruf = ''.join(c for c in k if c.isalpha())
    return (int(''.join(c for c in k if c.isdigit())), len(huruf), huruf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lama')
    ap.add_argument('baru')
    ap.add_argument('--maks', type=int, default=80)
    ap.add_argument('--sheet', default=None)
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    A = openpyxl.load_workbook(a.lama, read_only=True, data_only=True)
    B = openpyxl.load_workbook(a.baru, read_only=True, data_only=True)
    print('sheet hanya di lama:', sorted(set(A.sheetnames) - set(B.sheetnames)) or '-')
    print('sheet hanya di baru:', sorted(set(B.sheetnames) - set(A.sheetnames)) or '-')
    total = 0
    for nama in A.sheetnames:
        if nama not in B.sheetnames or (a.sheet and nama != a.sheet):
            continue
        ga, gb = grid(A[nama]), grid(B[nama])
        beda = [(k, norm(ga.get(k)), norm(gb.get(k))) for k in sorted(set(ga) | set(gb), key=kunci) if norm(ga.get(k)) != norm(gb.get(k))]
        if beda:
            total += len(beda)
            print(f'\n===== {nama}: {len(beda)} sel berubah')
            for k, va, vb in beda[:a.maks]:
                print(f'  {k}: {str(va)[:150]!r} -> {str(vb)[:150]!r}')
            if len(beda) > a.maks:
                print(f'  ... {len(beda) - a.maks} lainnya')
    print(f'\nTOTAL sel berubah: {total}')


if __name__ == '__main__':
    main()
