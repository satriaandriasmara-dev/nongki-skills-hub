---
name: tata-naskah-dinas-bpkp
description: Menyusun, mengedit, dan memvalidasi naskah dinas resmi di lingkungan BPKP (surat dinas, nota dinas, surat tugas, keputusan, berita acara, MoU, laporan, dll) sesuai Peraturan BPKP Nomor 4 Tahun 2026 tentang Tata Naskah Dinas (menggantikan Perban 4/2022). Gunakan saat diminta membuat draf naskah/surat dinas, menentukan jenis naskah yang tepat, menyusun penomoran arsip, memilih pejabat penanda tangan, atau mengklasifikasikan derajat kerahasiaan naskah.
tags: [bpkp, tata-naskah-dinas, tnd, naskah-dinas, surat-dinas, nota-dinas, surat-tugas, peraturan-bpkp-4-2026, penomoran, penanda-tangan]
---

# Tata Naskah Dinas BPKP

Skill ini membantu menyusun naskah dinas resmi di lingkungan BPKP sesuai **Peraturan BPKP Nomor 4 Tahun 2026 tentang Tata Naskah Dinas di Lingkungan BPKP** (menggantikan Peraturan BPKP Nomor 4 Tahun 2022 sebagaimana diatur dalam Pasal 12 Pencabutan), baik untuk unit pusat maupun perwakilan.

> [!important] Perubahan Struktural Utama (Perban 4/2022 → Peraturan 4/2026)
> - **Judul**: "Pedoman Tata Naskah Dinas" → "Tata Naskah Dinas" (tanpa kata "Pedoman").
> - **Struktur**: Lampiran I–VII (Perban 4/2022) → **BAB I–VI** (Peraturan 4/2026).
> - **Pendahuluan** (Lampiran I) → **BAB I** (ditambah sub-bagian C. Sasaran dan D. Prinsip).
> - **Penciptaan Naskah Dinas** (Lampiran III) → **BAB II: Pembuatan Naskah Dinas** (jeda spasi, margin, TTD/paraf/cap, kaidah penulisan, estetika & etika, rujukan, perubahan/ralat tergabung).
> - **Penanda Tangan & TTE** (Lampiran IV) → **BAB III: Pejabat Penanda Tangan** (ditambah Tabel III.2 Matriks ke Instansi Luar BPKP).
> - **Pengamanan & Pengendalian** (Lampiran V) → **BAB IV**.
> - **Jenis, Susunan, Bentuk** (Lampiran II tersebar) → **BAB V** utuh dengan sub-bagian A (Arahan), B (Korespondensi), C (Khusus, 20 jenis).
> - **Perubahan/Ralat/Penutup** (Lampiran VI–VII) → terintegrasi pada BAB II-M dan **BAB VI Penutup**.

Baca file referensi sesuai kebutuhan:
- [Katalog Master Template](references/templates_registry.json) -- katalog 46 template naskah dinas resmi Word (.docx) beserta daftar placeholder.
- [Profil Unit Kerja & Kop](assets/unit_profiles.json) -- konfigurasi identitas kop surat resmi perwakilan (Papua Tengah, Kalsel, Papua, Jatim, DKI, dll).
- [Jenis Naskah Dinas](references/jenis-naskah-dinas.md) -- taksonomi lengkap, definisi, dan sistematika tiap jenis.
- [Penomoran dan Format](references/penomoran-dan-format.md) -- format nomor, kode jenis naskah, kop, kertas, spasi, margin.
- [Matriks Penanda Tangan](references/matriks-penanda-tangan.md) -- wewenang penandatanganan per jenis naskah, pelimpahan wewenang (a.n., u.b., Plt., Plh.), TTE.
- [Pengamanan dan Perubahan](references/pengamanan-dan-perubahan.md) -- klasifikasi keamanan, enkripsi, tata cara perubahan/pencabutan/pembatalan/ralat.

## 1. Taksonomi Jenis Naskah Dinas

Naskah dinas BPKP terbagi menjadi tiga kelompok besar:

```
Naskah Dinas
├── Arahan
│   ├── Pengaturan : peraturan, instruksi, surat edaran, prosedur baku
│   │                pelaksanaan kegiatan (SOP)
│   ├── Penetapan  : keputusan
│   └── Penugasan  : surat perintah, surat tugas
├── Korespondensi
│   ├── Internal   : nota dinas, memorandum, disposisi, undangan internal
│   └── Eksternal  : surat dinas
└── Khusus (20 jenis): dokumentasi pengawasan, pedoman, panduan teknis
    pengawasan, petunjuk pelaksanaan/teknis, laporan, MoU, surat perjanjian,
    berita acara, surat kuasa, surat keterangan, surat pengantar naskah/barang,
    pengumuman, surat peringatan, surat pernyataan, notula/risalah, telaah staf,
    sertifikat, piagam penghargaan, kerangka acuan kerja, formulir
```

