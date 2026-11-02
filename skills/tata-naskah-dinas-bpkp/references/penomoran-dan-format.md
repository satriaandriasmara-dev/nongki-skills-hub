# Penomoran dan Format Naskah Dinas BPKP

Referensi format penomoran, kode jenis naskah, kop, kertas, spasi, margin, dan tabel sesuai **BAB II Pembuatan Naskah Dinas** Peraturan BPKP Nomor 4 Tahun 2026 (menggantikan Lampiran BAB III Perban 4/2022).

---

## 1. Format Penomoran Naskah Dinas

Nomor naskah dinas adalah segmen penting kearsipan; susunannya harus memudahkan penyimpanan, penemuan kembali, dan penilaian arsip. Setiap unit kerja wajib menggunakan penomoran sesuai ketentuan.

Peraturan 4/2026 membagi penomoran menjadi **dua format**:

### Format 1: Tanpa Kode Jenis (Naskah Dinas Arahan Pengaturan)
Digunakan untuk Peraturan, Instruksi, dan Surat Edaran. Hanya menyebutkan nomor dan tahun penetapan, tanpa kode jenis, penanda tangan, dan unit kerja konseptor.
```
(Nama Jenis Naskah Dinas)
(Nama Jabatan)
NOMOR xxx TAHUN xxxx
TENTANG
(Judul Hal yang Diatur)
```

### Format 2: Dengan Kode Jenis (Umum)
Untuk naskah dinas selain Peraturan/Instruksi/Surat Edaran:
```
[kode klasifikasi arsip] / [kode klasifikasi keamanan] / [kode jenis] - [nomor urut] / [kode unit penanda tangan] / [kode konseptor] / [tahun]
```
Kode klasifikasi keamanan diletakkan **setelah** kode klasifikasi arsip (Peraturan 4/2026 Bagian II.B.b). Untuk surat dinas berkategori **Biasa**, segmen tersebut **dikosongkan** -- tidak diisi kode apa pun. Contoh: `OT.01 / / S-20 / PW20/2 / 2026`.

Contoh resmi penomoran (Peraturan 4/2026 Bagian II.B.2):
```
OT.00/KEP-23/K/SU/2026          # Kepala, konsep Sekretaris Utama
OT.00/KEP-32/SU/01/2026         # Sekretaris Utama, konsep Biro MKKOTL
OT.00/S-123/SU01/3/2026         # Kepala Biro MKKOTL, konsep Koordinator Org & Tata Laksana
OT.00/NOTULA-35/SU01.3/2026     # Koordinator Org & Tata Laksana (tanpa kode konseptor)
PL.02.01/PRJ-123/SU05.3/2026    # PPK Bagian Rumah Tangga
PL.02.01/PRJ-123/PW10.1/2026    # PPK pada Perwakilan BPKP Provinsi Jawa Barat
```

Contoh penomoran naskah pengawasan (kode klasifikasi arsip dan kode konseptor berasal dari unit kerja masing-masing; **tidak ditetapkan oleh peraturan**):
```
PE.09.02/ST-314/PW34/2/2026
PE.09.03/LHP-314/PW34/2/2026
```

> [!warning] Verifikasi kode unit
> Kode unit (mis. `PW34` untuk Kantor Perwakilan BPKP Provinsi Papua Tengah) ditetapkan melalui petunjuk teknis terpisah oleh Kepala. **Selalu verifikasi kode unit ke `assets/unit_profiles.json`**, jangan menyalin dari contoh di dokumen -- contoh pada skill ini bisa tidak sinkron dengan daftar resmi.

### Kode Klasifikasi Keamanan (Khusus Surat Dinas)
- `SR` : Sangat Rahasia
- `R`  : Rahasia
- `T`  : Terbatas
- **Biasa**: **tanpa kode** pada nomor naskah. Tulis "Biasa" pada baris sifat surat.

Penentuan kategori klasifikasi keamanan mengacu pada ketentuan kearsipan yang berlaku di lingkungan BPKP.

### Pengecualian Penomoran
- **Tanpa kode jenis**: Peraturan, Instruksi, Surat Edaran (Format 1).
- **Tidak dibubuhi penomoran sama sekali**: Disposisi, Dokumentasi Pengawasan, Pedoman, Panduan Teknis Pengawasan, Petunjuk Pelaksanaan/Teknis, Telaah Staf, Kerangka Acuan Kerja, dan Formulir. Tata cara penomorannya tidak mengikuti format di Peraturan Badan ini; mengikuti kebijakan unit kerja.

