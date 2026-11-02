---
name: mpp-bpkp
description: "Buat paket dokumen MPP BPKP untuk penyiapan Surat Tugas dari file isian XLSX, termasuk rencana, pengantar, ST manual atau output SIMA-NG, KM 4/5/6, DPP, pakta, dan laporan PIA yang berlaku. Gunakan saat diminta membuat seluruh kelengkapan ST dalam satu folder nama penugasan."
tags: [bpkp, mpp, surat-tugas, audit-planning, docx, peraturan-bpkp-2-2023, peraturan-bpkp-4-2026]
---

# MPP BPKP

Hasilkan paket perencanaan yang sudah terisi dari satu workbook, memakai DOCX asli pada [assets/templates](assets/templates). Pertahankan kop, logo, tabel, header berulang, border, dan penomoran templat. Identitas awal Papua Tengah; profil unit lain dapat diisi pada DATA. Jangan membangun ulang dokumen dengan gaya generik.

## Jalur utama: satu file, satu prompt

1. Gunakan XLSX yang dirujuk pengguna. File isian awal tersedia pada `D:/autoST/Isian_DATA_MPP_BPKP.xlsx` dan [assets/Isian_DATA_MPP_BPKP.xlsx](assets/Isian_DATA_MPP_BPKP.xlsx). Workbook sumber lama `D:/autoST/KM4_KM5_KM6.xlsx` tetap menjadi acuan pemetaan DATA, bukan sasaran perubahan. Untuk membuat salinan isian kosong baru, jalankan `scripts/create_workbook.py <output.xlsx>`.
2. Baca workbook dengan formula dan cache. Untuk memahami sel/tab, lihat [references/isian-dan-generator.md](references/isian-dan-generator.md). DATA menyimpan identitas/jadwal dan lokasi sumber; IHP menyimpan Insilwas bila tidak dibaca dari KAP. Workbook pengguna tidak memuat isian risiko, narasi DPP, atau program kerja. Tambahan anggota tim tidak terbatas pada 12 orang contoh. Gunakan `TIM_TAMBAHAN`, dengan alokasi masing-masing pada `JAM_TIM`.
3. Adopsi substansi `buat-dpp`: baca KAP/Insilwas, pedoman teknis, dan hasil PIA yang relevan sebelum menyusun/mereviu narasi. Bila workbook hanya berisi identitas, susun isian substansi pada **salinan kerja** dari sumber yang tersedia. Jangan mengarang hasil PIA, fakta klien, mandat, tingkat keyakinan, nomor surat, tanggal, nama/NIP, atau bukti pemenuhan. Bila data faktual yang diperlukan tidak tersedia, laporkan kekurangan spesifik dari preflight. Keluaran dengan placeholder atau paragraf kosong bukan paket lengkap.
4. Baca fakta dan anggaran dengan perintah berikut. Selanjutnya susun rancangan JSON kerja sesuai [panduan risiko, TAO/TEO dan KM 6](references/risiko-tao-teo-km6.md). Rancangan ini dibuat agent dari sumber, bukan diminta sebagai isian tambahan pengguna. Ikuti rantai Insilwas → risiko klien → TAO/TEO → program kerja/KM 6 → task bernama. Dahulukan TAO/TEO pusat dalam pedoman dan pertahankan rumusannya. Bila tidak tersedia, nyatakan tujuan lokal sebagai usulan tentatif. Periksa rancangan menggunakan `--content <rancangan.json> --check` sebelum menghasilkan folder:

   ```powershell
   python "C:/Users/Admin/.codex/skills/mpp-bpkp/scripts/generate_mpp.py" "<isian.xlsx>" --inspect
   ```

5. Jika siap, buat seluruh dokumen, render PDF, dan gabungkan pratinjau:

   ```powershell
   python "C:/Users/Admin/.codex/skills/mpp-bpkp/scripts/generate_mpp.py" "<isian.xlsx>" --content "<rancangan.json>" --output-root "D:/autoST/Hasil_MPP"
   ```

   Generator menempatkan berkas di `<output-root>/<nama penugasan>/`. Nama direktori dibersihkan hanya dari karakter yang tidak sah pada Windows; nama asli dicatat dalam manifest. Bila sudah ada hasil sebelumnya, versi baru ditempatkan di subfolder `Versi_<waktu>` dalam folder penugasan tersebut. Jangan menimpa hasil pengguna.
6. Periksa `Manifest_MPP.json`, jumlah dokumen, data personel, kesesuaian jam, dan hasil render. Buka pratinjau khususnya kop surat, halaman terakhir tabel panjang, pakta, serta blok pengesahan. Validasi OOXML melalui validator skill `docx` jika tersedia. Jika tata letak memerlukan koreksi, pertahankan font/format templat dan sesuaikan pemisahan baris/halaman; jangan mengecilkan seluruh dokumen agar muat satu halaman.
7. Berikan tautan folder hasil dan pratinjau. Sebutkan pengecualian laporan PIA, sumber SIMA-NG yang digunakan, dan kekurangan yang masih material. Hindari menyebut konsep sebagai dokumen yang telah disahkan.

## Pemilihan dokumen

| No. | Dokumen | Sumber/perlakuan |
|---|---|---|
| 01–04 | Lembar rute, checklist SIMA LAK, checklist MPP, rencana penugasan | Templat, diisi dari workbook |
| 05 | Surat pengantar penugasan kepada objek | Selalu manual DOCX |
| 06 | Konsep ST | Manual DOCX atau salinan output SIMA-NG |
| 07–08 | KM 4 alokasi waktu, KM 5 kartu penugasan | Manual/autoST, atau output SIMA-NG bila tersedia |
| 09 | Nota dinas dan laporan hasil PIA | Hasil manual penugasan PIA sebelumnya; hanya untuk pengawasan berikutnya |
| 10–12 | DPP, KM 6 program kerja, pakta integritas | Templat, diisi dari workbook |