> [!note] Perubahan Komposisi Naskah Dinas Khusus (Perban 4/2022 → Peraturan 4/2026)
> - **Pedoman, Petunjuk Pelaksanaan/Teknis** dipindahkan dari Naskah Dinas Arahan → Naskah Dinas Khusus.
> - **Panduan Teknis Pengawasan** (baru), **Telaah Staf**, **Sertifikat**, **Piagam Penghargaan**, **Kerangka Acuan Kerja (KAK)** kini dikategorikan secara eksplisit sebagai Naskah Dinas Khusus.
> - **Naskah Dinas Dokumentasi Pengawasan** (kategori baru) menggabungkan: Surat Permintaan Data, Notisi, Rencana Tindak Perbaikan (RTP), Pernyataan Kesanggupan Tindak Lanjut, BA Pembahasan Hasil Pengawasan, BATL, BA Pemutakhiran Data, BA TPTD, dan SPTJM.
> - **Dihapus sebagai jenis mandiri**: Surat Izin (`SI`), Surat Pernyataan Melaksanakan Tugas (`SPMT`), Surat Pernyataan Menduduki Jabatan (`SPMJ`), Surat Pernyataan Pelantikan (`SPL`), Surat Pengukuhan Perintah Lisan (`SPPL`), Surat Perjalanan Dinas (`SPD` -- tunduk peraturan terpisah), BA Pengangkatan Sumpah (`BAPS`), Naskah Serah Terima Jabatan (`NST`).

### Panduan memilih jenis naskah

| Situasi | Jenis naskah |
|---|---|
| Membuat kebijakan pokok yang mengikat umum | Peraturan |
| Acuan bersifat umum (bentuk: Peraturan) | Pedoman |
| Cara/teknis pelaksanaan kegiatan | Petunjuk pelaksanaan/teknis |
| Perintah pelaksanaan kebijakan UU/peraturan | Instruksi |
| Pemberitahuan hal penting dan mendesak | Surat Edaran |
| Menetapkan status/kedudukan/tindak lanjut (tidak mengatur) | Keputusan |
| Memerintahkan bawahan mengerjakan pekerjaan tertentu | Surat Perintah |
| Menugaskan pegawai melaksanakan kerja sesuai tugas/fungsi | Surat Tugas |
| Komunikasi resmi internal antar unit/pejabat dalam BPKP | Nota Dinas |
| Menyampaikan informasi kedinasan ke instansi lain | Surat Dinas |
| Mengundang peserta rapat/acara | Surat Undangan |
| Dokumentasi hasil pembahasan/kesepakatan dengan auditan | Berita Acara |
| Kerja sama antarinstansi | MoU / Perjanjian Kerja Sama |

Rincian definisi, dasar pasal, dan sistematika tiap jenis ada di [Jenis Naskah Dinas](references/jenis-naskah-dinas.md).

## 2. Format Penomoran Naskah Dinas

Peraturan 4/2026 membagi penomoran menjadi **dua format**:

**Format 1 -- Tanpa kode jenis** (untuk Naskah Dinas arahan bersifat pengaturan: Peraturan, Instruksi, Surat Edaran). Hanya menyebutkan nomor dan tahun penetapan, tanpa kode jenis, penanda tangan, dan unit kerja konseptor.
```
(Nama Jenis Naskah Dinas)
(Nama Jabatan)
NOMOR xxx TAHUN xxxx
TENTANG
(Judul Hal yang Diatur)
```

**Format 2 -- Dengan kode jenis** (untuk naskah dinas selain di atas):
```
[kode keamanan] / [kode klasifikasi arsip] / [kode jenis] - [nomor urut] / [kode unit penanda tangan] / [kode konseptor] / [tahun]
```

Kode keamanan hanya untuk surat dinas: `SR` (Sangat Rahasia), `R` (Rahasia), `T` (Terbatas), `S` (Biasa, tanpa kode). Kode jenis utama (Peraturan 4/2026): `KEP`, `SPRIN`, `ST`, `ND`, `MO`, `UND`, `S`, `LHP`, `LPP`, `MoU`, `PRJ`, `BA`, `KS`, `KET`, `SP`, `PENG`, `PRT`, `SPT`, `NOTULA`, `SERT`, `PI`.

**Naskah Dinas tanpa penomoran** (tidak dibubuhi nomor; mengikuti kebijakan unit kerja): disposisi, dokumentasi pengawasan, pedoman, panduan teknis pengawasan, petunjuk pelaksanaan/teknis, telaah staf, kerangka acuan kerja, dan formulir.

Nomor urut agenda elektronik dimulai dari 1 setiap awal tahun, dikelompokkan per jenis naskah, dan **tidak diperkenankan ditambahkan kode, huruf, angka romawi, maupun penanda lainnya** yang mengubah format penomoran. Detail elemen, daftar kode lengkap, serta ketentuan kop/kertas/spasi/margin ada di [Penomoran dan Format](references/penomoran-dan-format.md).

## 3. Wewenang Penanda Tangan

Aturan kunci (Peraturan 4/2026, BAB III):
- Naskah bersifat **kebijakan/keputusan/arahan** kepada pihak luar BPKP: ditandatangani **Kepala BPKP**, dapat didelegasikan/dilimpahkan ke **JPT Madya**.
- **Peraturan/Instruksi**: hanya Kepala BPKP.
- **Surat Edaran/Keputusan**: Kepala BPKP, JPT Madya, atau JPT Pratama.
- **SOP**: hanya JPT Pratama.
- **Nota dinas/disposisi/memorandum/undangan internal/surat dinas**: semua jenjang sampai administrator/koordinator/pengawas.
- **MoU/Perjanjian Kerja Sama luar negeri**: Kepala BPKP atau JPT Madya (tidak lagi hanya Kepala BPKP).
- **Laporan hasil pengawasan**: Kepala BPKP, JPT Madya, JPT Pratama.
- **Dokumentasi Pengawasan**: JPT Pratama, Administrator/Koordinator, atau Staf/Jabatan Fungsional (tanpa kop dan cap unit kerja).

