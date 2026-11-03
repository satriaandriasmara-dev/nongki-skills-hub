# Isian DATA dan pelaksanaan satu prompt

Workbook pengguna tidak meminta risiko, TAO/TEO, atau program kerja. Ketiganya disusun oleh skill dari Insilwas, pedoman pusat, laporan PIA yang relevan, dan data penugasan. Hasil analisis disimpan sebagai Rancangan_MPP.json bersama dokumen hasil, bukan sebagai formulir tambahan pengguna.

## Isi workbook

Workbook dirancang sangat ringkas dengan **4 sheet aktif**:

| Tab | Status | Isi pengguna |
|---|---|---|
| DATA | Aktif | Identitas penugasan, seluruh tim pengawasan (PM, PT, KT, AT 1..20), jadwal, surat, dan contoh isian langsung pada Kolom D |
| IHP | Aktif | Butir Insilwas dalam satu kolom tunggal (skrip otomatis mengekstrak ID dan uraian) |
| TEMBUSAN | Aktif | Jabatan/instansi tujuan tembusan surat tugas / pengantar |
| JAM_TIM | Aktif | Alokasi jam kerja orang per fase (nama dan NIP otomatis dari DATA, jam awal terhitung) |

Templat publik `assets/Isian_DATA_MPP_BPKP.xlsx` tidak memuat data kepegawaian. Sheet `Pegawai` (tersembunyi, untuk dropdown nama dan VLOOKUP NIP) hanya dibuat bila workbook lokal disusun dengan `scripts/create_workbook.py --with-pegawai`.

Sheet `PANDUAN` ditiadakan karena petunjuk dan contoh isian realistis telah disematkan langsung pada **Kolom D** di sheet `DATA`.

DATA memuat seluruh susunan tim di B4:B26 (PM di B4, PT di B5, KT di B6, dan Anggota Tim 1 s.d. 20 di B7:B26). Baris anggota yang tidak digunakan cukup dikosongkan. NIP di C4:C27 diketik manual sebagai teks 18 digit; hanya workbook `--with-pegawai` yang mengisinya otomatis via VLOOKUP dari sheet Pegawai. Isian golongan ditiadakan karena dokumen penugasan pengawasan BPKP tidak mensyaratkan golongan.

Isian tanpa output langsung (Lokasi penugasan, Kode unit, Path output SIMA-NG, serta rincian profil kop perwakilan) telah dibersihkan dari sheet DATA. Profil unit dan kop resmi otomatis menggunakan nilai baku dari `profil_unit.json`; ubah berkas itu (atau tambahkan baris DATA berkunci `UNIT_KERJA`, `KOP_BARIS1`, `KOP_BARIS2`, `ALAMAT_UNIT`, `WILAYAH_KODEPOS`, `EMAIL_UNIT`, `WEBSITE_UNIT`, `KOTA_UNIT` di kolom E) untuk unit selain Papua Tengah. Status checklist MPP otomatis ditetapkan `TERSEDIA` (atau `N/A` untuk penugasan PIA awal) saat dokumen dibuat.

## Kalender dan anggaran

Tanggal pengesahan awal sama tanggal konsep ST; RPL awal sama akhir ST. Awal persiapan 2 hari kerja setelah ST mengikuti pola workbook asal. Nilai awal ini dapat diganti. Sabtu/Minggu otomatis dikecualikan sebagai hari libur kerja; sheet LIBUR tidak lagi diperlukan.

Jam pengawasan per hari orang maksimal 6,5 jam (nilai bawaan `JAM_PER_HARI`). Generator menolak `JAM_PER_HARI` di atas 6,5 serta jam fase per orang di JAM_TIM yang melebihi hari fase × 6,5. JAM_TIM awal menganggarkan partisipasi penuh untuk setiap personel; sesuaikan PM/PT/anggota bila kontribusinya berbeda. Tidak ada rasio wajib KT=2×PM. KM 4 mengagregat peran/fase, KM 5 menghitung total orang masing-masing, dan jam KM 6 harus menjaga anggaran tiap orang.

NIP disimpan sebagai teks (diketik, atau dari sheet Pegawai saat nama dipilih via dropdown pada workbook `--with-pegawai`). Format NIP standar (dengan atau tanpa spasi) diverifikasi valid 18 digit angka. Tidak ada nama/NIP pejabat lama yang diprefill. Nomor resmi boleh kosong saat konsep; tidak diganti nomor fiktif.

## Alur agent

1. Baca workbook dan jalankan `generate_mpp.py <xlsx> --inspect`. Perintah menghitung ulang salinan sementara dan mengembalikan fakta, tim, Insilwas, hash input, serta total anggaran fase.
2. Baca sumber yang dirujuk. Susun rancangan analitis menurut `risiko-tao-teo-km6.md`: Insilwas → risiko klien → TAO/TEO → program kerja/KM 6 → task dan nama pelaksana. Dahulukan rumusan TAO/TEO pusat; usulan lokal diberi status tentatif.
3. Simpan JSON hasil kerja agent, lalu jalankan `generate_mpp.py <xlsx> --content <json> --check`. Periksa rantai hubungan, seluruh Insilwas/risiko/tujuan, serta nama dan anggaran pelaksana.
4. Jalankan tanpa `--check`, dengan `--output-root <folder>`. Generator mengisi OOXML dari DOCX asli dan mempertahankan kop. Word merender pratinjau sebelum hasil dipublikasikan ke folder nama penugasan.
5. Reviu visual, isi dan sumber dokumen; berikan tautan hasil kepada pengguna. Satu prompt pengguna mencakup seluruh langkah ini.

CLI `--check` tidak membuat folder penugasan. `--inspect` juga tidak menghasilkan paket. Kode keluar 2 berarti isian/rancangan belum lengkap; kode 1 berarti kesalahan eksekusi. Jangan menyamakan keduanya dengan hasil berhasil.

Default runtime memakai instance Excel/Word terpisah, tidak menutup aplikasi pengguna atau menyimpan input asli. Jika LibreOffice tidak tersedia di Windows, Office COM yang terpasang menjadi jalur hitung/render. Dependensi Python: openpyxl, lxml, PyMuPDF, pywin32. Tidak perlu npm untuk pemakaian skill. `--cached` hanya bila cache formula sudah baru dan diperiksa; `--no-pdf` hanya jika pratinjau memang tidak diperlukan/tidak dapat dibuat, dengan keterbatasannya dilaporkan.

ST PIA menghasilkan 11 dokumen. Pengawasan berikutnya menghasilkan 12, dengan laporan PIA FILE disalin utuh atau hasil manual yang benar-benar tersedia dirangkum pada bagian pia di rancangan. File PDF yang sudah disahkan tidak dikonversi menjadi konsep baru. Output SIMA-NG juga disalin utuh; agent tetap mencocokkan nama, personel, periode, dan alokasi dengan workbook.

Folder hasil memuat dokumen, manifest, rancangan analitis, ringkasan, dan pratinjau PDF. Pemanggilan ulang membuat subfolder versi di dalam folder penugasan, tanpa menimpa hasil lama. Nama asli dicatat dalam manifest; karakter folder yang tidak sah pada Windows dibersihkan. Nama yang melampaui batas komponen direktori disingkat dengan hash.
