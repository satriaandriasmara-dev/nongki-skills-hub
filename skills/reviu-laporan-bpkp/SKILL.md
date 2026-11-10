---
name: reviu-laporan-bpkp
description: Reviu menyeluruh atas draf laporan hasil pengawasan BPKP yang sudah ada (LHE, LHP, LHR, notisi, laporan evaluasi/audit/reviu dalam .docx) seperti yang dilakukan pengendali teknis. Skill ini mencocokkan angka dengan KKE, menguji kelengkapan 5C dan ketepatan kriteria, memetakan setiap temuan ke rekomendasi, memeriksa EYD V, tabel, penomoran, dan tata letak PDF. Hasilnya berupa daftar temuan reviu berkelompok, lalu perbaikan yang disetujui diterapkan sebagai versi draf baru. Gunakan setiap kali pengguna meminta "reviu", "reviu lagi", "reviu menyeluruh", "cek/periksa laporan", "QA draf", "apakah ada perubahan data KKE yang perlu disesuaikan", atau ingin laporan pengawasan dicek sebelum dikirim ke dalnis/daltu, walaupun tidak menyebut skill ini. Untuk menyusun laporan dari nol gunakan laporan-pengawasan-bpkp; skill ini untuk menguji dan merapikan draf yang sudah ada.
tags: [bpkp, reviu, quality-assurance, laporan-pengawasan, lhe, lhp, lhr, 5c, kke, eyd-v, docx, pdf]
---

# Reviu Laporan Pengawasan BPKP

Skill ini menempatkan Claude sebagai pereviu (pengendali teknis) atas draf laporan yang sudah jadi. Tujuannya menemukan semua hal yang akan dikoreksi atasan atau dipersoalkan auditi: angka yang tidak cocok dengan kertas kerja, temuan yang kriteria atau rekomendasinya bolong, klaim yang saling bertentangan, ejaan, tabel, dan tata letak. Hasilnya diserahkan dulu kepada pengguna sebagai daftar temuan reviu. File baru diubah setelah pengguna menyetujui.

## Prinsip

- **Baca laporan utuh, jangan hanya mengandalkan skrip.** Skrip menangkap kesalahan mekanis. Temuan reviu yang paling berharga muncul dari membaca seluruh teks dan memahami logikanya, misalnya kalimat yang subjeknya keliru, judul yang tidak sesuai isi, atau klaim yang bertentangan dengan hasil kas opname.
- **KKE adalah sumber kebenaran.** Setiap angka dihitung ulang dari KKE atau dari tabel di laporan itu sendiri. Bila KKE ada versi daring, pastikan yang dipakai versi terbaru.
- **Pisahkan yang bisa diputuskan dari dokumen dan yang butuh tim.** Redaksi, format, dan rekomendasi yang belum menampung temuan bisa langsung diusulkan. Fakta lapangan, data yang bertentangan antar-sheet, dan pertimbangan profesional dikembalikan ke tim.
- **Jangan menimpa draf.** Perbaikan disimpan sebagai versi baru, misalnya "(Draf v12)". Draf lama tetap utuh agar perubahan bisa dilacak.
- **Hormati teks yang tidak boleh diubah**: kutipan pasal (verbatim), nama resmi instansi, nama produk/aplikasi, nomor naskah, dan teks templat resmi kecuali jelas keliru.
- Tulis hasil reviu dalam bahasa Indonesia yang lugas, tanpa tanda pisah panjang (em dash).

## Alur kerja

### 0. Kenali bahan

Temukan draf terbaru, KKE sumber (.xlsx, termasuk tautan daring bila ada), templat, dan catatan reviu sebelumnya. Jika laporan dibangun oleh skrip (misalnya `build.py`), perbaikan nanti dilakukan di skrip itu, bukan langsung di .docx, agar tidak hilang saat dibangun ulang. Periksa juga apakah draf sedang terbuka di Word (ada berkas `~$...docx` di folder yang sama). Draf yang sedang terbuka tidak boleh ditimpa.

Jika pengguna bertanya apakah data KKE berubah, unduh salinan terbaru ke folder kerja baru. Untuk Excel Online, gunakan File > Create a Copy > Download a Copy. Lalu bandingkan dengan salinan yang dipakai laporan:

```bash
python scripts/banding_xlsx.py KKE_lama.xlsx KKE_baru.xlsx
```

Laporkan sel yang berubah dan bagian laporan yang terdampak. Jangan pernah menyimpan KKE dengan openpyxl, karena tautan eksternal, rentang edit, dan dropdown akan rusak. Bila KKE harus diubah, ubah melalui Excel.

### 1. Ekstrak teks dan render PDF