Pelimpahan wewenang melalui **delegasi** (tanggung jawab pindah; tidak pakai a.n.) atau **mandat** (tanggung jawab tetap pada pejabat definitif; pakai a.n./u.b./Plt./Plh.). Matriks lengkap 32 jenis naskah + Tabel III.2 (ke instansi luar BPKP) ada di [Matriks Penanda Tangan](references/matriks-penanda-tangan.md).

## 4. Alur Kerja (Workflow)

### Langkah 1: Identifikasi kebutuhan
Tanyakan jika belum jelas:
- Tujuan dan isi naskah (untuk menentukan jenis).
- Pihak yang dituju (internal BPKP atau eksternal).
- Pejabat penandatangan yang dimaksud.
- Apakah ada template/format khusus dari unit kerja -- jika ada, ikuti template.

### Langkah 2: Tentukan jenis dan validasi wewenang
- Tentukan jenis naskah menggunakan panduan di Bagian 1; rujuk referensi jenis untuk sistematika.
- Cek matriks penanda tangan: apakah pejabat yang diminta pengguna berwenang? Jika tidak, sampaikan alternatif pejabat yang berwenang atau opsi pelimpahan wewenang yang sah.

### Langkah 3: Susun draf
- Gunakan sistematika dan format sesuai jenis naskah (referensi jenis).
- Susun nomor naskah sesuai format Bagian 2; jika kode klasifikasi arsip/konseptor tidak diketahui, gunakan placeholder dan beri catatan kepada pengguna.
- Terapkan klasifikasi keamanan bila perlu (default surat dinas: Biasa/kode `S`).
- Untuk naskah elektronik berklasifikasi SR/R: ingatkan kewajiban enkripsi; TTE menggunakan sertifikat BSrE (berlaku 2 tahun).

### Langkah 4: Validasi kelengkapan
Periksa:
- [ ] Jenis naskah tepat untuk keperluan
- [ ] Struktur lengkap sesuai sistematika jenis (kop, nomor, lampiran, perihal, tanggal, tujuan, isi, penutup, tanda tangan)
- [ ] Penanda tangan berwenang (cek matriks)
- [ ] Nomor mengikuti format baku
- [ ] Derajat keamanan sesuai isi
- [ ] Singkatan dieja lengkap pada kemunculan pertama
- [ ] Bahasa formal Indonesia, EYD V

### Langkah 5: Penyuntingan bahasa
Terapkan prinsip humanisasi dan pemeriksaan EYD V sebagaimana diuraikan pada skill `laporan-pengawasan-bpkp` (Bagian 7 dan 8): hindari artefak chatbot, pertahankan istilah teknis dan kutipan regulasi, periksa huruf kapital jabatan, kata depan vs imbuhan, tanda baca, dan singkatan.

## 5. Interaksi dengan Pengguna

- Jika pengguna hanya menyebut "buatkan surat" tanpa detail, tentukan sendiri jenis yang paling tepat berdasarkan konteks, lalu konfirmasi singkat sebelum finalisasi.
- Jika pejabat penanda tangan yang diminta tidak berwenang menurut matriks, jelaskan dan tawarkan pejabat yang berwenang atau skema delegasi/mandat.
- Jika diminta mengedit naskah yang sudah ada, pertahankan substansi dan fakta; fokus pada kesesuaian format TND, struktur, dan bahasa.
- Jika pengguna memberikan template unit kerja yang berbeda dari Peraturan 4/2026, ikuti template tersebut dan beri catatan jika ada penyimpangan material.
- Skill ini tidak menggantikan peraturan teknis lain (misal pengadaan barang/jasa atau SPD yang kini diatur peraturan terpisah); rujuk peraturan khusus bila formatnya diatur terpisah.

---

## 6. Standar Formatting, Indentasi, & Penomoran Word (docx)

Berdasarkan implementasi standar naskah dinas dan laporan pengawasan BPKP pada Microsoft Word (`docx`):

### 6.1 Pengaturan Halaman & Tipografi
- **Ukuran Kertas & Margin:** Kertas A4 (21,0 cm x 29,7 cm). Margin Kiri: 3,0 cm (1.18", ruang jilid); Margin Atas, Kanan, dan Bawah: 2,0 cm (0.79").
- **Font:** Font resmi **Arial** 100% konsisten pada seluruh teks. Pada OpenXML Word wajib menyertakan:
  `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/>`
- **Ukuran Font:**
  - Judul Dokumen/Naskah: Arial 12–14 pt Bold (Cover: Arial 14–16 pt Bold)
  - Nama Lembaga Cover: Arial 13 pt Bold; Nama Perwakilan/Kedeputian: Arial 12 pt Bold
  - Heading 1/Judul Bab: Arial 12 pt Bold, Rata Tengah, Spasi Atas 12 pt, Spasi Bawah 6 pt
  - Heading 2 & Heading 3: Arial 12 pt Bold, Rata Kiri, Spasi Atas 12 pt, Spasi Bawah 6 pt
  - Sub-Heading / Butir Temuan (`a.`, `b.`): Arial 12 pt Bold
  - Isi Narasi Paragraf / Rincian: Arial 12 pt Regular
  - Header & Isi Tabel: Arial 10 pt (Header Bold, Isi Regular)
  - Catatan Kaki, Keterangan Sumber Tabel, Alamat Kop: Arial 9 pt Regular / Italic
