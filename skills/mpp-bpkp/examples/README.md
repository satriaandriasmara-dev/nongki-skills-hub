# Berkas Contoh Sintetis MPP BPKP

Folder ini berisi contoh rancangan (`--content`) sintetis untuk generator dokumen MPP BPKP:

1. **`UJI SINTETIS Evaluasi Nabire.json`**:
   - Contoh untuk penugasan non-PIA (Evaluasi).
   - Menghasilkan paket lengkap 12 dokumen (termasuk laporan hasil PIA sebelumnya).
   - Bentuk pengawasan: `EVALUASI` (menggunakan TEO - *Tentative Evaluation Objective*).

2. **`UJI SINTETIS PIA Nabire.json`**:
   - Contoh untuk penugasan awal Penelaahan Informasi Awal (PIA).
   - Menghasilkan paket 11 dokumen (laporan hasil PIA belum terbit sehingga ditandai N/A).
   - Bentuk pengawasan: `PIA`.

Pasangan workbook `.xlsx`-nya **tidak disertakan** karena `.gitignore` mengecualikan seluruh `*.xlsx` selain templat isian. Rancangan juga terkunci ke workbook asalnya melalui `input_sha256`, sehingga JSON di folder ini hanya berguna sebagai contoh struktur rancangan. Bila dipasangkan dengan workbook lain, hasilnya ditolak dengan pesan "Rancangan berasal dari versi input berbeda".

### Cara Menjalankan Uji Coba:

`verify_workflow.py` membuat ulang pasangan `.xlsx` + `.json` yang cocok (butuh Excel dan Word), lalu pasangan itu bisa dicek atau di-generate ulang:

```powershell
# Dari direktori root mpp-bpkp:
python scripts/verify_workflow.py "<folder-uji-kosong>" assets/Isian_DATA_MPP_BPKP.xlsx
python scripts/generate_mpp.py "<folder-uji-kosong>/UJI SINTETIS Evaluasi Nabire.xlsx" --content "<folder-uji-kosong>/UJI SINTETIS Evaluasi Nabire.json" --cached --check
```