### Aturan Nomor Urut
Nomor urut adalah nomor agenda elektronik unit kerja dalam 1 (satu) tahun takwim/kalender, menggunakan angka arab berurutan. Setiap awal tahun, per kelompok buku agenda elektronik, dimulai dari nomor urut 1. Pengelompokan per jenis Naskah Dinas (tidak digabung). **DILARANG** menambahkan kode, huruf, angka romawi, atau penanda lain yang mengubah format.

### Kode Konseptor
Kode unit/jabatan/konseptor menunjukkan siapa pejabat yang menandatangani Naskah Dinas dan unit kerja konseptor asal. Dipisahkan dengan garis miring (`/`) antara kode penanda tangan dan konseptor. Pencantuman kode konseptor hanya sampai satu tingkat di bawah pejabat penanda tangan. Daftar kode ditetapkan oleh Kepala (melalui petunjuk teknis terpisah).

### Kode Perwakilan & Akronim Unit Kerja
Peraturan 4/2026 menambahkan penggunaan **kode konseptor, kode perwakilan, dan akronim unit kerja** di lingkungan BPKP. Petunjuk teknisnya ditetapkan oleh Kepala.

---

## 2. Kode Jenis Naskah Dinas (Peraturan BPKP 4/2026)

### a. Naskah Dinas Arahan
| Naskah | Kode |
|---|---|
| Peraturan | Tanpa kode (Format 1) |
| Instruksi | Tanpa kode (Format 1) |
| Surat Edaran | Tanpa kode (Format 1) |
| Standar Operasional Prosedur (SOP) | Tanpa kode |
| Keputusan | `KEP` |
| Surat Perintah | `SPRIN` |
| Surat Tugas | `ST` |

### b. Naskah Dinas Korespondensi
| Naskah | Kode |
|---|---|
| Nota Dinas | `ND` |
| Memorandum | `MO` |
| Disposisi | Tanpa kode, tanpa nomor |
| Undangan Internal | `UND` |
| Surat Dinas | `S` |

### c. Naskah Dinas Khusus
| Naskah | Kode |
|---|---|
| Dokumentasi Pengawasan | Tanpa kode, tanpa nomor |
| Pedoman | Tanpa kode, tanpa nomor |
| Panduan Teknis Pengawasan | Tanpa kode, tanpa nomor |
| Petunjuk Pelaksanaan/Teknis | Tanpa kode |
| Laporan Hasil Pengawasan | `LHP` |
| Laporan Penunjang Pengawasan | `LPP` |
| Nota Kesepahaman/MoU | `MoU` |
| Surat Perjanjian | `PRJ` |
| Berita Acara | `BA` |
| Surat Kuasa | `KS` |
| Surat Keterangan | `KET` |
| Surat Pengantar Naskah/Barang | `SP` |
| Pengumuman | `PENG` |
| Surat Peringatan | `PRT` |
| Surat Pernyataan | `SPT` |
| Notula/Risalah | `NOTULA` |
| Telaah Staf | Tanpa kode, tanpa nomor |
| Sertifikat | `SERT` |
| Piagam Penghargaan | `PI` |
| Kerangka Acuan Kerja | Tanpa kode, tanpa nomor |
| Formulir | Tanpa kode, tanpa nomor |

> [!note] Perubahan Kode Jenis (Perban 4/2022 → Peraturan 4/2026)
> - **Dihapus**: `SPD` (Surat Perjalanan Dinas -- kini peraturan terpisah), `SPPL` (Surat Pengukuhan Perintah Lisan), `BAPS` (BA Pengangkatan Sumpah), `NST` (Naskah Serah Terima Jabatan), `SI` (Surat Izin), `SPMT`/`SPMJ`/`SPL` (diganti `SPT`).
> - **Kode berubah**: Surat Kuasa dari tanpa kode → `KS`; Surat Pernyataan dari gabungan `SPMT`/`SPMJ`/`SPL` → `SPT`; Memorandum kini eksplisit `MO`.
> - **Kode baru**: `NOTULA`, `SERT`, `PI`.

---

## 3. Buku Agenda & Penomoran Awal Tahun

Pencatatan naskah dalam buku agenda elektronik dikelompokkan per jenis Naskah Dinas (tidak digabung beberapa jenis). Setiap awal tahun kalender, penomoran pada seluruh buku agenda dimulai kembali dari nomor urut 1.

---

## 4. Kop Naskah Dinas Resmi (Unit Pusat & Perwakilan)

Peraturan 4/2026 BAB II.A membedakan **dua varian kop**. Jangan menerapkan satu varian untuk semua naskah.