- **Spasi & Perataan:** Line spacing **1,15 line pitch** (`w:line="276"`), Space After **6 pt** (`w:after="120"` dxa), Space Before **0 pt** (khusus sub-heading: Space Before **8 pt**). Perataan teks wajib **100% Justified (Rata Kiri-Kanan)**.

### 6.2 Headings Bertingkat: Style Word, Google Docs, & Markdown

Pemisahan dan penerapan *style Heading* bawaan Word / Google Docs (`Heading 1` s.d. `Heading 4`) sangat penting agar Navigation Panel (Pohon Navigasi) dan Daftar Isi (TOC) terbentuk otomatis dan utuh hingga level sub-temuan/sub-pokok naskah.

> [!important] KEHARUSAN PENERAPAN HEADING BERTINGKAT (MARKDOWN & DOKUMEN OFFICE)
> AI Asisten dan penyusun naskah **WAJIB** menerapkan struktur heading bertingkat secara hierarkis dan konsisten pada setiap draf narasi, baik luaran teks/markdown maupun dokumen DOCX/Google Docs.
> **DILARANG** menyajikan judul bab/bagian/topik hanya sebagai teks biasa yang ditebalkan (`**tebal**`) tanpa penanda heading!

#### A. Dua Skema Hierarki Heading Resmi BPKP

1. **Skema 1: Laporan Pengawasan Bab Panjang (LHP / LHE / LHR)**
   - **Level 1 (`#` / `Heading 1` / `HEADING_1`)**: Judul BAB — Arial 12pt Bold, Center.
     *Contoh:* `# BAB I SIMPULAN DAN REKOMENDASI` atau `# BAB III HASIL EVALUASI`
   - **Level 2 (`##` / `Heading 2` / `HEADING_2`)**: Bagian BAB (Huruf Kapital) — Arial 12pt Bold, Left.
     *Contoh:* `## A. Simpulan`, `## B. Rekomendasi`, `## A. Latar Belakang`
   - **Level 3 (`###` / `Heading 3` / `HEADING_3`)**: Topik Temuan / Topik Evaluasi (Angka Desimal) — Arial 12pt Bold, Left.
     *Contoh:* `### 1. Tata Kelola Lahan Pertanian Belum Tertata Optimal`
   - **Level 4 (`####` / `Heading 4` / `HEADING_4`)**: Sub-Temuan / Aspek 5C (Huruf Kecil) — Arial 12pt Bold, Left.
     *Contoh:* `#### a. Penetapan LP2B Belum Memiliki Regulasi Definitif`
   - **Level 5 (`#####` / Normal `ilvl=3` / `HEADING_5`)**: Rincian Lokus / Entitas Uji Petik (`1)`) — Arial 12pt Regular, Indent 1,25".
     *Contoh:* `##### 1) Pemerintah Provinsi Papua Tengah`
   - **Level 6 (`######` / Normal `ilvl=4` / `HEADING_6`)**: Detail Butir Permasalahan (`a)`) — Arial 12pt Regular, Indent 1,50".
     *Contoh:* `###### a) Rincian Realisasi Anggaran Bantuan`

2. **Skema 2: Notisi Pembahasan & Naskah Dinas Khusus**
   - **Level 1 (`#` / `Heading 1` / `HEADING_1`)**: Judul Dokumen / Angka Romawi Utama — Arial 12pt Bold, Center.
     *Contoh:* `# NOTISI HASIL PENGAWASAN` atau `# I. RINGKASAN HASIL EVALUASI`
   - **Level 2 (`##` / `Heading 2` / `HEADING_2`)**: Seksi Huruf Kapital atau Satuan Kerja — Arial 12pt Bold, Left.
     *Contoh:* `## A. Perencanaan dan Prioritisasi Bantuan` atau `## 1. SMP Negeri 1 Mimika`
   - **Level 3 (`###` / `Heading 3` / `HEADING_3`)**: Sub-Seksi Angka Desimal atau Sub-Topik — Arial 12pt Bold, Left.
     *Contoh:* `### 1. Pemenuhan Kuota Usulan oleh Pemda` atau `### a. Bantuan Revitalisasi Sarana Fisik`
   - **Level 4 (`####` / `Heading 4` / `HEADING_4`)**: Sub-Temuan / Uraian Masalah Lapangan — Arial 12pt Bold, Left.
     *Contoh:* `#### a. Ruang Kelas Rusak Berat Belum Terdata`
   - **Level 5 (`#####` / Normal `ilvl=3`)**: Rincian Fakta Lapangan (`1)`) — Arial 12pt Regular.
   - **Level 6 (`######` / Normal `ilvl=4`)**: Butir Rekomendasi/Detail (`a)`) — Arial 12pt Regular.

#### B. Pemetaan Style Word & Google Docs