**ST untuk penugasan PIA:** laporan hasil PIA belum menjadi prasyarat. Jangan mewajibkan, membuat, atau mengarang laporan hasil PIA ketika menerbitkan ST PIA. Generator menghasilkan 11 dokumen dan menandai butir hasil PIA pada checklist sebagai N/A. Pengecualian tersebut tidak otomatis meniadakan DPP atau program kerja PIA.

**ST pengawasan berikutnya:** gunakan laporan hasil PIA yang dibuat manual sebagai dasar DPP. Sumber laporan dapat berupa FILE yang sudah ada atau ISIAN hasil nyata yang telah tersedia dan dirangkum ke bagian pia pada rancangan. FILE disalin utuh, termasuk bila berupa PDF; jangan mengubah laporan yang sudah ditandatangani agar menyerupai konsep baru. Dengan jalur ini paket memuat 12 dokumen.

## Adopsi buat-dpp, buat-st, dan TND

- Untuk penyusunan substansi DPP, baca skill `buat-dpp` yang terpasang; untuk interaksi SIMA-NG yang memang diminta pengguna, baca skill `buat-st`. Ringkasan integrasi dan konflik yang sudah diketahui tersedia pada [references/adopsi-skill.md](references/adopsi-skill.md).
- Terapkan enam komponen DPP. Pastikan Insilwas pada rencana dan DPP sama, risiko klien terkait Insilwas, TAO/TEO menjembatani risiko dengan program kerja, dan prosedur KM 6 menjawab TAO/TEO tersebut. Pastikan pula alokasi jam konsisten antar KM. Risiko klien berbeda dari risiko penugasan. KM 6 dan program kerja adalah instrumen yang sama; versi rinci memuat nama orang pada setiap task, bukan hanya peran Tim/KT/AT. Tingkat keyakinan mengikuti jenis penugasan/pedoman; tidak selalu limited assurance atau konsultansi.
- KM 4 pada paket ini bernama **Alokasi Waktu Pengawasan**, KM 5 **Kartu Penugasan**, dan KM 6 **Program Kerja Pengawasan**. Jangan mengikuti label KM 4/KM 5 yang tertukar dalam narasi lama `buat-st`.
- Jumlah hari ST dihitung sebagai hari kerja rentang tanggal, dengan Sabtu/Minggu otomatis dikecualikan (sheet LIBUR tidak lagi diperlukan). Periksa hari orang KT dari KM 4 sama dengan hari ST. Jam/hari 6,5 merupakan parameter workbook asal yang dapat diubah; tidak ada rasio PM/PT/KT 1:1:2 yang otomatis menjadi aturan umum.
- Nama tim diisi via searchable dropdown yang merujuk sheet `Pegawai` (database 6.500+ pegawai BPKP), dengan NIP terisi otomatis lewat VLOOKUP. Isian yang tidak memiliki output langsung ke dokumen (seperti lokasi baris 17, kode unit baris 81, profil unit baris 82–88, dan status checklist baris 101–104) bersifat opsional/otomatis dan tidak wajib diisi ulang oleh pengguna.
- Surat pengantar selalu manual. Jalur SIMA-NG hanya menyalin output yang tersedia. Cocokkan nama penugasan, personel, tanggal, alokasi waktu, dan pejabat dari file SIMA-NG dengan workbook sebelum dipaketkan. Berkas lokal bukan bukti ST telah tersimpan/terkirim pada aplikasi.
- Membuat paket lokal tidak mencakup pengiriman ke Reviu Dalnis atau perubahan data SIMA-NG. Jika pengguna meminta tindakan aplikasi, gunakan `buat-st` dalam lingkup permintaan tersebut; jangan menjalankan langkah penghentian seluruh proses Edge dari panduan lama.
- Aturan pengguna dan TND yang sudah diperiksa mengungguli resep lama skill. Gunakan tabel berkotak sesuai contoh, termasuk garis luar pakta. Abaikan anjuran lama menghapus semua garis vertikal, pakta harus satu halaman, margin bawah 20 mm sebagai aturan universal, penyalinan scan tanda tangan, atau pengisian nomor fiktif `000000`.
- Templat asli berlandaskan MPP Peraturan BPKP 2/2023 dan TND Peraturan BPKP 4/2026 yang diberikan pengguna. [references/acuan-format.md](references/acuan-format.md) memuat sumber visual dan batas penerapannya. Tidak perlu menelusuri ulang Drive setiap kali jika berkas aset dan sumber yang diperlukan masih tersedia.

## Keandalan hasil

- Generator membaca salinan sementara workbook, menghitung ulang menggunakan instance Excel tersendiri, dan tidak menyimpan perubahan ke input. Ia memakai cache formula yang terhitung, memeriksa error formula, NIP sebagai teks 18 digit, urutan kalender, dan keseimbangan jam.
- Tidak ada folder hasil penugasan sebelum preflight lulus. Pembuatan dilakukan pada staging; kesalahan render menghentikan publikasi. Blok tanda tangan, paraf, realisasi, dan bukti kegiatan yang belum terjadi tetap kosong.
- `--cached` hanya untuk cache formula yang baru dihitung dan telah diperiksa. `--no-pdf` hanya bila pengguna tidak memerlukan PDF atau Word tidak tersedia; laporkan bahwa pratinjau belum dibuat. Jangan mengklaim pemeriksaan visual yang belum dilakukan.
- Untuk masalah skrip, uji di direktori terpisah dengan data fiktif; jangan memakai/mengganti workbook asli atau mengirim apa pun ke SIMA-NG sebagai pengujian.