### 4.1 Kop Jabatan (Logo tanpa Alamat)
Kop jabatan menunjukkan nama jabatan Kepala/wakil kepala dan **hanya dipakai untuk naskah yang ditandatangani Kepala/wakil kepala atas nama Kepala**.
- **Logo BPKP berwarna** diletakkan **di atas, simetris**, ukuran **panjang 34 mm x tinggi 17 mm** (rasio 2:1), paling kurang 10 mm dari tepi atas kertas.
- `BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN` -- **Arial 13 pt Bold**, seluruhnya huruf kapital, diletakkan simetris di bawah logo.
- Nama unit kerja -- **Arial 12 pt Bold**, seluruhnya huruf kapital, di bawah nama lembaga.

### 4.2 Kop dengan Logo dan Alamat
Dipakai untuk **Naskah Dinas arahan bersifat penugasan, Naskah Dinas korespondensi, dan Naskah Dinas khusus**.
- **Logo BPKP** di **bagian atas sebelah kiri**, simetris, paling kurang 10 mm dari tepi atas kertas. Ukuran **panjang 32 mm x tinggi 16 mm** (rasio 2:1).
- `BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN` -- **Arial 12 pt Bold**, kapital, diletakkan **samping kanan logo**.
- Nama unit kerja -- **Arial 12 pt Bold**, kapital, di bawah nama lembaga.
- Alamat lengkap, telepon, faksimile, email, dan website (bila diperlukan) -- **Arial 9 sampai 11 pt**, kapital di setiap awal kata, di bawah nama unit kerja.
- **Garis penutup:** garis tebal tunggal ketebalan **2,25 pt**, mulai dari batas margin kiri **30 mm** sampai batas margin kanan **20 mm**.

---

## 5. Standar Format Dokumen Microsoft Word (`docx`)

### A. Ukuran Kertas & Ruang Tepi (Margin)
- **Kertas:** A4 (21,0 cm x 29,7 cm)
- **Ruang tepi bersifat fleksibel** dan paling kurang (Peraturan 4/2026 Bagian II.E):

  | Tepi | Nilai |
  |---|---|
  | Atas | 10 mm bila memakai kop Naskah Dinas; **paling kurang 20 mm** tanpa kop atau pada halaman berikutnya |
  | Bawah | **paling kurang 25 mm** |
  | Kiri | **paling kurang 30 mm** (media rekam kertas); **paling kurang 20 mm** (media rekam elektronik) |
  | Kanan | **paling kurang 20 mm** |

  Penentuan akhir menyesuaikan kondisi isi naskah dengan memperhatikan keserasian dan estetika.

### B. Tipografi & Spasi
- **Jenis huruf:** **Arial ukuran 11 atau 12 pt**. Untuk naskah berupa **produk hukum** (peraturan, instruksi, surat edaran, keputusan): **Bookman Old Style ukuran 12 pt**.
- **Jarak spasi:** tidak ditetapkan angka baku oleh peraturan. Jarak antara kop surat dengan kepala Naskah Dinas: line spacing 1 dengan 2 kali enter; jarak antara bab dan judul: line spacing 1 dengan 2 kali enter; jarak antara judul dan subjudul: line spacing 1 dengan 3 enter; jarak antara subjudul dan uraian: line spacing 1 dengan 2 kali enter; jarak masing-masing baris disesuaikan dengan keperluan.
- **Preset teknis proyek** (umum dipakai, bukan angka wajib peraturan): line spacing 1.15 (`w:line="276"`), Space After 6 pt (`w:after="120"`), Space Before 0 pt (sub-heading 8 pt).
- **Perataan:** 100% **Justified (Rata Kiri-Kanan)**.
- **Kata penyambung:** hanya pada Naskah Dinas peraturan dengan media rekam kertas, ditulis di sudut kanan bawah halaman dengan urutan kata penyambung + tiga titik. **Tidak dicantumkan** pada media rekam elektronik.

### C. Hierarki Indentasi & Tab Stops (Anti-Bocor / Hanging Indent)
- **Level 1 (Topik/Bab):** Left `0.00"`, First Line `0.00"`, Bold 12 pt.
- **Level 2 (Sub-Heading `a.`, `b.`):** Left `0.75"` (1080 dxa), First Line `-0.25"` (-360 dxa), Tab Stop di `1440 dxa` (`1.00"`), Bold 12 pt.
- **Level 2 Body (Narasi Pengantar):** Left `1.00"` (1440 dxa), First Line `0.00"`, Regular 12 pt, Justified.
- **Level 3 (Rincian Lokus `1)`, `2)`):** Left `1.25"` (1800 dxa), First Line `-0.25"` (-360 dxa), Tab Stop di `1800 dxa` (`1.25"`), Justified, Nama Lokus Regular.
- **Level 4 (Detail Item `a)`, `b)`):** Left `1.50"` (2160 dxa), First Line `-0.25"` (-360 dxa), Tab Stop di `2160 dxa` (`1.50"`), Justified.