| Elemen Hierarki | Markdown | Style Word (docx) | Style Google Docs API | Muncul di Outline / Panel Navigasi? |
|---|---|---|---|---|
| **Judul BAB / Dokumen** | `#` | `Heading 1` | `HEADING_1` | Ya (Level 1) |
| **Bagian BAB / Seksi Romawi** | `##` | `Heading 2` | `HEADING_2` | Ya (Level 2) |
| **Topik Utama / Sub-Seksi** | `###` | `Heading 3` | `HEADING_3` | Ya (Level 3) |
| **Sub-Temuan / Butir 5C (`a.`)** | `####` | `Heading 4` | `HEADING_4` | Ya (Level 4) |
| **Rincian Lokus (`1)`)** | `#####` | Normal (`ilvl=3`) / `Heading 5` | `HEADING_5` / `NORMAL_TEXT` | Opsional |
| **Detail Butir (`a)`)** | `######` | Normal (`ilvl=4`) / `Heading 6` | `HEADING_6` / `NORMAL_TEXT` | Tidak (Body) |

**Aturan Bold & Font pada Heading & Sub-Heading:**
- **Heading 1/2/3/4 (style Word & Docs):** Bold 12 pt — seluruh teks tajuk termasuk nomor otomatis adalah Bold Arial 12 pt Hitam (`#000000`).
- **Line break pada Heading 1:** Judul bab dan nama bab disatukan dalam satu paragraf heading dengan line break (`\n`), misalnya: `BAB I\nSIMPULAN DAN REKOMENDASI`, agar di panel navigasi terbaca sebagai satu kesatuan tajuk.
- **Sub-Heading Butir (`a.`, `b.`):** Gunakan `Heading 4` / `####`. Seluruh teks pada paragraf tersebut (nomor + judul) adalah Bold.
- **Paragraf narasi/isi:** Regular 12 pt — tidak ada Bold kecuali judul butir pada detail item.
- **Larangan:** DILARANG mem-Bold kata atau frasa di tengah paragraf narasi untuk penekanan. Penekanan dalam naskah dinas dilakukan melalui diksi tegas, bukan format.

> **Catatan ukuran font:** Seluruh teks (heading, sub-heading, body, narasi) diseragamkan menjadi **12 pt** untuk konsistensi. Hanya tabel (10 pt) dan catatan kaki/sumber (9 pt) yang berbeda.

### 6.3 Sistem Numbering Multilevel Word (`numbering.xml` / `w:numPr`)

Untuk dokumen yang dibangun dari nol atau tanpa template numbering bawaan, gunakan sistem multilevel list Word native:

| `ilvl` | Format | `numFmt` | Contoh | Fungsi |
|---|---|---|---|---|
| 0 | `%1.` | `upperLetter` | **A.** | Heading 2 — Bagian utama |
| 1 | `%2.` | `decimal` | **1.** | Heading 3 — Sub-bagian |
| 2 | `%3.` | `lowerLetter` | **a.** | Butir pembahasan (Bold, bukan style Heading) |
| 3 | `%4)` | `decimal` | **1)** | Rincian per unit/lokus |
| 4 | `%5)` | `lowerLetter` | **a)** | Detail butir |

**Aturan Restart:**
- **Bab/Bagian baru:** Buat instance `<w:num>` baru dengan `lvlOverride startOverride=1` pada semua level (0–4).
- **Sub-bagian baru:** Berbagi `numId` induk; nomor berlanjut sekuensial. Sub-level otomatis restart saat level atas maju.
- Setiap level dalam `abstractNum` wajib menyertakan `<w:rPr>` dengan `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>` dan `<w:sz w:val="24"/>` (12 pt).

### 6.4 Sistem Tab Stop & Hierarki Indentasi Presisi (Hanging Indent Cascade)