```bash
python scripts/dump_docx.py "Laporan (Draf vN).docx" > teks_vN.txt
powershell -ExecutionPolicy Bypass -File scripts/render_pdf.ps1 -Docx "Laporan (Draf vN).docx" -Pdf <folder-kerja>/draf_vN.pdf
```

Simpan hasil kerja di folder kerja (scratchpad), bukan di folder pengguna. Label `P012` (paragraf) dan `T05R02C03` (sel tabel) dipakai semua skrip, jadi lokasi temuan bisa dirujuk dengan konsisten.

### 2. Baca utuh

Baca `teks_vN.txt` dari awal sampai akhir, sekitar 200 baris per bagian. Sambil membaca, catat angka, istilah, klaim, dan rujukan peraturan per bagian. Pakai `references/daftar-periksa.md` bagian 2 sampai 4 sebagai pemandu. Reviu yang hanya melihat potongan teks hampir selalu melewatkan kontradiksi antarbagian.

### 3. Cek mekanis otomatis

```bash
python scripts/cek_mekanis.py "Laporan (Draf vN).docx" [--izinkan APIP,SKPD]
```

Skrip ini memeriksa: akronim yang belum dieja pada kemunculan pertama, tanda baca dan spasi, format angka dan Rp, kata tidak baku, koma serial, huruf kapital jabatan dan judul, pola tanda baca daftar bernomor, penomoran yang diketik manual, istilah asing yang belum miring, placeholder dan teks merah, kalimat lebih dari 50 kata, serta informasi yang diulang di dua tempat. Hasilnya berupa daftar kandidat, jadi triase setiap butir. Positif palsu yang lazim: judul, kutipan pasal, nama produk ("Siskeudes Online"), nomor naskah di kop, dan pola kalimat per desa yang memang disengaja.

### 4. Cocokkan angka dan istilah dengan KKE

- Hitung ulang total, selisih, persentase, dan rata-rata di setiap tabel dan paragraf. Perhatikan pembaginya, misalnya rata-rata atas desa penerima atau atas semua desa.
- Cocokkan angka kunci dengan sel KKE. Baca KKE dengan `openpyxl.load_workbook(..., read_only=True, data_only=True)`.
- Pakai istilah KKE/juknis. Contoh: bila KKE memakai "Tingkat Dampak", laporan jangan menulis "urgensi".
- Bandingkan tanggal data dengan *cut off* evaluasi. Misalnya realisasi per 10 Oktober, padahal *cut off* 3 November.

### 5. Uji 5C dan petakan rekomendasi

Susun matriks kerja (cukup untuk diri sendiri) berisi temuan, kondisi, kriteria (pasal), sebab, akibat, dan rekomendasi. Lalu cari yang bolong:

- Ketidaksesuaian yang tidak punya kriteria berpasal.
- Kriteria yang tidak relevan dengan kondisi.
- Sebab yang hanya mengulang kondisi.
- Akibat yang tidak menyebut nilai.
- Temuan bersebab yang belum punya rekomendasi.
- Rekomendasi yang tidak selaras dengan kriteria. Contoh: kriteria mewajibkan penyetoran, tetapi rekomendasi hanya meminta "mencatat".

Rinciannya ada di `references/daftar-periksa.md` bagian 2 dan 4.

### 6. Cek tata letak

```bash
python scripts/cek_tata_letak.py <folder-kerja>/draf_vN.pdf
python scripts/cek_tata_letak.py <folder-kerja>/draf_vN.pdf --cari "Kas Seharusnya" --halaman 9,14 --keluar <folder-kerja>/cek.png
```

Skrip mendeteksi judul atau pengantar yang tertinggal di bawah halaman, sumber yang terpisah dari tabelnya, ruang kosong besar, label nomor yang tidak seragam, dan kata terpotong di kolom tabel yang sempit (misal "Pake/t", "Pemeliharaa/n"). Lihat gambar PNG-nya untuk tabel yang mencurigakan. Tampilan PDF adalah yang dibaca auditi.

### 7. Sajikan hasil reviu

Jangan mengubah file pada tahap ini. Sajikan hasil reviu dengan susunan berikut:

```markdown
Saya sudah mereviu <nama draf> dari awal sampai akhir. <Satu kalimat: kondisi umum dan berapa perbaikan.>

**Yang sudah dicek dan aman**
- <angka/bagian yang sudah dicocokkan, singkat>

**A. Bisa langsung diperbaiki**
1. **<Lokasi atau topik (hal. PDF)>:** <masalah>. Usul: "<teks pengganti>".

**B. Rekomendasi yang belum menampung temuan**
2. **<Temuan>:** <yang belum tertampung>. Usul: <butir/sub-butir rekomendasi>.

**C. Perlu konfirmasi tim**
- **<Topik>:** <apa yang bertentangan atau kurang, dan apa yang perlu dipastikan>.

**Masih menunggu tim (dari reviu sebelumnya)**
- <item lama yang belum selesai>
```