### D. Format Tabel BPKP (Clean Open-Table Style)
- Garis border **hanya horizontal** (Top, Bottom, dan pemisah Header sz="4" abu-abu/hitam). **Tanpa border vertikal**.
- Header shading abu-abu lembut (`#F2F2F2`), teks bold rata tengah/kiri, *vertically centered*.
- Padding sel: Atas/Bawah 100 dxa (~5 pt), Kiri/Kanan 150 dxa (~7.5 pt).
- Angka rata kanan, teks uraian rata kiri/justified, nomor rata tengah. Keterangan sumber dicantumkan di bawah tabel (*Arial 9 pt Italic*).

### E. Format Khusus Google Workspace / Google Docs (GWS)
- **Tabel Metadata Surat Pengantar:** Wajib menggunakan format **4 Kolom** (Kolom 1: Label `69 pt`, Kolom 2: `:` `18 pt`, Kolom 3: Konten/Judul `237.75 pt`, Kolom 4: Tanggal Kanan `129.75 pt`) untuk mencegah *hanging indent* pada *line wrapping* judul `Hal`.
- **Indeks Kolom Tabel:** Setiap paragraf di dalam sel tabel wajib dideklarasikan `<w:ind w:left="0" w:right="0" w:firstLine="0"/>` (`indentStart: 0, indentFirstLine: 0`) agar *marker ruler* Google Docs tidak bergeser ke tengah.
- **Narasi Sub-Heading Level 1 (`HEADING_3`):** Paragraf narasi diset dengan `indentStart: 54 pt` (0.75" / 1080 dxa) dan `indentFirstLine: 54 pt` agar sejajar 100% dengan huruf pertama judul sub-heading.

### F. Resep Lengkap Numbering Multi-Level untuk Google Docs (XML)

Untuk daftar bertingkat `A. → 1. → a.` yang merender benar di Google Docs, bangun `word/numbering.xml` dengan definisi `abstractNum` berikut (terverifikasi):

```xml
<abstractNum abstractNumId="1">
  <lvl ilvl="0"> <numFmt w:val="upperLetter"/> <lvlText w:val="%1."/> <lvlJc w:val="left"/> <pPr><ind w:left="720"  w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="1"> <numFmt w:val="decimal"/>     <lvlRestart w:val="1"/> <lvlText w:val="%2."/> <lvlJc w:val="left"/> <pPr><ind w:left="1080" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="2"> <numFmt w:val="lowerLetter"/> <lvlRestart w:val="2"/> <lvlText w:val="%3."/> <lvlJc w:val="left"/> <pPr><ind w:left="1440" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="3"> <numFmt w:val="decimal"/>     <lvlRestart w:val="3"/> <lvlText w:val="%4)"/> <lvlJc w:val="left"/> <pPr><ind w:left="1800" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="4"> <numFmt w:val="lowerLetter"/> <lvlRestart w:val="4"/> <lvlText w:val="%5)"/> <lvlJc w:val="left"/> <pPr><ind w:left="2160" w:hanging="360"/></pPr> </lvl>
</abstractNum>
<num numId="1"><abstractNumId w:val="1"/></num>
```

Pemakaian pada paragraf: `<w:numPr><w:ilvl w:val="N"/><w:numId w:val="1"/></w:numPr>` dengan `w:ind` identik nilai `left` dan `hanging` pada level terkait.

**Teknik tercekat (metode salin-referensi):** membangun `numbering.xml`/`styles.xml` dari nol berulang kali gagal render di Google Docs. Metode yang selalu berhasil: **salin docx referensi berformat benar → kosongkan seluruh paragraf dan tabelnya (`p._p.getparent().remove(p._p)`) → tulis ulang konten**. Numbering, styles, dan section properties terwarisi utuh.

**Peringatan nilai piksel vs dxa:** jangan gunakan konversi piksel (708/1068/1428). Nilai baku wajib kelipatan grid 360 dxa: `720/1080/1440`. Selisih 12 dxa tidak kasat mata tetapi membuat *marker ruler* Google Docs tidak jatuh pada grid 0,5"/0,75"/1,0".

**Penyelarasan tabel dengan teks:** agar garis tepi kiri tabel rata sejajar teks narasi di atasnya (bukan menonjol keluar), setel `w:tblPr` dengan `<w:jc w:val="left"/>`, `<w:tblInd w:w="720" w:type="dxa"/>` (identik `w:ind w:left` paragraf), dan `<w:tblW w:w="8318" w:type="dxa"/>` (lebar efektif = lebar halaman minus kedua margin minus indent). Isi `w:tcW` tiap sel dengan jumlah yang sama persis.