Sistem indentasi menggunakan prinsip **cascade**: posisi nomor setiap level sejajar dengan posisi awal teks pada level di atasnya. Jarak antar level = 360 dxa (0,25").

#### Formula Cascade (dxa = twips, 1440 dxa = 1 inci)

| `ilvl` | Format | Nomor di (dxa) | Teks di (dxa) | `w:ind w:left` | `w:ind w:hanging` | `w:tab w:pos` |
|---|---|---|---|---|---|---|
| 0 | `A.` | 360 | 720 | 720 | 360 | 720 |
| 1 | `1.` | 720 | 1080 | 1080 | 360 | 1080 |
| 2 | `a.` | 1080 | 1440 | 1440 | 360 | 1440 |
| 3 | `1)` | 1440 | 1800 | 1800 | 360 | 1800 |
| 4 | `a)` | 1800 | 2160 | 2160 | 360 | 2160 |

> **Konversi ke inci:** 360 dxa = 0,25" | 720 = 0,50" | 1080 = 0,75" | 1440 = 1,00" | 1800 = 1,25" | 2160 = 1,50"

#### Aturan Titik Dua (`:`) pada Naskah Dinas

Tanda titik dua memiliki beberapa konteks penggunaan dengan aturan format berbeda:

**A. Metadata Kop Surat:**
Label rata kiri dengan padding tetap, lalu `:`, lalu spasi, lalu nilai. Tanpa spasi sebelum `:`.
```
Nomor    : PE.09.02/ST-314/PW36/2/2026
Lampiran : Satu Berkas
Hal      : Surat Tugas
```

**B. Pengantar Daftar Bernomor:**
Kalimat pengantar yang diikuti daftar bernomor **wajib diakhiri titik dua** (bukan titik/koma). Tidak boleh ada teks tambahan setelah titik dua pada baris yang sama.
```
...dengan rincian:
1) ...
2) ...
```

**C. Label Nama/Lokus:**
Pada mode numbering otomatis, nama lokus **tidak menggunakan titik dua** — nama lokus berdiri sebagai sub-heading bernomor pada paragraf tersendiri (Regular, tanpa Bold), dan narasi mengikuti pada paragraf terpisah di bawahnya.

Pada mode manual (legacy/fallback), nama atau label diikuti `:` menempel tanpa spasi sebelum, lalu satu spasi sebelum narasi. Nama/label Bold, narasi Regular:
```
1) Provinsi Papua Tengah: [narasi]
```

> **Mode otomatis lebih disukai** karena menghasilkan struktur yang lebih bersih.

**D. Sumber Tabel:**
```
Sumber: [Instansi], [Tahun]
```
Dicetak miring (*Italic*), Arial 9 pt.

### 6.5 Standar Tabel Naskah Dinas BPKP (Clean Open-Table Style)
- Garis border **hanya horizontal** (Top, Bottom, Header separator `sz="4"`, warna `#B0B0B0` atau `#000000`), **tanpa border vertikal** (*Left, Right, InsideV = none*).
- Header row shading abu-abu lembut (`#F2F2F2`), Font Arial 10 pt Bold, Center/Left aligned, Vertically centered.
- Padding sel: Atas/Bawah 100 dxa (~5 pt), Kiri/Kanan 150 dxa (~7.5 pt).
- Angka rata kanan, teks uraian rata kiri/justified, nomor rata tengah. Keterangan sumber dicantumkan di bawah tabel (*Arial 9 pt Italic*).

### 6.6 Penomoran Word Otomatis vs Penomoran Manual
- Seluruh elemen penomoran otomatis Word (`w:numPr`, `numbering.xml`), *list level*, dan *indentation* asli dari template harus dipergunakan dan dipertahankan.
- **DILARANG** mengetik nomor manual teks (seperti `1. `, `a. `, `1) `) pada paragraf yang sudah menggunakan penomoran otomatis Word (`w:numPr`) guna menghindari penomoran ganda (*double numbering*).
- **Format Nomor Manual (Fallback):** Bila terpaksa menggunakan penomoran manual teks, format: `[nomor]\t[teks]` dengan tab stop eksplisit. Jangan gunakan spasi sebagai pemisah. Contoh: `a.\tJudul` (dengan tab stop di 1440 dxa).

### 6.7 Standar Kompatibilitas Google Workspace / Google Docs (GWS)
Saat dokumen dirender atau dimanipulasi pada Google Docs melalui Google Workspace API / MCP:
1. **Pembersihan Indentasi dalam Sel Tabel (Anti-Loncatan Ruler):**
   - Setiap paragraf di dalam sel tabel wajib memiliki deklarasi indentasi nol eksplisit: `<w:ind w:left="0" w:right="0" w:firstLine="0"/>` (`indentStart: 0, indentFirstLine: 0`).
   - Jangan biarkan paragraf sel mewarisi indentasi paragraf global agar *blue marker ruler* tidak bergeser ke tengah atau membuat *hanging indent* liar.
2. **Struktur Tabel Metadata & Kop Resmi:**
   - **Tabel Nomor/Tanggal Cover (3 Kolom):** Kolom Label (`84 pt`), Kolom Separator `:` (`27.75 pt`), Kolom Nilai (`222.75 pt`). Paragraf sel berindentasi seragam (`14.17 pt`).
   - **Tabel Kop Surat (2 Kolom):** Kolom Logo (`86.7 pt`), Kolom Teks Lembaga (`366.3 pt`). Teks instansi rata tengah murni (`alignment: CENTER`), spasi baris 1.0, dan indentasi 0.
   - **Tabel Metadata Surat Pengantar (4 Kolom Terpisah):**
     - Kolom 1 (`69 pt`): Label (`Nomor`, `Lampiran`, `Hal`)
     - Kolom 2 (`18 pt`): Pemisah `:`
     - Kolom 3 (`237.75 pt`): Isi teks nomor/lampiran/judul laporan (*Justified*, indentasi 0)
     - Kolom 4 (`129.75 pt`): Tanggal surat (baris 1, *Right-aligned*)
     - *Catatan:* Tanggal wajib diletakkan pada kolom ke-4 mandiri (bukan *right tab stop*) agar judul laporan pada baris `Hal` tidak mengalami *hanging indent* saat *line wrapping*.
3. **Penyelarasan Narasi di Bawah Sub-Heading Level 1 (`HEADING_3` / `1.`):**
   - Tajuk sub-bagian bernomor (misal `1. Anggaran Ketahanan Pangan Daerah`) memiliki `indentFirstLine: 36 pt` (nomor) dan `indentStart: 54 pt` (teks judul).
   - Paragraf narasi/isi di bawahnya wajib diset persis dengan **`indentStart: 54 pt` (0.75" / 1080 dxa) dan `indentFirstLine: 54 pt`**, sehingga seluruh baris narasi sejajar 100% dengan huruf pertama judul poinnya.


---

## 7. Modul Python Bawaan (Scripts) — Helper Naskah Dinas

Skill ini membundel modul Python siap pakai di folder `scripts/` untuk menyusun komponen naskah dinas (kop surat, nota dinas, surat tugas, lembar pengesahan) yang sesuai Peraturan BPKP 4/2026. Modul ini mengimpor engine inti dari skill `laporan-pengawasan-bpkp` untuk konsistensi format.

### 7.1 Paket & File

```
scripts/
├── __init__.py
└── naskah_dinas_helper.py    # Helper: kop, nota dinas, surat tugas, lembar pengesahan, TTE
```

### 7.2 Cara Mengimpor

```python
import sys
sys.path.insert(0, r"<skills-dir>/tata-naskah-dinas-bpkp/scripts")

from naskah_dinas_helper import (
    add_kop_surat, add_nota_dinas_header, add_surat_tugas_header,
    add_lembar_pengesahan, add_tte_marker
)

# Engine inti (dari skill laporan-pengawasan-bpkp)
sys.path.insert(0, r"<skills-dir>/laporan-pengawasan-bpkp/scripts")
from bpkp_docx_engine import create_document
```

### 7.3 API Helper (`naskah_dinas_helper.py`)

| Fungsi | Kegunaan |
|---|---|
| `add_kop_surat(doc, unit_kerja, alamat, telepon, email, website, kode_pos)` | Kop surat BPKP (nama lembaga, unit kerja, alamat, garis pembatas). |
| `add_nota_dinas_header(doc, nomor, sifat, lampiran, hal, kepada, dari, tempat_tanggal)` | Header nota dinas (tabel 2 kolom: Nomor/Sifat/Lampiran/Hal + Kepada/Dari/Tanggal). |
| `add_surat_tugas_header(doc, nomor, sifat, lampiran, hal)` | Header surat tugas (tabel 2 kolom: Nomor/Sifat/Lampiran/Hal). |
| `add_lembar_pengesahan(doc, judul_laporan, tempat_tanggal, pejabat_list)` | Halaman lembar pengesahan (tabel Nama/Jabatan/Tanda Tangan + TTE). |
| `add_tte_marker(doc)` | Placeholder Tanda Tangan Elektronik (abu-abu italic). |

### 7.4 Contoh Penggunaan

```python
import sys
sys.path.insert(0, r"<skills-dir>/tata-naskah-dinas-bpkp/scripts")
sys.path.insert(0, r"<skills-dir>/laporan-pengawasan-bpkp/scripts")

from bpkp_docx_engine import create_document
from naskah_dinas_helper import add_kop_surat, add_nota_dinas_header

doc = create_document()

# Kop surat
add_kop_surat(
    doc,
    unit_kerja="Perwakilan BPKP Provinsi Papua Tengah",
    alamat="Jl. Pemuda No. 1, Nabire",
    telepon="(0986) 123456",
    email="perwakilan.ptengah@bpkp.go.id",
    kode_pos="98811",
)

# Header nota dinas
add_nota_dinas_header(
    doc,
    nomor="ND-01/PW.T/01/2026",
    sifat="Biasa",
    lampiran="-",
    hal="Permohonan Data Pendukung",
    kepada="Kepala Dinas Tanaman Pangan",
    dari="Kepala Perwakilan BPKP",
    tempat_tanggal="Nabire, 15 Januari 2026",
)

doc.save("NotaDinas.docx")
```

---

## 8. Naskah Penugasan & Kendali Mutu Pengawasan (Pakta Integritas & KM 4–6)

Pada pelaksanaan pengawasan intern BPKP, Surat Tugas (ST) selalu disertai naskah pendukung penugasan yang wajib mematuhi standar format tata naskah dinas dan sistem kendali mutu pengawasan.

### 8.1 Pakta Integritas Penugasan Pengawasan

Pakta Integritas merupakan komitmen etika dan integritas tim sebelum melaksanakan penugasan pengawasan. Dokumen ini wajib dibuat dengan standar presisi:
- **Ketentuan Format & Layout:**
  - Kertas: A4 (21,0 cm x 29,7 cm), layout **tepat 1 halaman penuh (single page)**.
  - Margin: Kiri 3,0 cm (ruang jilid/arsip), Kanan 2,0 cm, Atas 2,0 cm, Bawah 2,0 cm.
  - Kop naskah dinas: BPKP Perwakilan / Unit Kerja eselon II terkait, garis pemisah kop tebal (`sz=18`).
  - Tipografi: Arial konsisten (Judul 13pt bold, Subjudul/Isi 10.5–11pt spasi 1.15, Tabel TTD 10pt spasi 1.0).
  - Poin Komitmen: 7 butir komitmen integritas menggunakan penomoran multilevel native Word (`<w:numPr>`) dengan *hanging indent* rapi.
- **Tabel Penandatangan Tim (Struktur Berjenjang):**
  - Menggunakan format tabel dinas tanpa garis vertikal (*clean table*, garis pembatas horizontal tipis).
  - Memuat seluruh peran tim: Penanggung Jawab, Pengendali Mutu/Teknis (Dalnis), Ketua Tim, dan Anggota Tim lengkap dengan NIP.

### 8.2 Formulir Kendali Mutu Pengawasan (Format KM 4, KM 5, KM 6)

Kendali mutu penugasan pengawasan dituangkan ke dalam kertas kerja spreadsheet terintegrasi:
- **Format KM 4 (Program Kerja Pengawasan / PKP):**
  - Memuat rincian langkah kerja audit/evaluasi, tujuan pengujian, prosedur pemeriksaan, waktu alokasi rencana, pelaksana tugas, dan kolom paraf persetujuan Pengendali Teknis.
- **Format KM 5 (Alokasi Rencana Jam Kerja / Mandays):**
  - Rencana alokasi jam kerja efektif tim (PJ, Dalnis, KT, AT) yang dirinci menurut tahapan: Persiapan, Pelaksanaan Lapangan, dan Penyusunan Laporan Hasil Pengawasan.
- **Format KM 6 (Realisasi Jam Kerja Pengawasan):**
  - Pencatatan berkala/kumulatif realisasi jam kerja mandays per penugasan, link formula ke KM 5 untuk menghitung varians/selisih efisiensi jam kerja.
- **Formula Keterkaitan Antar-Sheet (Inter-Sheet Automation):**
  - **Sinkronisasi Metadata:** Seluruh sheet (KM 4, KM 5, KM 6) mereferensikan sel metadata utama (Nomor ST, Tanggal ST, Nama Penugasan, Objek Pengawasan, Periode Penugasan).
  - **Kalkulasi Mandays Otomatis:** Perhitungan hari kerja menggunakan formula `=NETWORKDAYS(start_date, end_date, libur)` atau konversi jam kerja standar (1 Mandays = 7,5 jam kerja efektif BPKP).
  - **Lookup Profil Tim:** Nama dan NIP tim diambil otomatis via formula `=VLOOKUP(...)` atau `=XLOOKUP(...)` dari master data pegawai.

### 8.3 Ekstraksi dan Penanganan Tanda Tangan Transparan

Untuk menyematkan tanda tangan basah hasil scan ke dokumen naskah dinas (DOCX/XLSX) tanpa merusak tampilan layout:
1. **Penghapusan Latar Belakang (Alpha Thresholding):**
   - Latar belakang putih/kusam wajib dikonversi menjadi transparansi (kanal Alpha / RGBA).
   - Gunakan skrip Python Pillow:
     ```python
     from PIL import Image

     def make_signature_transparent(input_path: str, output_path: str, threshold: int = 220):
         img = Image.open(input_path).convert("RGBA")
         datas = img.getdata()
         new_data = []
         for item in datas:
             # Jika piksel mendekati putih, jadikan transparan
             if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                 new_data.append((255, 255, 255, 0))
             else:
                 new_data.append(item)
         img.putdata(new_data)
         img.save(output_path, "PNG")
     ```
2. **Penyisipan ke Dokumen TND (Word / Excel):**
   - Pada Word (`python-docx`), sisipkan tanda tangan langsung ke sel tabel penandatangan dengan lebar proporsional (`width = Cm(2.5)` s.d. `Cm(3.0)`).
   - Pastikan paragraf sel tabel memiliki indentasi 0 dan spasi before/after 0 agar posisi tanda tangan tidak menggeser batas baris tabel dan tidak menabrak baris NIP.

---

## 9. Master Template Library & Unified Generator Engine

Skill ini dilengkapi dengan **46 Master Template Microsoft Word (.docx)** resmi sesuai Peraturan BPKP Nomor 4 Tahun 2026 di direktori `assets/templates/` dan mesin generator tunggal `scripts/generate_naskah.py`.

### 9.1 Mekanisme Kop Surat Perwakilan Terpusat (`assets/unit_profiles.json`)
Kop surat untuk unit perwakilan dan pusat dikonfigurasi secara modular. Profil mencakup nama instansi, alamat, nomor telepon/faks, email, website, kota kedudukan, serta kode unit naskah dinas:
- **`papua_tengah`**: Perwakilan BPKP Provinsi Papua Tengah di Nabire (Kode Unit: `PW36`)
- **`kalsel`**: Perwakilan BPKP Provinsi Kalimantan Selatan di Banjarbaru (Kode Unit: `PW16`)
- **`papua`**: Perwakilan BPKP Provinsi Papua di Jayapura (Kode Unit: `PW26`)
- **`papua_barat`**: Perwakilan BPKP Provinsi Papua Barat di Manokwari (Kode Unit: `PW33`)
- **`dki`, `jabar`, `jateng`, `jatim`, `sulsel`, `sumut`, `pusat_utama`**, dll.

Untuk menambah unit kerja baru, cukup tambahkan entri JSON pada `assets/unit_profiles.json`.

### 9.2 Cara Menjalankan Generator Naskah Dinas

1. **Melihat Daftar 46 Template yang Tersedia:**
   ```bash
   python scripts/generate_naskah.py --list
   ```

2. **Melihat Daftar Profil Unit Kerja / Kop Surat:**
   ```bash
   python scripts/generate_naskah.py --list-profiles
   ```

3. **Menyusun Dokumen (Contoh: Surat Tugas Papua Tengah):**
   ```bash
   python scripts/generate_naskah.py --jenis surat_tugas --unit papua_tengah --data payload.json --output Surat_Tugas_PT.docx
   ```

4. **Menyusun Dokumen yang Sama untuk Perwakilan Lain (Contoh: Kalsel):**
   ```bash
   python scripts/generate_naskah.py --jenis surat_tugas --unit kalsel --data payload.json --output Surat_Tugas_Kalsel.docx
   ```
   *Secara otomatis kop surat tabel logo BPKP, nomor naskah (PW16 vs PW36), dan kota penandatanganan akan beralih ke Kalimantan Selatan tanpa mengubah kode generator.*


