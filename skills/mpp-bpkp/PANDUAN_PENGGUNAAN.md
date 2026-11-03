# PANDUAN PENGGUNAAN SKILL MPP BPKP

Panduan komprehensif ini menjelaskan cara penggunaan modul dan skill **MPP-BPKP** (*Manajemen Penugasan Pengawasan Badan Pengawasan Keuangan dan Pembangunan*), baik secara otomatis melalui AI Coding Assistant (Antigravity / Codex / Claude) maupun secara manual melalui skrip Python.

Modul ini disusun berlandaskan:
- **Peraturan BPKP Nomor 2 Tahun 2023** tentang Manajemen Penugasan Pengawasan (MPP).
- **Peraturan BPKP Nomor 4 Tahun 2026** tentang Tata Naskah Dinas (TND) di lingkungan BPKP.

---

## 1. Pembaruan & Penyederhanaan Terkini

1. **Bebas Data Pribadi Kepegawaian (Aman untuk Publik / Git):**
   - Berkas master `Isian_DATA_MPP_BPKP.xlsx` di repositori tidak menyertakan sheet database pegawai demi perlindungan privasi.
   - Pengisian nama dan NIP tim dilakukan secara manual langsung pada sheet `DATA` (kolom kuning).
   - Kolom NIP diformat sebagai teks (`@`) untuk menjaga ketepatan 18 digit angka.
   - Pengguna yang memiliki database pegawai internal di komputer lokal dapat menggunakan opsi `--with-pegawai` pada skrip `create_workbook.py` untuk mengaktifkan *searchable dropdown* dan *auto-VLOOKUP* secara privat.

2. **Pembersihan Total Isian Tanpa Output:**
   - **Path Output SIMA-NG Dihapus:** Kolom path output konsep ST, KM-4, dan KM-5 SIMA-NG telah dibuang dari lembar isian.
   - **Lokasi Penugasan Dihapus:** Kolom lokasi penugasan telah dibuang karena tidak ada token `{{LOKASI}}` di templat dokumen (dokumen resmi menggunakan alamat objek atau kota penerima).
   - **Kode Unit & Rincian Profil Kop Dihapus:** Kolom kode unit, alamat kantor, email, website, dan kop surat dibuang dari lembar isian pengguna. Sistem secara cerdas mengambil profil baku perwakilan dari `profil_unit.json`.
   - **Status Checklist MPP Dihapus:** Status checklist DPP, Rencana, dan KM-6 otomatis ditetapkan sebagai `TERSEDIA` (atau `N/A` untuk PIA) saat dokumen dibuat.

3. **Panduan & Contoh Isian Langsung di Sheet `DATA` (Sheet `PANDUAN` Dihapus):**
   - Sheet `PANDUAN` yang terpisah telah dihapus.
   - Pada sheet `DATA`, **Kolom D** kini berfungsi sebagai **"Petunjuk & Contoh Isian Nyata"**. Setiap baris isian langsung disertai contoh konkret (misalnya judul evaluasi, sasaran, dasar hukum, pedoman teknis, dsb.).

4. **Sheet `IHP` Disederhanakan (1 Kolom Tunggal):**
   - Kolom "Rujukan KAP/Halaman" dihapus.
   - Kolom ID dan Insilwas disatukan menjadi 1 kolom saja: `Informasi Hasil Pengawasan (Insilwas)`.
   - Skrip secara otomatis mengekstrak nomor/ID dan uraian teksnya (mendukung format `IHP-01`, penomoran angka `1.`, atau teks polos).

5. **Seluruh Tim Disatukan di Sheet `DATA`:**
   - Disediakan slot langsung untuk:
     * Wakil Penanggung Jawab (PM) - Baris 4
     * Pengendali Teknis (PT) - Baris 5
     * Ketua Tim (KT) - Baris 6
     * **Anggota Tim 1 s.d. 20 (AT 1 s.d. AT 20) - Baris 7 s.d. 26**
     * Kepala Perwakilan - Baris 27
   - Cukup isi baris anggota yang ditugaskan; baris yang tidak digunakan **cukup dibiarkan kosong**.
   - Kolom Golongan telah ditiadakan.

---

## 2. Struktur Workbook Excel (`Isian_DATA_MPP_BPKP.xlsx`)

Saat membuka berkas Excel, pengguna disajikan **4 sheet aktif**:

| No | Nama Sheet | Fungsi Utama |
|---|---|---|
| **1** | **`DATA`** | Lembar isian utama (Tim, Detail Penugasan, Jadwal, Surat) lengkap dengan contoh isian di Kolom D. |
| **2** | **`IHP`** | Daftar butir Informasi Hasil Pengawasan (1 kolom praktis). |
| **3** | **`TEMBUSAN`**| Daftar instansi/jabatan penerima tembusan surat. |
| **4** | **`JAM_TIM`** | Alokasi jam kerja orang per fase (terhitung otomatis dari DATA). |

---

## 3. Daftar 12 Dokumen Hasil Paket MPP