Nomori butir A dan B secara berurutan agar pengguna bisa menjawab "terapkan nomor 1 sampai 8". Setiap butir menyebut lokasi, masalah, dan usulan teks yang konkret. Tutup dengan satu pertanyaan, misalnya "Terapkan N perbaikan yang tidak butuh konfirmasi tim?"

### 8. Terapkan perbaikan yang disetujui

1. Ubah sumbernya, yaitu skrip pembangun bila ada. Bila tidak ada, edit .docx dengan menjaga format run dan numbering (lihat skill `docx`).
2. Simpan sebagai versi baru di folder yang sama dengan draf, misalnya "Laporan ... (Draf vN+1).docx" beserta PDF-nya. Pastikan tidak ada berkas kunci `~$`.
3. Verifikasi:
   - validasi struktur .docx (skrip `validate.py` dari skill `docx`, bila tersedia);
   - jalankan ulang `cek_mekanis.py`;
   - render PDF lalu jalankan `cek_tata_letak.py`, dan lihat gambar bagian yang diubah;
   - jalankan `banding_docx.py` versi lama dan baru untuk memastikan hanya perubahan yang disetujui yang masuk.
4. Laporkan apa saja yang berubah per butir, hasil verifikasi, dan item yang masih menunggu tim.

## Konvensi penulisan yang dipakai

Konvensi ini lahir dari reviu nyata dan disepakati pengguna. Terapkan juga saat mengusulkan teks pengganti.

- **Rincian di dalam kalimat dijadikan daftar bernomor Word asli**, bukan nomor yang diketik. Rincian kondisi memakai 1), sedangkan butir kriteria dan sub-butir rekomendasi memakai a) atau 1) di bawah huruf. Rekomendasi yang memuat banyak tindakan dipecah menjadi sub-butir.
- **Label nomor seragam dengan teks isi**: font dan ukuran sama, tegak, dan hitam. Tanda paragraf di templat sering berformat merah atau miring sehingga labelnya ikut. Atur format label secara eksplisit.
- **Tanda baca daftar (EYD V)**:
  - Butir berupa frasa lanjutan kalimat pengantar diawali huruf kecil dan diakhiri ";". Butir kedua terakhir diakhiri "; dan", butir terakhir diakhiri titik.
  - Butir berupa kalimat lengkap diawali huruf kapital dan diakhiri titik.
  - Butir terakhir sub-daftar mengikuti akhiran induknya: ";", "; dan", atau ".".
- **Pola paragraf temuan**:
  - kriteria: "Kondisi tersebut tidak sesuai dengan <peraturan> sebagai berikut:" diikuti daftar pasal;
  - sebab: "Ketidaksesuaian tersebut disebabkan ...";
  - akibat: "Akibatnya, ...".
- **Rujukan peraturan yang telah diubah ditulis seragam**, misalnya "Permendagri Nomor 1 Tahun 2016 sebagaimana telah diubah dengan Permendagri Nomor 3 Tahun 2024".
- **Akronim dieja lengkap pada kemunculan pertama di badan teks.** Judul tidak dihitung. Setelah itu akronim dipakai secara konsisten.
- **Istilah mengikuti cakupannya.** Contoh: KDKMP untuk desa dan kelurahan, KDMP bila hanya tingkat desa.

## Skrip

| Skrip | Fungsi |
|---|---|
| `scripts/dump_docx.py` | Teks utuh berlabel (paragraf, numbering, tabel, teks merah, gambar) |
| `scripts/cek_mekanis.py` | Kandidat kesalahan mekanis dan bahasa |
| `scripts/render_pdf.ps1` | Render .docx ke PDF lewat Word (read-only) |
| `scripts/cek_tata_letak.py` | Masalah tata letak PDF dan gambar halaman |
| `scripts/banding_xlsx.py` | Perubahan sel antara dua versi KKE |
| `scripts/banding_docx.py` | Perubahan teks antara dua versi laporan |

Semua skrip memerlukan python-docx, PyMuPDF, Pillow, dan openpyxl (`pip install python-docx pymupdf pillow openpyxl`). Jalankan skrip dengan path lengkapnya dari folder skill ini.

## Rujukan

- `references/daftar-periksa.md`: daftar periksa lengkap per lapisan, beserta contoh temuan nyata. Baca saat langkah 2 sampai 6.
- Skill terkait:
  - `eyd-indonesia`: kasus ejaan yang meragukan;
  - `laporan-pengawasan-bpkp`: struktur laporan dan kerangka 5C;
  - `tata-naskah-dinas-bpkp`: kop, nomor, tembusan, dan penandatangan;
  - `audit-legal-crawler`: verifikasi bunyi pasal;
  - `docx`: mengedit file Word dengan aman.
