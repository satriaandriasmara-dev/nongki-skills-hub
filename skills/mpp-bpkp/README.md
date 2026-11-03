# Skill MPP BPKP (Manajemen Penugasan Pengawasan)

Paket dokumen perencanaan pengawasan dan penyiapan Surat Tugas (ST) otomatis berbasis Peraturan BPKP Nomor 2 Tahun 2023 dan Peraturan BPKP Nomor 4 Tahun 2026 (Tata Naskah Dinas).

## Panduan Lengkap
Silakan baca berkas panduan lengkap:
👉 **[PANDUAN_PENGGUNAAN.md](PANDUAN_PENGGUNAAN.md)**

## Fitur & Pembaruan Terkini
1. **Bebas Data Pribadi (Aman untuk Publik/Git):** Berkas master `Isian_DATA_MPP_BPKP.xlsx` di repositori tidak menyertakan database kepegawaian internal. Pengisian nama dan NIP tim dilakukan secara manual langsung pada sheet `DATA`. (Untuk penggunaan internal lokal, skrip menyediakan opsi `--with-pegawai`).
2. **Seluruh Tim Disatukan di Sheet `DATA`:** Disediakan slot langsung untuk PM, PT, KT, dan AT 1 s.d. AT 20. Baris yang tidak terpakai cukup dikosongkan (sangat fleksibel untuk 1, 2, atau banyak anggota tim). Sheet `TIM_TAMBAHAN` telah dihapus.
3. **Isian Golongan Ditiadakan:** Dokumen perencanaan pengawasan tidak mempersyaratkan golongan, sehingga kolom golongan telah dihapus dari isian pengguna.
4. **Pembersihan Total Isian:** Isian tanpa output (Lokasi, Kode Unit, Path Output SIMA-NG, Profil Kop Unit, dan Status Checklist) telah dibersihkan sepenuhnya dari sheet `DATA`.
5. **Panduan & Contoh Isian Langsung di Sheet `DATA`:** Sheet `PANDUAN` terpisah telah dihapus; Kolom D pada sheet `DATA` kini memuat petunjuk dan contoh konkret untuk setiap baris.
6. **Sheet `IHP` 1 Kolom Tunggal:** Butir Insilwas disatukan dalam 1 kolom; skrip otomatis mengekstrak nomor ID dan uraian teksnya.
7. **Bebas Sheet Libur:** Perhitungan hari kerja otomatis mengecualikan Sabtu dan Minggu tanpa circular reference.

## Ringkasan Cepat

### 1. Menyiapkan Isian
Buka berkas Excel:
`assets/Isian_DATA_MPP_BPKP.xlsx`
(Tersedia 4 sheet aktif: `DATA`, `IHP`, `TEMBUSAN`, dan `JAM_TIM`).

### 2. Menggunakan Prompt AI
Kirimkan prompt ini ke AI Assistant (Antigravity / Codex / Claude):
```text
Gunakan $mpp-bpkp untuk membuat seluruh dokumen MPP dari file isian XLSX ini dalam folder nama penugasannya.
```

### 3. Menggunakan Command Line
- **Inspect**:
  ```powershell
  python scripts/generate_mpp.py "<file.xlsx>" --inspect
  ```
- **Validasi Preflight**:
  ```powershell
  python scripts/generate_mpp.py "<file.xlsx>" --content "<rancangan.json>" --check
  ```
- **Generate Dokumen (DOCX & PDF)**:
  ```powershell
  python scripts/generate_mpp.py "<file.xlsx>" --content "<rancangan.json>" --output-root "<folder-hasil>"
  ```
- **Membuat Master Isian Baru**:
  ```powershell
  # Versi bersih (manual input, tanpa data kepegawaian):
  python scripts/create_workbook.py "path/ke/isian.xlsx" --overwrite

  # Versi lokal dengan database pegawai internal:
  python scripts/create_workbook.py "path/ke/isian.xlsx" --overwrite --with-pegawai
  ```
- **Uji Alur Lengkap (data sintetis, butuh Excel dan Word)**:
  ```powershell
  python scripts/verify_workflow.py "<folder-uji-kosong>" assets/Isian_DATA_MPP_BPKP.xlsx
  ```