| No. | Kode / Nama Dokumen | Keterangan & Ketentuan |
|---|---|---|
| **01** | **Lembar Rute Perencanaan** | Lembar kendali disposisi rute persetujuan perencanaan. |
| **02** | **Checklist SIMA-LAK & Perencanaan** | Formulir checklist verifikasi kelengkapan dan input sistem. |
| **03** | **Checklist Pemenuhan MPP** | Verifikasi kepatuhan seluruh instrumen manajemen penugasan pengawasan. |
| **04** | **Rencana Penugasan** | Ringkasan identitas, susunan tim, sasaran, dan jadwal per fase. |
| **05** | **Surat Pengantar Penugasan** | Surat dinas manual resmi yang ditujukan kepada objek pengawasan. |
| **06** | **Konsep Surat Tugas (ST)** | Konsep ST manual DOCX resmi TND BPKP. |
| **07** | **KM-4 (Alokasi Waktu Pengawasan)** | Rincian alokasi hari/jam penugasan tiap personel per fase. |
| **08** | **KM-5 (Kartu Penugasan)** | Kartu instrumen penugasan pengawasan. |
| **09** | **Nota Dinas & Laporan Hasil PIA** | *ST PIA = N/A (11 dokumen); ST Lanjutan = Wajib (12 dokumen).* |
| **10** | **Desain Penugasan Pengawasan (DPP)**| Dokumen teknis perencanaan metodologi, lokus, dan risiko. |
| **11** | **KM-6 (Program Kerja Pengawasan / PKA)** | Prosedur langkah kerja rinci yang menjawab TAO/TEO. |
| **12** | **Pakta Integritas** | Komitmen integritas tim pengawasan berformat tabel berkotak resmi. |

---

## 4. Panduan Pengisian Sheet `DATA`

1. **Susunan Tim (Baris 4–27):**
   - **Kolom B (Nama Pegawai):** Ketik nama pegawai yang ditugaskan.
   - **Kolom C (NIP):** Ketik NIP 18 digit angka (disimpan sebagai teks).
   - **Kolom D:** Memuat petunjuk dan contoh isian.
   - Cukup isi baris anggota yang ditugaskan (tersedia hingga AT 20); baris AT yang tidak terpakai dibiarkan kosong.
2. **Detail Penugasan (Baris 29–37):**
   - **Bidang (B29):** Pilih dari dropdown (`Umum`, `IPP`, `APD`, `AN`, `Investigasi`, `P3A`).
   - **Nama Penugasan (B30)**, **Sasaran (B31)**, **Objek (B33)**, **Periode (B34)**, **Alamat (B37)**: Isi sesuai penugasan (contoh tersedia di Kolom D).
3. **Jadwal & Waktu (Baris 39–54):**
   - **Tanggal ST (B39):** Masukkan tanggal konsep Surat Tugas.
   - **Hari Persiapan (B41)**, **Pelaksanaan (B42)**, **Penyelesaian (B43)**: Isi jumlah hari kerja tiap tahap (misal: 1, 3, 1).
   - Seluruh tanggal dan total hari ST terhitung otomatis (Sabtu dan Minggu otomatis dilewati).
   - **Jumlah AT (B54):** Otomatis menghitung jumlah anggota tim yang terisi nama.
4. **Kelengkapan Surat & Administrasi (Baris 56–80):**
   - **Jenis (B56):** Pilih `PIA` atau `PENGAWASAN`.
   - **Bentuk (B57):** Pilih `EVALUASI`, `AUDIT`, `PIA`, atau `LAINNYA`.
   - **Sektor, Tema, Topik (B58–B60)**: Bidang pengawasan.
   - **Tujuan (B61)**, **Ruang Lingkup (B62)**, **Penerima Laporan (B63)**, **Sumber Pembiayaan (B64)**, **Dasar Hukum (B65)**, **Pedoman (B66)**, **Penerima Surat (B67)**, **Kota (B68)**.

---

## 5. Cara Penggunaan

### Menggunakan AI Coding Assistant (Direkomendasikan)
Cukup lampirkan file Excel isian dan dokumen referensi teknis, lalu berikan instruksi:
```text
Gunakan $mpp-bpkp untuk membuat seluruh dokumen MPP dari file isian XLSX ini dalam folder nama penugasannya.
```

### Menggunakan Command Line (Terminal)
- **Inspect**:
  ```powershell
  python scripts/generate_mpp.py "assets/Isian_DATA_MPP_BPKP.xlsx" --inspect
  ```
- **Preflight Check**:
  ```powershell
  python scripts/generate_mpp.py "examples/UJI SINTETIS Evaluasi Nabire.xlsx" --content "examples/UJI SINTETIS Evaluasi Nabire.json" --cached --check
  ```
- **Generate Dokumen Lengkap (DOCX & PDF)**:
  ```powershell
  python scripts/generate_mpp.py "path/ke/isian.xlsx" --content "path/ke/rancangan.json" --output-root "<folder-hasil>"
  ```
- **Membuat Master Isian Baru**:
  ```powershell
  # Versi bersih (manual input, tanpa data kepegawaian):
  python scripts/create_workbook.py "path/ke/isian.xlsx" --overwrite

  # Versi lokal dengan database pegawai internal:
  python scripts/create_workbook.py "path/ke/isian.xlsx" --overwrite --with-pegawai
  ```
