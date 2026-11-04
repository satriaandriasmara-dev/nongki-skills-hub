---
name: laporan-pengawasan-bpkp
description: Menyusun, memperbaiki, dan mengisi laporan hasil pengawasan internal BPKP (LHP, LHE, LHR, Notisi Hasil Pengawasan, serta Berita Acara Exit Meeting) berbasis Global Internal Audit Standards (IIA 15.1) dan Peraturan BPKP Nomor 4 Tahun 2026. Skill ini merupakan MASTER SKILL yang secara mandiri mengintegrasikan secara penuh (built-in) kaidah Tata Naskah Dinas BPKP (tata-naskah-dinas-bpkp), eliminasi tanda pisah (em dash), penyuntingan bahasa alami auditor profesional (humanizer-indonesia), serta tata ejaan baku resmi EYD V (eyd-indonesia).
tags: [bpkp, laporan-pengawasan, lhp, lhe, lhr, notisi, temuan-audit, 5c, iia, audit-internal, eyd-indonesia, humanizer-indonesia, tata-naskah-dinas-bpkp, peraturan-bpkp-4-2026]
---

# Laporan Pengawasan BPKP (Master Integrated Skill)

Skill ini membantu menyusun laporan hasil pengawasan internal (Laporan Hasil Pemeriksaan/LHP, Laporan Hasil Evaluasi/LHE, Laporan Hasil Reviu/LHR, Notisi) sesuai prinsip Global Internal Audit Standards (IIA Standard 15.1) yang diadaptasi ke dalam konteks BPKP.

> [!important] MASTER INTEGRATED SKILL (ALL-IN-ONE) — TIDAK PERLU PEMANGGILAN TERPISAH
> Skill ini dirancang secara mandiri memuat seluruh kapabilitas:
> 1. **Tata Naskah Dinas BPKP (Peraturan BPKP Nomor 4 Tahun 2026)**: Kop surat tabel resmi, penomoran, penanda tangan, etika WBS & anti-suap/gratifikasi.
> 2. **Humanizer Indonesia (Gaya Auditor Profesional)**: Bahasa lugas, objektif, menghilangkan artefak bot, tidak mekanis.
> 3. **Pemeriksaan EYD V**: Ejaan, huruf kapital, tanda baca, kata depan, partikel, serapan.
> **Auditor/Asisten AI WAJIB menjalankan seluruh kaidah ini secara terpadu dalam satu siklus pengerjaan tanpa meminta pengguna memanggil skill eyd-indonesia, humanizer-indonesia, atau tata-naskah-dinas-bpkp secara terpisah.**

---

> [!caution] HIERARKI KEUTAMAAN FORMAT: TEMPLATE PENGGUNA ADALAH PRIORITAS 1 (MUTLAK)
> 1. **Template-First Principle**: Jika pengguna menyediakan atau merujuk file template/draf laporan tertentu (misal: Evaluasi Pembiayaan Daerah, Notisi Pembahasan, LHP Kinerja, atau dokumen berformat surat pendek), **FORMAT DAN STRUKTUR TEMPLATE PENGGUNA TERSEBUT MENJADI ACUAN TERTINGGI**.
> 2. **Dilarang Overfitting Contoh Ketapang**: Dokumen contoh (seperti Laporan Ketapang atau contoh di `references/template-format.md`) adalah **contoh kasus multi-lokus berskala besar**, BUKAN cetak biru wajib untuk semua laporan. **DILARANG** merombak atau memaksakan susunan dokumen pengguna menjadi bab-bab Ketapang jika pengguna sudah memiliki template sendiri!
> 3. **Pencegahan Duplikasi Metadata (Nomor, Lampiran, Hal)**: Jika template dokumen pengguna sudah memiliki baris/tabel kop dan metadata `Nomor`, `Lampiran`, `Hal`, **LAKUKAN PENGISIAN / PERBAIKAN SECARA IN-PLACE**. Dilarang keras menyisipkan tabel metadata tambahan yang mengakibatkan penulisan Nomor, Lampiran, Hal tertulis dua kali!
> 4. **Invarian Nomor dan Tanggal Laporan (Draf)**: Saat membuat laporan atau draf laporan hasil pengawasan, **nomor laporan dan tanggal laporan JANGAN DIISI**. Cukup diisi placeholder `"   "` (tripel spasi kosong) saja, baik pada cover, metadata surat pengantar, maupun kaki/tanda tangan, karena penomoran agenda keluar dan penanggalan resmi dilakukan oleh sekretaris/tata usaha.

> [!important] Acuan Tata Naskah Dinas: Peraturan BPKP 4/2026
> Skill ini mengacu pada **Peraturan BPKP Nomor 4 Tahun 2026 tentang Tata Naskah Dinas** (BAB V-C.5 Laporan, BAB IV Pengamanan, BAB III Pejabat Penanda Tangan), yang menggantikan Peraturan BPKP Nomor 4 Tahun 2022. Detail lihat Bagian 11.

Baca [Panduan Standar IIA](references/standar-iia.md) untuk kerangka struktural dan prinsip kualitas komunikasi. Baca [Contoh Struktur Laporan](references/template-format.md) sebagai salah satu contoh format -- bukan format baku (lihat Bagian 2).

## 1. Prinsip Kualitas Komunikasi (IIA)

Setiap teks laporan yang dihasilkan wajib memenuhi 6 karakteristik:

| Prinsip | Penerapan |
|---|---|
| **Akurat** | Data, angka, dan rujukan regulasi harus presisi. Verifikasi setiap angka yang disebut. |
| **Objektif** | Fakta nyata, tanpa opini subjektif. Gunakan "berdasarkan hasil evaluasi..." bukan "menurut kami..." |
| **Jelas** | Bahasa formal Indonesia, hindari jargon yang tidak perlu. Singkatan dieja lengkap pada kemunculan pertama. |
| **Ringkas** | Langsung ke pokok masalah. Satu paragraf = satu ide utama. Hindari pengulangan. |
| **Konstruktif** | Nada membantu perbaikan, bukan menyalahkan. Rekomendasi berorientasi solusi. |
| **Tepat Waktu** | Sajikan informasi yang relevan dengan periode pengawasan yang sedang berjalan. |

## 2. Struktur Dokumen: Tidak Baku, Bervariasi

**PENTING**: Struktur laporan BPKP **tidak baku**. Setiap jenis penugasan (evaluasi, pemeriksaan, reviu, audit kinerja, audit investigasi, dll.) dapat memiliki format dan susunan BAB yang berbeda-beda, tergantung pada:
- Jenis penugasan dan pedoman teknis yang berlaku
- Arahan dari pimpinan/penanggung jawab penugasan
- Template yang sudah disediakan oleh unit kerja

Contoh struktur di [references/template-format.md](references/template-format.md) hanya merupakan **satu contoh** dari jenis Laporan Hasil Evaluasi (LHE). Jangan gunakan contoh tersebut sebagai format wajib untuk semua laporan.

### Pendekatan yang benar:
1. **Jika pengguna memberikan template**: Ikuti template tersebut. Jangan memaksakan struktur dari contoh.
2. **Jika pengguna tidak memberikan template**: Tanyakan jenis penugasan dan apakah ada format/template yang harus diikuti. Jika tidak ada, gunakan contoh di references sebagai titik awal dan sesuaikan.
3. **Yang selalu berlaku di semua jenis laporan**: Kerangka 5C untuk temuan (Bagian 3), prinsip kualitas komunikasi (Bagian 1), distribusi terbatas (Bagian 4), dan conformance statement (Bagian 5).

### Placeholder dan Kertas Kerja

Jika pengguna sudah menyediakan **template laporan** (dalam format DOCX atau format lain), placeholder/variabel yang perlu diisi pada template tersebut **umumnya berasal dari kertas kerja berbentuk xlsx** (spreadsheet). Kertas kerja xlsx biasanya memuat data temuan, angka realisasi, target, bukti audit, dan informasi pendukung lainnya yang perlu dipindahkan ke dalam template laporan.

Skill ini tidak memiliki kemampuan bawaan untuk membaca file xlsx. Jika pengguna perlu mengambil data dari kertas kerja xlsx untuk mengisi placeholder template, gunakan **skill atau alat terpisah** untuk membaca xlsx terlebih dahulu, lalu gunakan data yang diperoleh untuk mengisi template laporan melalui skill ini.

## 3. Kerangka Penulisan Temuan: Metode 5C & Multi-Lokus

Setiap temuan/permasalahan harus diurai menggunakan kerangka 5C. Dalam pengawasan kewilayahan/multi-entitas (misalnya tingkat Provinsi dan beberapa Kabupaten/Kota), uraian temuan mengikuti pola agregat dan rincian per lokus berikut:

### Pola Naratif Per Sub-Topik (Format Multi-Lokus)

```
[a./b./c.] [Judul Permasalahan Spesifik] (Bold 12pt)

Kondisi di tingkat wilayah pengawasan diuraikan sebagai berikut:

1) [Nama Entitas/Provinsi]: [Uraian fakta kondisi riil, data kuantitatif, target vs realisasi, temuan lapangan].
2) [Nama Entitas/Kabupaten A]: [Uraian fakta kondisi riil, data kuantitatif, target vs realisasi, temuan lapangan].
3) [Nama Entitas/Kabupaten B]: [Uraian fakta kondisi riil, data kuantitatif, target vs realisasi, temuan lapangan].

[Kriteria / Regulasi]
(.)  <-- Warna MERAH jika masih berupa draf/placeholder/unverified
-- ATAU --
"Kondisi tersebut tidak sesuai dengan [Regulasi/Peraturan] Nomor [X] Tahun [XXXX] tentang [Judul], Pasal [X] ayat ([X]) yang menyatakan bahwa '[Kutipan normatif]'." (Warna HITAM jika sudah definitif)

[Penyebab / Root Cause]
Kondisi tersebut disebabkan oleh [akar masalah sistemik, bukan sekadar gejala permukaan].

[Akibat / Dampak / Risiko]
Akibatnya, [dampak negatif riil atau potensi risiko finansial/operasional/kegagalan target].

[Rekomendasi / Corrective Action]
Atas permasalahan tersebut, direkomendasikan agar:
1) [Rekomendasi untuk level Provinsi / Pimpinan Daerah];
2) [Rekomendasi untuk level Kabupaten / OPD Teknis].
```

### Pola Naratif Per Topik Utama (Agregat)

Sebelum masuk ke sub-topik `a.`, `b.`, dst., diawali dengan:
```
[Heading 3] [Nomor & Judul Topik Utama] (misal: 1. Lahan Pertanian Belum Terkelola dengan Efektif)

[Paragraf Simpulan Umum Topik]
Uraikan gambaran umum kondisi menyeluruh pada topik tersebut di seluruh wilayah pengawasan secara ringkas dan padat.
```

Setelah seluruh sub-topik temuan selesai, topik ditutup dengan bagian **Tanggapan Mitra Evaluasi dan Rencana Aksi**:
```
Tanggapan Mitra Evaluasi dan Rencana Aksi
Atas hasil evaluasi yang telah disampaikan, pihak [Pemerintah Daerah / OPD terkait] menyatakan sependapat dan berkomitmen menyusun rencana aksi penyelesaian tindak lanjut dengan rincian:
1) [Uraian rencana aksi 1] diselesaikan paling lambat [Bulan/Tahun];
2) [Uraian rencana aksi 2] diselesaikan paling lambat [Bulan/Tahun].
```

### Kunci Penulisan 5C dalam Konteks BPKP

- **Criteria**: Selalu kutip regulasi spesifik (UU, PP, Permen, Perda, Perbup, SE, Juknis) beserta pasal dan ayat. Tandai warna **MERAH (`RGB(255, 0, 0)`)** bila masih placeholder `(.)` atau butuh verifikasi regulasi.
- **Condition**: Nyatakan fakta berbasis bukti KKE (Kertas Kerja Evaluasi). Sajikan perbandingan target vs realisasi atau tabel pendukung bila tersedia.
- **Cause**: Identifikasi akar masalah (*root cause*) dengan awalan baku: `"Kondisi tersebut disebabkan oleh..."`.
- **Consequence**: Nyatakan dampak nyata atau risiko potensial dengan awalan baku: `"Akibatnya, ..."`.
- **Corrective Action / Rekomendasi**: Berjenjang (strategis untuk Kepala Daerah, operasional untuk Kepala OPD) dengan awalan baku: `"Atas permasalahan tersebut, direkomendasikan agar: ..."`.

## 4. Distribusi dan Kerahasiaan

Setiap laporan wajib memuat klausul distribusi terbatas:

> "Laporan ini terbatas ditujukan kepada [Jabatan Penerima] untuk dapat digunakan sebagai salah satu bahan pertimbangan atau rekomendasi dalam pengambilan keputusan atas permasalahan yang terjadi."

Tembusan hanya kepada pejabat yang berwenang sesuai hierarki:
- Deputi Kepala BPKP yang relevan
- Pejabat lain sesuai kebutuhan

## 5. Pernyataan Pemenuhan Norma (Conformance Statement)

Laporan wajib memuat pernyataan bahwa pengawasan telah dilakukan sesuai:
1. Standar Audit Intern Pemerintah Indonesia (SAIPI) yang diterbitkan AAIPI
2. Peraturan BPKP tentang Standar Kerja Pengawasan Intern BPKP

Contoh kalimat standar:
> "Pengawasan ini telah dilakukan sesuai Standar Audit Intern Pemerintah Indonesia yang diterbitkan Asosiasi Auditor Intern Pemerintah Indonesia (AAIPI) dan Peraturan BPKP Nomor [X] Tahun [XXXX] tentang Standar Kerja Pengawasan Intern BPKP."

## 6. Konvensi Gaya Penulisan

### Singkatan dan Akronim
- Tulis lengkap pada kemunculan pertama, diikuti singkatan dalam kurung.
  Contoh: "Lahan Pertanian Pangan Berkelanjutan (LP2B)"
- Setelahnya gunakan singkatan secara konsisten.

### Penomoran Bertingkat
Gunakan hierarki berikut (sesuaikan dengan template jika sudah disediakan):
```
A.   (bagian utama: Simpulan, Rekomendasi, dll.)
  1.  (topik utama: Lahan, Bibit, Pupuk, dll.)
    a.  (sub-temuan spesifik)
      1)  (rincian per lokus/entitas)
        a)  (detail butir)
```

#### Sistem Multilevel Numbering Word (`numbering.xml` / `w:numPr`)

Untuk dokumen yang dibangun dari nol atau tanpa template numbering bawaan, gunakan sistem multilevel list Word native sebagai berikut:

| Level (`ilvl`) | Format | `numFmt` | Contoh | Fungsi |
|---|---|---|---|---|
| 0 | `%1.` | `upperLetter` | **A.** | Heading 2 -- Bagian (Simpulan, Rekomendasi, Hasil Evaluasi) |
| 1 | `%2.` | `decimal` | **1.** | Heading 3 -- Topik utama (Lahan, Bibit, Pupuk, dst.) |
| 2 | `%3.` | `lowerLetter` | **a.** | Sub-Heading temuan spesifik (Bold, bukan style Heading) |
| 3 | `%4)` | `decimal` | **1)** | Rincian per lokus/entitas (Provinsi, Kabupaten) |
| 4 | `%5)` | `lowerLetter` | **a)** | Detail butir/rincian sub-lokus |

**Aturan Restart (`w:lvlOverride` / `w:startOverride`):**
- **Bab baru (Heading 1):** Buat instance `<w:num>` baru dengan `lvlOverride startOverride=1` pada **semua level** (0–4). Seluruh penomoran reset dari A./1./a./1)/a).
- **Topik baru (Heading 3):** Tidak membuat instance baru — topik berbagi `numId` milik Bab. Nomor topik berlanjut sekuensial (1., 2., ..., 10.). Sub-level (a., 1), a)) otomatis restart saat level atas maju, sesuai perilaku bawaan Word multilevel list.
- **Sub-temuan baru (ilvl 2):** Saat `a.` maju ke `b.`, level 3 dan 4 otomatis restart.
- **Locus baru (ilvl 3):** Saat `1)` maju ke `2)`, level 4 otomatis restart.

**Penting tentang `w:rPr` pada `w:lvl`:** Setiap level dalam `abstractNum` wajib menyertakan `<w:rPr>` dengan `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>` dan `<w:sz w:val="24"/>` (12 pt) untuk memastikan karakter nomor/letter memakai font Arial 12 pt yang konsisten.

### Nada dan Diksi
- Formal, impersonal: "telah dilakukan evaluasi..." bukan "kami mengevaluasi..."
- Konstruktif: "direkomendasikan agar..." bukan "harus segera dilakukan..."
- Hindari kata-kata emosional atau menghakimi.
- Gunakan kalimat pasif untuk temuan, kalimat aktif untuk rekomendasi.

### Tabel dan Data
- Setiap tabel harus memiliki judul dan sumber data.
- Format: "Sumber: [Nama Instansi/Dokumen], [Tahun]"

---

## 7. Humanisasi Bahasa (Built-In)

Setiap teks laporan yang dihasilkan harus terasa ditulis oleh auditor profesional untuk audiens tertentu (Bupati, Kepala OPD, Deputi), bukan teks yang terasa generik atau mekanis.

### Sasaran
Hasilkan tulisan yang terasa ditulis seseorang untuk audiens tertentu. Pertahankan tingkat formalitas, tujuan, fakta, istilah, kutipan, dan suara penulis. Dalam teks dinas, manusiawi berarti **jernih dan tidak mekanis**, bukan percakapan santai.

### Pola yang Harus Diperiksa dan Dihindari

**Artefak chatbot:**
- Pembuka seperti "Tentu", "Baik", atau "Berikut adalah" ketika teks dapat langsung dimulai.
- Penutup seperti "Semoga bermanfaat" atau tawaran bantuan yang bukan bagian dari naskah.
- Sapaan dan pujian generik yang tidak cocok dengan genre laporan.

**Klaim dan abstraksi:**
- "merupakan bukti nyata", "memainkan peran penting", "menjadi tonggak", "di tengah lanskap yang terus berkembang" tanpa informasi konkret.
- Kata evaluatif seperti "sangat penting", "komprehensif", "inovatif", atau "strategis" tanpa ukuran atau bukti.
- Atribusi kabur: "para ahli mengatakan", "banyak pihak menilai", atau "berbagai penelitian" tanpa sumber.

**Struktur mekanis:**
- Paragraf dengan pola pembuka-tiga butir-kesimpulan yang berulang.
- Setiap bagian diakhiri rangkuman yang hanya mengulang isinya.
- Kalimat berpanjang hampir sama dan selalu memakai pola subjek-predikat-objek.
- Penggunaan "selain itu", "lebih lanjut", "di sisi lain", dan "oleh karena itu" secara beruntun meski hubungan antarkalimat sudah jelas.
- Konstruksi "bukan hanya ..., melainkan juga ..." yang dipakai sebagai hiasan.

### Perbaikan yang Aman
- Ganti abstraksi dengan siapa melakukan apa, jika informasinya memang tersedia.
- Gabungkan kalimat yang mengulang; pecah kalimat yang menanggung terlalu banyak gagasan.
- Pakai kata "adalah", "ialah", "punya", atau verba langsung ketika lebih alami untuk ragam formal.
- Pertahankan istilah resmi, teknis, dan kutipan regulasi. Jangan mengarang contoh, statistik, pengalaman, atau sikap penulis.
- Variasikan panjang serta bentuk kalimat secara wajar. Jangan sengaja menambahkan kesalahan, slang, humor, opini, atau pengalaman pribadi.
- Baca keras secara mental. Hapus kalimat yang terdengar seperti slogan, presentasi korporat, atau respons chatbot.
- Lakukan audit makna: angka, nama, negasi, tingkat kepastian, hubungan sebab-akibat, dan kutipan harus tetap sama.

### 7.1 Kosakata Penanda AI Hasil Uji Lapangan Pengawasan (Terverifikasi)

Daftar berikut dikumpulkan dari temuan nyata penugasan pengawasan lapangan yang sering lolos beberapa putaran pemolesan LLM dan baru tertangkap saat reviu pengendali teknis. Wajib dieliminasi atau disubstitusi:

| Penanda AI | Contoh Keluaran Robotik | Perbaikan Standar Auditor BPKP |
| :--- | :--- | :--- |
| `turut + verba` | "kendala anggaran *turut menyulitkan* distribusi pupuk", "literasi *turut menghambat*" | Hapus "turut", gunakan verba langsung lugas: "menyulitkan", "menghambat" |
| `nyaris tidak` | "Pemda *nyaris tidak memiliki* pilihan rekanan penyedia" | "hampir tidak memiliki pilihan rekanan" atau "terbatas dalam memilih rekanan" |
| `tercermin dari` | "kondisi ini *tercermin dari* data realisasi serapan" | Hubungkan langsung: "fakta tersebut dibuktikan oleh data realisasi serapan" atau pecah kalimat |
| `telah terpetakan` | "jumlah unit sasaran *telah terpetakan*" | "sudah teridentifikasi dalam data" atau "telah dihimpun" |
| `menyimpan risiko` | "mekanisme ini *menyimpan risiko* penyimpangan" | "berisiko menimbulkan penyimpangan" (risiko bukan barang yang disimpan) |
| `perlu diwaspadai` | "beberapa celah pengendalian *perlu diwaspadai*" | "merupakan celah pengendalian yang perlu diuji dan dimitigasi" |
| `perlu dilakukan` | "Langkah selanjutnya yang *perlu dilakukan* Kepala Dinas adalah" | "Langkah perbaikan bagi Kepala Dinas adalah" atau gunakan kalimat aktif rekomendasi |
| Kata ganda satu klausa | "Sebagian sasaran bantuan *telah terealisasi sebagian*" | Pecah kontras: "Sebanyak X sasaran telah terealisasi; sisanya Y sasaran belum: ..." |
| Kolon dramatis | "berjalan lambat: 77,17% unit belum tuntas" | "belum berjalan sesuai jadwal. Hambatan utama ditunjukkan oleh 77,17% unit yang belum tuntas" |
| Keterangan menumpuk sebelum subjek | "Berdasarkan KAP dan arahan pimpinan, unit kerja bertugas melaksanakan" | "Sesuai KAP, unit kerja bertugas melaksanakan..." |

> [!tip] Kosakata Formal Kedinasan yang DILARANG Dihapus
> Kata formal baku seperti **"merupakan"**, **"menunjukkan"**, **"bertujuan"**, dan **"guna memastikan"** adalah kosakata baku naskah dinas resmi dan pedoman pengawasan BPKP. **JANGAN PERNAH** menghapus atau mengganti kata-kata tersebut hanya karena dicurigai sebagai teks bot!

### 7.2 Konversi Penanda Miring Markdown ke Run Italic Asli (Mencegah Kebocoran Asterisk)

Output sub-agent LLM sering memakai penanda markdown `*kata*` atau `_kata_`. Jika teks tersebut ditanam langsung ke docx atau Google Docs sebagai string, tanda bintang/garis bawah tercetak mentah/literal (misalnya: `"kebutuhan riil perumahan (*backlog*)"` tercetak dengan karakter bintang).

**Aturan Penanganan Mutlak:**
1. Sebelum teks narasi ditanam ke docx, konversi penanda markdown menjadi run native OpenXML dengan properti `run.italic = True` (font Arial 12pt).
2. Modul `bpkp_docx_engine.py` telah dilengkapi fitur otomatis: fungsi `add_p()` otomatis mendeteksi penanda `*`, `**`, `<i>`, atau `<b>` dan memecahnya menjadi run native tanpa tanda bintang mentah.
3. Gunakan helper `add_runs_with_markdown()` atau `add_runs_with_italic()` saat mengisi teks secara manual per sel/paragraf.
4. **Invarian Audit**: Jumlah karakter literal `*` pada seluruh teks dokumen hasil kompilasi **WAJIB 0**.

### 7.3 Audit Deterministik Wajib Pra-Selesai (Invarian Mutlak)

Sebelum menyatakan dokumen laporan (LHP, LHE, LHR, Notisi) selesai, jalankan fungsi audit deterministik `audit_docx_deterministic(doc)` atau `audit_text_deterministic(teks)`. Dokumen hanya dapat diserahkan jika memenuhi:
- [ ] **Jumlah em dash / en dash (`—`, `–`, `--`) = 0**.
- [ ] **Jumlah literal asterisk (`*`) = 0**.
- [ ] **Temuan penanda AI lapangan = 0** (`turut + verba`, `nyaris`, `tercermin dari`, `telah terpetakan`, `menyimpan risiko`, `perlu diwaspadai`, `perlu dilakukan`).
- [ ] **Panjang kalimat**: Kalimat dengan $>60$ kata dievaluasi untuk dipecah (kecuali kalimat tabel deret angka).

---

## 8. Pemeriksaan EYD V (Built-In)

Setelah humanisasi, periksa ejaan sesuai kaidah EYD V (Ejaan Bahasa Indonesia yang Disempurnakan Edisi V). DILARANG mengubah nama diri, istilah merek, kutipan langsung regulasi, kode, URL, rumus, atau slogan tanpa instruksi spesifik.

### Pemeriksaan Berurutan

#### A. Penggunaan Huruf

**Huruf Kapital:**
- Jabatan/Gelar: Kapital jika diikuti nama diri (*Presiden Joko Widodo*, *Gubernur Jawa Barat*). Kecil jika tidak diikuti nama (*menjadi seorang presiden*, *calon gubernur*).
- Geografis: Kapital jika spesifik/nama diri (*Danau Toba*, *Kecamatan Menteng*). Kecil jika generik/nama jenis (*berenang di danau*).
- Nama Bangsa/Suku/Bahasa: Kapital (*bahasa Indonesia*, *suku Dayak*).

**Huruf Miring:**
- Istilah/kata asing atau bahasa daerah yang belum diserap (*online*, *drive-thru*).
- Judul buku, majalah, atau surat kabar yang dikutip dalam kalimat.

**Huruf Tebal:**
- Menegaskan bagian tulisan yang sudah dimiringkan, serta judul bab/subbab.

#### B. Penulisan Kata

**Kata Depan vs Imbuhan:**
- Kata Depan (`di`, `ke`, `dari`): Dipisah jika menunjukkan tempat/arah/waktu (*di rumah*, *ke mana*, *dari Surabaya*).
- Imbuhan (`di-`, `ke-`): Disambung jika membentuk kata kerja pasif atau kata bilangan (*ditulis*, *dimakan*, *ketiga*).

**Bentuk Terikat (`pasca-`, `sub-`, `non-`, `anti-`, `antar-`):**
- Disambung dengan kata yang mengikutinya (*pascabencana*, *antarkota*, *nonaktif*).
- Tanda hubung jika diikuti kata berawalan kapital atau angka (*non-Indonesia*, *pro-IKN*).

**Bentuk Terikat `maha-`:**
- Disambung jika diikuti kata dasar mengacu Tuhan (*Mahakuasa*, *Mahatahu*). Pengecualian: *Maha Esa*.
- Dipisah jika diikuti kata berimbuhan (*Maha Pengasih*, *Maha Pemurah*).

**Partikel `pun`:**
- Dipisah jika bermakna "juga" (*apa pun*, *saya pun*, *siapa pun*).
- Disambung pada kata klise: *adapun*, *ataupun*, *bagaimanapun*, *biarpun*, *kalaupun*, *kendatipun*, *maupun*, *meskipun*, *sungguhpun*, *walaupun*, *sekalipun*.

**Singkatan dan Akronim:**
- Singkatan umum 3 huruf kecil diakhiri 1 titik (*dll.*, *dsb.*, *hlm.*, *yth.*).
- Singkatan umum 2 huruf kecil menggunakan titik di tiap huruf (*a.n.*, *d.a.*, *s.d.*, *u.p.*).
- Akronim nama diri menggunakan kapital tanpa titik (*BPKP*, *SAIPI*, *AAIPI*).

**Angka dan Bilangan:**
- Ditulis huruf jika satu atau dua kata (*tiga kali*, *dua puluh orang*).
- Ditulis digit untuk rincian, ukuran, nilai uang, waktu (*5 cm*, *Rp50.000,00*, *pukul 08.00*).

#### C. Penggunaan Tanda Baca

**Tanda Koma (`,`) & Kaidah Konjungsi Koordinatif:**
- Sebelum konjungsi pertentangan (*..., tetapi...*, *..., melainkan...*, *..., sedangkan...*).
- **Aturan Koma Perincian**:
  - **2 Unsur**: **TIDAK** menggunakan koma sebelum konjungsi (*"Kepala Perwakilan dan Pengendali Teknis memimpin rapat"*, BUKAN *"..., dan Pengendali Teknis..."*).
  - **> 2 Unsur (Perincian $\ge 3$)**: **WAJIB** menggunakan tanda koma sebelum konjungsi terakhir (*Oxford comma* versi EYD V: *"kriteria, penyebab, dan akibat"*; *"KPA, PPK, serta Bendahara Pengeluaran"*).
- **Kaidah Pemilihan "Dan" vs "Serta"**:
  - Gunakan **"dan"** untuk relasi penambahan murni yang setara secara kedudukan/bobot (*"Kondisi dan Kriteria"*, *"pemeriksaan fisik dan konfirmasi pihak ketiga"*).
  - Gunakan **"serta"** untuk relasi penyertaan/pendampingan (bermakna *beserta*, *ikut*, *turut*, atau berkas/pihak pelengkap pendamping: *"Gubernur serta jajarannya"*, *"dokumen kontrak serta lampiran Berita Acara"*).
  - **Perincian Bertingkat (Hierarkis)**: Gunakan **"dan"** untuk kelompok utama yang setara dan **"serta"** untuk kelompok pendamping/tambahan (*"Dinas Pertanian dan Dinas Ketahanan Pangan, serta perwakilan kelompok tani"*).
- **Larangan Pleonasme**: **DILARANG KERAS** menggunakan gabungan *"dan serta"* secara berdampingan tanpa jeda struktur (*"peralatan dan serta bahan"* -> **SALAH**, perbaiki menjadi *"peralatan dan bahan"* atau perinci dengan koma).
- Di belakang kata transisi antarkalimat (*Oleh karena itu, ...*, *Namun, ...*).
- Anak kalimat mendahului induk kalimat: pakai koma (*Jika hujan, saya tidak datang*). Sebaliknya, tanpa koma.

**Tanda Titik Dua (`:`):**
- Di akhir pernyataan lengkap yang diikuti rincian.
- TIDAK jika rincian merupakan pelengkap langsung kalimat.

**Tanda Hubung (`-`):**
- Kata ulang (*anak-anak*), `ke-` + angka (*ke-2*), angka + `-an` (*tahun 1990-an*), imbuhan + kata asing (*di-upgrading*).

**Eliminasi Tanda Pisah (Em Dash `—` / `--`):**
- **DILARANG KERAS** menggunakan tanda pisah (*em dash* `—` atau tanda hubung ganda `--`) dalam naskah dinas, laporan pengawasan, notisi, simpulan, maupun rekomendasi BPKP.
- Tanda pisah merupakan artefak khas terjemahan mentah dan luaran model AI yang tidak lazim dalam ragam bahasa birokrasi/audit Indonesia formal.
- **Substitusi Wajib**:
  1. Gunakan tanda koma (`,`) untuk klausa selaan sederhana.
  2. Gunakan tanda kurung (`(...)`) untuk rincian teknis pelengkap.
  3. Gunakan kata "sampai dengan" (atau singkatan baku `s.d.`) untuk rentang angka/tanggal (*tahun 2024 s.d. 2026*, bukan *2024—2026*).
  4. Restrukturisasi kalimat majemuk menjadi kalimat lugas aktif berurutan.

**Tanda Petik (`"..."`):**
- Mengapit petikan langsung. Titik/koma penutup di **dalam** tanda petik.

#### D. Unsur Serapan

**Penyesuaian Akhiran Asing:**
- *-ism* -> *-isme*, *-ty* -> *-tas*, *-tion* -> *-si*, *-logy* -> *-logi*, *-ive* -> *-if*, *-ic* -> *-ik*

**Konsonan Ganda:**
- Diserap menjadi tunggal (*effect* -> *efek*, *commission* -> *komisi*).

### Verifikasi Kasus Batas

Jika aturan EYD diragukan atau terdapat kata serapan yang berpotensi diperdebatkan, gunakan `webfetch` ke URL spesifik dari situs resmi EYD V:
- Situs utama: <https://ejaan.kemendikdasmen.go.id/eyd/>
- Huruf Kapital: <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-huruf/huruf-kapital/>
- Kata Depan: <https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/kata-depan/>
- Singkatan dan Akronim: <https://ejaan.kemendikdasmen.go.id/eyd/penulisan-kata/singkatan-dan-akronim/>
- Tanda Koma: <https://ejaan.kemendikdasmen.go.id/eyd/penggunaan-tanda-baca/tanda-koma/>
- Unsur Serapan Umum: <https://ejaan.kemendikdasmen.go.id/eyd/unsur-serapan/umum/>
- Unsur Serapan Khusus: <https://ejaan.kemendikdasmen.go.id/eyd/unsur-serapan/khusus/>

### Batas Penyuntingan EYD
- Jangan mengubah kutipan langsung regulasi kecuali diminta.
- Jangan mengganti istilah teknis audit/pemerintahan hanya karena terasa asing; verifikasi konteksnya.
- Jika EYD V membolehkan variasi, pilih satu bentuk dan terapkan secara konsisten di seluruh dokumen.

---

## 9. Alur Kerja (Workflow)

### Langkah 1: Identifikasi Jenis dan Format Laporan
Tanyakan kepada pengguna jika belum jelas:
- Jenis laporan (LHP / LHE / LHR / lainnya)
- Objek pengawasan
- Periode pengawasan
- Perwakilan BPKP pelaksana
- **Apakah sudah ada template laporan yang harus diikuti?** Jika ya, minta template-nya. Jika template memiliki placeholder, tanyakan apakah data pengisinya berasal dari kertas kerja xlsx.

### Langkah 2: Kumpulkan Data
- Minta data temuan, bukti audit, dan regulasi terkait.
- Jika pengguna memberikan data mentah (dari kertas kerja xlsx atau sumber lain), bantu menyusunnya ke dalam kerangka 5C.
- Jika data berasal dari file xlsx, minta pengguna membaca xlsx menggunakan skill/alat terpisah terlebih dahulu, atau berikan data dalam format yang bisa dibaca.

### Langkah 3: Susun Draf
- Jika ada template: ikuti template. Isi placeholder dengan data yang diperoleh.
- Jika tidak ada template: gunakan contoh di references sebagai titik awal, sesuaikan dengan jenis penugasan.
- Untuk setiap temuan, terapkan kerangka 5C (Bagian 3).
- Terapkan ketentuan tata naskah dinas laporan (Bagian 11): bentuk surat/bab, penomoran LHP/LPP, cover, dan penanda tangan sesuai wewenang.
- Pastikan simpulan konsisten dengan uraian temuan.
- Pastikan rekomendasi konsisten dengan uraian temuan.

### Langkah 4: Validasi Kelengkapan
Periksa bahwa laporan memuat (sesuaikan dengan jenis laporan):
- [ ] Klausul distribusi terbatas
- [ ] Conformance statement (pernyataan pemenuhan norma)
- [ ] Kerangka 5C untuk setiap temuan (Condition, Criteria, Cause, Consequence)
- [ ] Identifikasi risiko dan rekomendasi per topik
- [ ] Kutipan regulasi lengkap (nama, nomor, tahun, pasal, ayat)
- [ ] Tabel dengan judul dan sumber
- [ ] Singkatan dieja lengkap pada kemunculan pertama
- [ ] Konsistensi antara simpulan dan uraian temuan
- [ ] Konsistensi antara rekomendasi ringkas dan rekomendasi detail
- [ ] Penomoran memakai kode `LHP`/`LPP` sesuai format TND (Bagian 11.4)
- [ ] Penanda tangan sesuai wewenang: kepala unit kerja/Pejabat Berwenang untuk laporan hasil pengawasan; kepala unit kerja/Plh. untuk laporan berkala penunjang (Bagian 11.2)
- [ ] Cover memenuhi spesifikasi logo BPKP 3,4 x 1,7 cm, Arial 13-bold lembaga, nama unit kerja kapital Arial 12-bold (Bagian 11.6), bila laporan dicetak bercover

### Langkah 5: Penyuntingan Bahasa
Setelah substansi final, lakukan dua tahap secara berurutan:

1. **Humanisasi bahasa** (Bagian 7):
   - Periksa dan perbaiki kalimat mekanis, struktur berulang, dan artefak chatbot.
   - Pastikan teks terasa ditulis auditor profesional untuk pembaca spesifik.
   - Pertahankan semua fakta, angka, kutipan regulasi, dan istilah teknis.

2. **Pemeriksaan EYD V** (Bagian 8):
   - Periksa huruf kapital, kata depan vs imbuhan, tanda baca, singkatan, dan unsur serapan.
   - Pertahankan istilah teknis audit/pemerintahan yang baku.
   - Verifikasi ke situs resmi EYD V jika ada kasus batas.

### Langkah 6: Pengecekan Akhir
- Pastikan konsistensi penomoran di seluruh dokumen.
- Pastikan konsistensi simpulan - uraian - rekomendasi.
- Laporkan kepada pengguna jika ditemukan inkonsistensi.

## 10. Interaksi dengan Pengguna

- Jika pengguna memberikan data temuan mentah tanpa kerangka 5C, susun ke dalam format 5C dan konfirmasi sebelum finalisasi.
- Jika regulasi yang dikutip pengguna tidak lengkap (tanpa pasal/ayat), tanyakan detailnya.
- Jika diminta menulis satu bagian saja (misal: hanya temuan, hanya rekomendasi), tetap ikuti format yang relevan dari bagian tersebut.
- Jika diminta mengedit laporan yang sudah ada, fokus pada perbaikan substansi (kelengkapan 5C) dan bahasa, tanpa mengubah fakta/data yang sudah ada.
- Jika pengguna memberikan template dengan placeholder, tanyakan sumber data pengisi (umumnya dari kertas kerja xlsx).

---

## 11. Ketentuan Tata Naskah Dinas untuk Laporan (Peraturan BPKP 4/2026)

Bagian ini built-in dari **Peraturan BPKP Nomor 4 Tahun 2026 tentang Tata Naskah Dinas** (BAB V-C.5 Laporan, BAB III Pejabat Penanda Tangan, BAB IV Pengamanan, BAB II Pembuatan). Menggantikan ketentuan lama dari Perban 4/2022 (dicabut pada saat Peraturan 4/2026 mulai berlaku). Berlaku untuk semua laporan yang dihasilkan dalam penugasan pengawasan.

> [!note] Perubahan Pokok pada Laporan (Perban 4/2022 → Peraturan 4/2026)
> - **Struktur**: Laporan kini diatur di **BAB V-C.5** (bukan Lampiran BAB II), tergabung dalam Naskah Dinas Khusus.
> - **Klasifikasi Laporan Hasil Pengawasan disederhanakan** dari 18 jenis → **4 kategori umum**: (a) asurans, (b) konsultansi, (c) lainnya, (d) laporan eksekutif. Susunan batang tubuh mengacu Peraturan BPKP tentang Manajemen Penugasan Pengawasan.
> - **Laporan Penunjang Pengawasan disederhanakan** dari 12 jenis → **contoh umum**: (a) monitoring tindak lanjut, (b) pengelolaan BMN, (c) progres penugasan, (d) pelaksanaan kegiatan.
> - **Ketentuan baru**: Laporan hasil penugasan Pengawasan yang distribusikan kepada klien/entitas mitra **wajib disertai surat dinas** yang ditandatangani pejabat berwenang.
> - **Ketentuan baru**: Pada halaman terakhir laporan hasil pengawasan wajib ditambahkan **catatan kaki** mengenai diksi/kalimat yang menunjukkan tugas dilakukan tanpa melanggar peraturan, serta layanan pengaduan gratifikasi dan suap.
> - **Cover laporan**: Spesifikasi logo BPKP dinyatakan dalam satuan **mm** (34 mm x 17 mm) bukan cm (sebelumnya 3,4 cm).

### 11.1 Pengelompokan Laporan

**a. Laporan hasil pengawasan** (BAB V-C.5.a.1)) pada umumnya merupakan laporan yang dihasilkan dari penugasan pengawasan dan disampaikan kepada klien/entitas mitra. Susunan batang tubuh memuat materi komunikasi hasil pengawasan sesuai **Peraturan BPKP tentang Manajemen Penugasan Pengawasan**. Antara lain:
1) Laporan hasil pengawasan asurans;
2) Laporan hasil pengawasan konsultansi;
3) Laporan hasil pengawasan lainnya; dan
4) Laporan eksekutif.

> [!note] Perubahan
> Perban 4/2022 sebelumnya mengelompokkan 18 jenis laporan hasil pengawasan spesifik (Audit Operasional, Audit Kinerja, dll.). Peraturan 4/2026 menyederhanakan menjadi 4 kategori umum. Daftar laporan spesifik sebelumnya (Audit Operasional, Audit Investigatif, Laporan Keterangan Ahli, Evaluasi Hambatan, Reviu, Bimtek, Sosialisasi, Hasil Kajian, Pembinaan SPIP, Manajemen Risiko, GCG, Pembinaan APIP, Pembinaan JFA, Pengawasan dan Pembinaan) dapat tetap dipakai sebagai panduan non-normatif sepanjang relevan, tetapi rujukan formal mengikuti 4 kategori di atas.

**b. Laporan penunjang pengawasan** (BAB V-C.5.a.2)) merupakan laporan yang dihasilkan untuk menunjang pelaksanaan penugasan pengawasan. Contohnya:
1) Laporan monitoring tindak lanjut pengawasan;
2) Laporan pengelolaan BMN;
3) Laporan progres penugasan; dan
4) Laporan pelaksanaan kegiatan.

### 11.2 Wewenang Penciptaan dan Penandatanganan

| Jenis laporan | Penanda tangan |
|---|---|
| Laporan hasil pengawasan | Kepala unit kerja atau Pejabat yang Berwenang |
| Laporan berkala penunjang pengawasan | Kepala unit kerja atau pelaksana harian (Plh.) kepala unit kerja |

### 11.3 Bentuk dan Susunan

- Laporan dapat disampaikan dalam **bentuk panjang** (laporan disampaikan secara rinci dalam bentuk BAB) ataupun **bentuk pendek** (laporan disampaikan secara ringkas dalam bentuk surat) sesuai kebutuhan.
- Susunan laporan hasil pengawasan dan laporan penunjang pengawasan diatur dalam **pedoman/petunjuk teknis** yang diterbitkan secara khusus oleh unit kerja terkait. Contoh susunan dan bentuk laporan dalam Peraturan Badan ini dapat menjadi acuan, namun dapat disesuaikan dengan kebutuhan sepanjang tetap berpedoman pada standar dan ketentuan peraturan perundang-undangan -- konsisten dengan prinsip "struktur tidak baku" pada Bagian 2 skill ini.

**Struktur Laporan Bentuk Surat (Pendek)** — terdiri atas kepala, batang tubuh, dan kaki:
- **Kepala**: kop Naskah Dinas jabatan Kepala/wakil kepala, atau kop Naskah Dinas instansi (dengan alamat) untuk yang ditandatangani selain Kepala/wakil kepala; nomor, lampiran, dan hal di kiri bawah kop; tanggal penciptaan di kanan atas sejajar nomor; kata "Yth." di bawah "Hal" diikuti nama jabatan tujuan; alamat surat (nama kota tujuan) di bawah "Yth.".
- **Batang tubuh**: pendahuluan (penjelasan umum, maksud-tujuan, ruang lingkup, sistematika); materi laporan (kegiatan, faktor, hasil, hambatan, hal lain); simpulan dan saran; penutup (harapan/permintaan arahan/ucapan terima kasih).
- **Kaki**: tanggal pembuatan laporan; nama jabatan (kapital awal kata, diakhiri koma, rata kiri); tanda tangan pejabat (atau "Ditandatangani secara elektronik oleh" + kode QR bila TTE); nama lengkap pejabat (kapital awal kata, tanpa gelar dan NIP); cap dinas hanya untuk tanda tangan basah; tembusan (jika ada).

**Struktur Laporan Bentuk Bab (Panjang)** — mengikuti sistematika BAB yang diatur dalam pedoman/petunjuk teknis unit kerja.

### 11.4 Penomoran Laporan

Laporan menggunakan kode jenis naskah dinas pada nomor:
- `LHP` -- Laporan Hasil Pengawasan
- `LPP` -- Laporan Penunjang Pengawasan

Format nomor mengikuti pola umum TND: `[kode keamanan]/[kode klasifikasi arsip]/[LHP|LPP]/[nomor urut]/[kode konseptor]/[tahun]`. Nomor urut agenda dimulai dari 1 setiap awal tahun. Khusus naskah peraturan tidak memakai pola ini, tetapi laporan tetap memakai pola lengkap.

### 11.4a Ketentuan Pengisian Nomor dan Tanggal pada Draf Laporan

> [!important] Invarian Wajib: Jangan Isi Nomor & Tanggal Laporan (Cukup Placeholder `"   "`)
> - Ketika membuat laporan atau draf laporan hasil pengawasan (LHP, LHE, LHR, maupun laporan bentuk surat pendek), **nomor laporan dan tanggal laporan JANGAN DIISI** (dilarang mengarang nomor, menebak nomor agenda, atau mencantumkan tanggal saat ini/asumsi).
> - Cukup diisi dengan placeholder `"   "` (tripel spasi kosong) saja.
> - **Alasan Operasional**: Penomoran buku agenda naskah dinas keluar dan penetapan tanggal resmi penandatanganan sepenuhnya merupakan wewenang dan dilakukan oleh **sekretaris / unit tata usaha persuratan** saat naskah siap ditandatangani dan didistribusikan.
> - Ketentuan ini berlaku konsisten pada seluruh komponen laporan:
>   1. **Sampul / Cover Laporan**: Bagian nomor dan tanggal laporan cukup diisi placeholder `"   "`.
>   2. **Metadata Surat Pengantar**: Baris `Nomor    :` diisi `"   "`, dan kolom tanggal surat pengantar diisi `"   "`.
>   3. **Kaki Laporan / Blok Tanda Tangan**: Baris tanggal penandatanganan cukup diisi `"   "` (atau nama kota saja tanpa tanggal definitif, mis. `Nabire,              2026` atau `"   "`).

### 11.5 Distribusi Laporan

- Laporan didistribusikan kepada **pihak yang berkepentingan** dan dapat berupa softcopy yang **disertai surat pengantar**.
- **Ketentuan baru (Peraturan 4/2026)**: Laporan hasil penugasan Pengawasan yang distribusikan kepada klien/entitas mitra **wajib disertai dengan surat dinas** yang ditandatangani oleh pejabat yang berwenang.
- Distribusi tetap tunduk pada prinsip distribusi terbatas (Bagian 4) dan klasifikasi keamanan: Sangat Rahasia (`SR`), Rahasia (`R`), Terbatas (`T`), Biasa (tanpa kode).

### 11.5a Catatan Kaki Etika & Layanan Pengaduan (BARU)

**Ketentuan baru (Peraturan 4/2026, BAB V-C.5.c.5))**: Dalam laporan hasil pengawasan ditambahkan pada **halaman terakhir bagian catatan kaki** mengenai:
1. Diksi/kata atau kalimat yang menunjukkan bahwa tugas yang diemban dilakukan dengan **tidak melanggar ketentuan peraturan perundang-undangan**;
2. Layanan pengaduan apabila terdapat pegawai BPKP dalam melaksanakan tugas menerima/meminta **gratifikasi dan suap**.

### 11.6 Sampul/Cover Laporan

1. Kertas hard cover jenis **buffalo** atau kertas lain dengan spesifikasi lebih tinggi sesuai keperluan.
2. Batas/ruang tepi atas, bawah, kiri, dan kanan cover laporan mengikuti aturan penyusunan Naskah Dinas dengan memperhatikan estetika.
3. Susunan cover (BAB V-C.5.b.1)):
   a. **Logo BPKP berwarna** diletakkan di bagian atas secara simetris; ukuran panjang **34 mm** dan tinggi **17 mm**, dengan proporsi panjang dan tinggi **2:1**;
   b. Tulisan **"BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN"** (jenis huruf **Arial ukuran 13 dicetak tebal**) dan diletakkan secara simetris di bawah logo BPKP;
   c. **Nama unit kerja** ditulis seluruhnya dengan huruf kapital (jenis huruf **Arial ukuran 12 dicetak tebal**) dan diletakkan secara simetris di bawah tulisan "BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN";
   d. **Judul laporan** dapat ditulis dengan penggunaan huruf kapital, kursif, font, ukuran, dan warna yang beragam untuk mendukung estetika;
   e. **Nomor dan tanggal laporan**: Pada pembuatan draf laporan, nomor dan tanggal laporan **jangan diisi**, cukup diisi placeholder `"   "` (tripel spasi kosong) karena penomoran dilakukan oleh sekretaris. Dapat diformat dengan penggunaan huruf kapital, kursif, font, ukuran, dan warna yang beragam untuk mendukung estetika saat nomor definitif diisi nantinya.

> [!note] Perubahan Satuan Logo
> Peraturan 4/2026 menyatakan ukuran logo dalam satuan **mm** (34 mm × 17 mm) bukan cm (3,4 cm × 1,7 cm). Nilai numeriknya setara; satuan resmi kini mm.

### 11.7 Media Penyajian Visual

1. Untuk stakeholder dengan pertimbangan tertentu, laporan boleh disajikan dengan media informasi yang disajikan secara visual (desain grafis, infografis, dan sebagainya) dalam format berbeda dengan Tata Naskah Dinas.
2. Format berbeda tersebut **tetap wajib** memuat: logo dan nama BPKP, nomor Naskah Dinas, dan pejabat penanda tangan, dengan memperhatikan estetika dan etika.
3. Pengaturan warna sampul laporan, gambar, dan infografis yang dapat mendukung estetika serta informasi yang disajikan dapat ditentukan oleh masing-masing unit kerja dengan tetap memperhatikan etika penyajian informasi/gambar/infografis yang berlaku.

### 11.8 Unsur Pokok Naskah Dinas (untuk laporan bentuk surat)

Kop naskah dinas; nomor; lampiran; hal/perihal; tanggal; alamat tujuan; salam pembuka; isi (pembuka--inti--penutup); salam penutup; nama jabatan penanda tangan; nama pejabat (tanpa gelar dan NIP, Peraturan BPKP 4/2026 Bagian II tentang ruang tanda tangan); tembusan (bila ada); tanda tangan dan nama terang; nomor halaman; lampiran.

---

## 12. Standar Formatting, Indentasi, & Tata Naskah Dinas Word (docx)

Berdasarkan praktik terbaik dan standardisasi penyusunan laporan pengawasan (LHE/LHP) BPKP, berikut adalah aturan teknis formatting, hierarki indentasi, tabel, dan tipografi Word (docx) yang wajib dipatuhi:

### 12.1 Pengaturan Halaman & Tipografi
- **Ukuran Kertas & Ruang Tepi:** Kertas A4 (21,0 cm x 29,7 cm). Batas minimum ruang tepi (Peraturan BPKP 4/2026 Bagian II.E, bersifat fleksibel): atas 10 mm bila berkop / paling kurang 20 mm tanpa kop atau halaman berikutnya; **bawah paling kurang 25 mm**; kiri paling kurang 30 mm (media kertas) / 20 mm (elektronik); kanan paling kurang 20 mm. Preset engine (`create_document`): kiri 3,0 cm, kanan 2,0 cm, atas 2,0 cm, bawah 2,5 cm.
- **Font:** Naskah dinas memakai **Arial ukuran 11 atau 12** (Peraturan BPKP 4/2026 Bagian II.D.2; laporan pada skill ini memakai 12), konsisten di seluruh elemen (heading, paragraf, tabel, nomor, header, footer). Pada OpenXML Word pastikan seluruh *runs* menyertakan:
  `<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/>`
- **Ukuran Font:**
  - Judul Cover Utama: Arial 14–16 pt Bold
  - Tulisan Lembaga Cover: "BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN" Arial 13 pt Bold, Nama Perwakilan/Deputi Arial 12 pt Bold
  - Judul BAB (`Heading 1`): Arial 12 pt Bold, Rata Tengah (Center), Spasi Atas 12 pt, Spasi Bawah 6 pt
  - Bagian BAB (`Heading 2` & `Heading 3`): Arial 12 pt Bold, Rata Kiri, Spasi Atas 12 pt, Spasi Bawah 6 pt
  - Sub-Heading Temuan (`a.`, `b.`, dst.): Arial 12 pt Bold
  - Isi Paragraf / Narasi 5C / Rincian / Nama Lokus: Arial 12 pt Regular
  - Header & Isi Tabel: Arial 10 pt (Header Bold, Isi Regular)
  - Catatan Kaki, Keterangan Sumber Tabel, Alamat Kop: Arial 9 pt Regular / Italic
- **Spasi & Perataan:**
  - Line Spacing: **1,15 line pitch** (`w:line="276" w:lineRule="auto"`).
  - Space After: **6 pt** (`w:after="120"` dxa) untuk paragraf umum; Space Before: **0 pt** (kecuali sub-heading temuan: Space Before **8 pt**, dan paragraf nama lokus: Space After **2 pt**).
  - Alignment: **100% Justified (Rata Kiri-Kanan)** untuk seluruh teks narasi, deskripsi kondisi multi-lokus, kriteria, sebab, akibat, rekomendasi, dan simpulan.

---

### 12.2 Headings Bertingkat: Style Word, Google Docs, & Markdown

Pemisahan dan penerapan *style Heading* bawaan Word / Google Docs (`Heading 1` s.d. `Heading 4`) sangat penting agar Navigation Panel (Pohon Navigasi) dan Daftar Isi (TOC) terbentuk otomatis dan utuh hingga level sub-temuan spesifik.

> [!important] KEHARUSAN PENERAPAN HEADING BERTINGKAT (MARKDOWN & DOKUMEN OFFICE)
> AI Asisten dan penyusun naskah **WAJIB** menerapkan struktur heading bertingkat secara hierarkis dan konsisten pada setiap draf narasi, baik luaran teks/markdown maupun dokumen DOCX/Google Docs.
> **DILARANG** menyajikan judul bab/bagian/topik hanya sebagai teks biasa yang ditebalkan (`**tebal**`) tanpa penanda heading!

#### A. Dua Skema Hierarki Heading Resmi BPKP

1. **Skema 1: Laporan Hasil Pengawasan Bab Panjang (LHP / LHE / LHR)**
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

2. **Skema 2: Notisi Hasil Pengawasan & Naskah Dinas Khusus**
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

**Aturan Format dan Font pada Heading:**
- **Heading 1/2/3/4 (style Word & Docs):** Font Arial 12 pt Bold Hitam (`#000000`) konsisten pada seluruh level.
- **Line break pada Heading 1:** Judul bab dan nama bab disatukan dalam satu paragraf heading dengan line break (`\n`), misalnya: `BAB I\nSIMPULAN DAN REKOMENDASI`, agar di panel navigasi dan TOC terbaca sebagai satu kesatuan tajuk.
- **Sub-Heading Temuan (`a.`, `b.`):** Gunakan `Heading 4` / `####`. Seluruh teks judul sub-heading adalah Bold 12pt.
- **Paragraf narasi 5C (Kondisi, Kriteria, Sebab, Akibat, Rekomendasi):** Regular 12 pt (tidak ada Bold).
- **Nama Lokus pada rincian multi-lokus:** Regular 12 pt — berdiri sebagai sub-heading bernomor pada paragraf tersendiri, diikuti narasi pada paragraf terpisah di bawahnya.
- **Judul Butir pada detail item (`a)`):** Bold 12 pt — hanya judul butir yang Bold; titik dua dan isi Regular.

> **Catatan pengalaman:** Spesifikasi awal (`file.md`) menetapkan teks isi 11 pt dan heading 12 pt. Namun dalam implementasi kode, seluruh teks diseragamkan menjadi **12 pt** untuk konsistensi dan kesederhanaan. Standar 12 pt seragam ini yang digunakan sebagai acuan praktis.

### 12.3 Sistem Tab Stop & Hierarki Indentasi Presisi (Hanging Indent Cascade)

Sistem indentasi menggunakan prinsip **cascade**: posisi nomor setiap level berhimpit (sejajar) dengan posisi awal teks pada level di atasnya. Jarak antar level = 360 dxa (0,25"). Formula ini memastikan hierarki visual yang konsisten dan mencegah kerusakan tata letak saat kalimat terbungkus ke baris kedua (*line wrapping*).

#### Formula Cascade (dxa = twips, 1440 dxa = 1 inci)

| `ilvl` | Format | Nomor di (dxa) | Teks di (dxa) | `w:ind w:left` | `w:ind w:hanging` | `w:tab w:pos` |
|---|---|---|---|---|---|---|
| 0 | `A.` | 360 | 720 | 720 | 360 | 720 |
| 1 | `1.` | 720 | 1080 | 1080 | 360 | 1080 |
| 2 | `a.` | 1080 | 1440 | 1440 | 360 | 1440 |
| 3 | `1)` | 1440 | 1800 | 1800 | 360 | 1800 |
| 4 | `a)` | 1800 | 2160 | 2160 | 360 | 2160 |

> **Konversi ke inci:** 360 dxa = 0,25" | 720 = 0,50" | 1080 = 0,75" | 1440 = 1,00" | 1800 = 1,25" | 2160 = 1,50"

#### Penempatan Level pada Konteks Laporan

| Level / Elemen | `ilvl` | Left Indent | First Line (Hanging) | Tab Stop | Perataan & Gaya Font |
|---|---|---|---|---|---|
| **Topik Utama (`Heading 3`)** | 1 | `0,75"` (1080 dxa) | `-0,25"` (-360 dxa) | `1080 dxa` | Left, Arial 12 pt Bold |
| **Simpulan Topik** (paragraf pembuka) | — | `0,75"` (1080 dxa) | `0,00"` | — | Justified, Arial 12 pt Regular |
| **Sub-Heading Temuan** (`a.`, `b.`) | 2 | `1,00"` (1440 dxa) | `-0,25"` (-360 dxa) | `1440 dxa` | Justified, Arial 12 pt **Bold** |
| **Pengantar Kondisi** ("Kondisi di tingkat...") | — | `1,00"` (1440 dxa) | `0,00"` | — | Justified, Arial 12 pt Regular |
| **Rincian Lokus** (`1)`, `2)`) | 3 | `1,25"` (1800 dxa) | `-0,25"` (-360 dxa) | `1800 dxa` | Justified, Arial 12 pt Regular |
| **Detail Item** (`a)`, `b)`) | 4 | `1,50"` (2160 dxa) | `-0,25"` (-360 dxa) | `2160 dxa` | Justified, Arial 12 pt Regular |
| **Kriteria / Penyebab / Akibat / Rekomendasi** | — | `1,25"` (1800 dxa) | `0,00"` | — | Justified, Arial 12 pt Regular |

> **Catatan notasi:** Tabel *Formula Cascade* di atas menggunakan notasi numbering.xml `w:ind left` (posisi teks), sedangkan kolom "Nomor di" di tabel formula adalah posisi awal nomor. Tabel *Penempatan Level* di bawah menggunakan notasi paragraf manual (`Left Indent` = posisi teks; `First Line` = hanging). Kedua tabel ini ekuivalen dan saling konsisten.

#### Body Paragraf di Bawah Level Bernomor
Paragraf narasi 5C (Kriteria, Penyebab, Akibat, Rekomendasi) menggunakan **Left Indent = posisi teks level 3** (`1,25"` / 1800 dxa), **bukan** level 2. Ini sejajar dengan posisi teks rincian lokus (`1)`), karena dalam implementasi kode, fungsi `add_criteria()`, `add_cause()`, `add_effect()` menerima parameter `ilvl=3` dan mengambil `left` dari `_LEVEL_FMT[3]` yang bernilai 1800 dxa. Dengan demikian:
- Paragraf pengantar kondisi ("Kondisi di tingkat...") → Left `1,00"` (1440 dxa), sejajar dengan teks sub-heading `a.` (dari `add_body_sub` dengan `ilvl=2`)
- Paragraf Kriteria, Penyebab, Akibat, Rekomendasi → Left `1,25"` (1800 dxa), sejajar dengan teks rincian lokus `1)` (dari `add_criteria`/`add_cause`/`add_effect` dengan `ilvl=3`)

#### Rincian Lokus: Dua-Paragraf Terpisah (Mode Numbering Otomatis)

Pada mode numbering otomatis, rincian per lokus (`1)`, `2)`, `3)`) dipecah menjadi **dua paragraf terpisah**:
1. **Paragraf nama lokus (sub-heading bernomor):** Hanya berisi nama lokus (mis. `Provinsi Papua Tengah`), tanpa titik dua, tanpa narasi. Format: **Regular** (tidak Bold), 12 pt, Spasi After **2 pt** (lebih kecil dari default 6 pt, untuk merapatkan jarak ke narasi).
2. **Paragraf narasi lokus:** Berisi uraian fakta kondisi riil. Left Indent sejajar dengan teks level 3 (`1,25"` / 1800 dxa). Format: Regular 12 pt, Spasi After 6 pt.

Contoh struktur:
```
1)  Provinsi Papua Tengah          ← paragraf 1: nama lokus, Regular, spasi after 2pt
    Pemerintah Provinsi Papua Tengah belum menetapkan Perda maupun Pergub mengenai LP2B...  ← paragraf 2: narasi
2)  Kabupaten Nabire               ← paragraf 1: nama lokus
    Peraturan Daerah tentang RTRW Kabupaten Nabire belum ditetapkan...  ← paragraf 2: narasi
```

> **Pada mode manual (legacy/fallback):** Nama lokus, titik dua, dan narasi disatukan dalam satu paragraf: `1)\t[Nama Lokus]**:** [Narasi]` dengan nama lokus Bold. Mode otomatis lebih disukai karena menghasilkan struktur yang lebih bersih dan rapi.

---

### 12.3a Resep Multi-Level Numbering XML & Penyelarasan Tabel

#### A. Definisi Multi-Level XML yang Valid di Word & Google Docs
Untuk penomoran bertingkat `A. → 1. → a. → 1) → a)` yang stabil dan merender sempurna di Google Docs maupun Microsoft Word, definisi `abstractNum` wajib mematuhi formula berikut:

```xml
<abstractNum abstractNumId="1">
  <lvl ilvl="0"> <numFmt w:val="upperLetter"/> <lvlText w:val="%1."/> <lvlJc w:val="left"/> <pPr><ind w:left="720"  w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="1"> <numFmt w:val="decimal"/>     <lvlText w:val="%2."/> <lvlJc w:val="left"/> <pPr><ind w:left="1080" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="2"> <numFmt w:val="lowerLetter"/> <lvlText w:val="%3."/> <lvlJc w:val="left"/> <pPr><ind w:left="1440" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="3"> <numFmt w:val="decimal"/>     <lvlText w:val="%4)"/> <lvlJc w:val="left"/> <pPr><ind w:left="1800" w:hanging="360"/></pPr> </lvl>
  <lvl ilvl="4"> <numFmt w:val="lowerLetter"/> <lvlText w:val="%5)"/> <lvlJc w:val="left"/> <pPr><ind w:left="2160" w:hanging="360"/></pPr> </lvl>
</abstractNum>
<num numId="1"><abstractNumId w:val="1"/></num>
```

#### B. Peringatan Nilai Piksel vs DXA
Hindari nilai pembulatan piksel hasil konversi kasar (seperti 708, 1068, 1428 dxa). Seluruh nilai indentasi naskah dinas dan laporan pengawasan BPKP wajib menggunakan **kelipatan grid 360 dxa (0,25")**: `720 / 1080 / 1440 / 1800 / 2160 dxa`.

#### C. Teknik Salin-Referensi (Copy-Reference Technique)
Membangun elemen XML `numbering.xml` dan `styles.xml` mentah dari nol melalui script python sering menghasilkan dokumen yang korup atau penomoran tidak muncul di Google Docs.
**Metode Teruji dan Handal**:
Gunakan fungsi `clone_from_template("template_referensi.docx")`:
1. Salin berkas referensi DOCX yang memiliki konfigurasi style dan numbering yang valid.
2. Hapus seluruh isi tabel dan paragraf menggunakan `p._p.getparent().remove(p._p)`.
3. Tulis ulang konten laporan dengan mewarisi seluruh section properties, margins, numbering definitions, dan style heading asli.

#### D. Penyelarasan Tabel dengan Teks (Table-Text Flush Alignment)
Agar batas kiri tabel temuan sejajar lurus (*flush*) dengan indentasi teks narasi di atasnya (misal sejajar dengan sub-heading 720 dxa), terapkan helper `set_table_flush_alignment(table, left_dxa=720, total_width_dxa=8318)`. Ini menyetel:
- `<w:jc w:val="left"/>`
- `<w:tblInd w:w="720" w:type="dxa"/>` (sama persis dengan `w:ind w:left` paragraf)
- `<w:tblW w:w="8318" w:type="dxa"/>` (lebar efektif halaman minus kedua margin minus indent)

---

### 12.4 Standar Format Tabel BPKP (Clean Open-Table Style)

Tabel dalam laporan BPKP disajikan secara bersih, rapi, dan profesional dengan kaidah:
- **Borders:** Hanya menggunakan garis horizontal (Top, Bottom, dan garis pemisah header) tipis single border (`sz="4"`, warna abu-abu `#B0B0B0` atau hitam `#000000`). **DILARANG menggunakan border vertikal** (Left, Right, InsideV diset `val="none"`).
- **Cell Padding (Margin Sel):** Top/Bottom: 100 dxa (~5 pt), Left/Right: 150 dxa (~7.5 pt) agar teks tidak menempel ketat pada garis border.
- **Header Baris:** Background shading abu-abu muda (`#F2F2F2` atau `#E6E6E6`), Font Arial 10 pt Bold, Center/Left aligned, Vertically centered.
- **Isi Tabel:** Font Arial 10 pt Regular. Kolom Angka/Realisasi rata kanan (*Right-aligned*), Kolom No rata tengah (*Center*), Kolom Uraian rata kiri/justified.
- **Keterangan Sumber:** Wajib dicantumkan di bawah tabel dengan format: *Sumber: [Nama Instansi / Kertas Kerja Evaluasi], [Tahun]* (Font Arial 9 pt Italic).

---

### 12.5 Aturan Pewarnaan Font Teks & Placeholder
- **Warna MERAH (`RGB(255, 0, 0)`):** Digunakan secara khusus untuk kalimat, kata, atau paragraf yang memuat placeholder **`(.)`**, kriteria yang belum diverifikasi, atau data yang masih membutuhkan konfirmasi/draf.
- **Warna HITAM (`RGB(0, 0, 0)`):** Digunakan untuk seluruh teks/paragraf yang sudah definitif, *fixed*, dan terverifikasi dari bukti/kertas kerja pengawasan.

### 12.6 Aturan Titik Dua (`:`)

Tanda titik dua (`:`) memiliki tiga konteks penggunaan utama dalam laporan pengawasan BPKP, masing-masing dengan aturan format yang berbeda:

#### A. Titik Dua pada Metadata Kop Surat
Pada blok metadata surat pengantar (Nomor, Lampiran, Hal, Tanggal), titik dua **diletakkan tepat setelah label** tanpa spasi sebelum, lalu **satu spasi** sebelum nilai:
```
Nomor    :   
Lampiran : Satu Berkas
Hal      : Laporan Hasil Evaluasi atas Tata Kelola...
```
*(Catatan wajib: Nilai Nomor dan Tanggal pada draf laporan **jangan diisi**, cukup diisi placeholder `"   "` (tripel spasi kosong) karena penomoran dan penetapan tanggal dilakukan oleh sekretaris).*
Label rata kiri dengan padding tetap (mis. `Nomor` + spasi = 10 karakter), lalu `:`, lalu spasi, lalu nilai. Titik dua pada baris tanggal tidak digunakan (tanggal ditulis langsung).

#### B. Titik Dua pada Pengantar Daftar Bernomor
Kalimat pengantar yang diikuti daftar bernomor **wajib diakhiri titik dua** (bukan titik atau koma):
- `Kondisi di tingkat wilayah pengawasan diuraikan sebagai berikut:`
- `Atas permasalahan tersebut, direkomendasikan agar:`
- `...menyatakan sependapat dan berkomitmen menyusun rencana aksi penyelesaian tindak lanjut dengan rincian:`

Setelah titik dua, baris berikutnya langsung berisi butir daftar bernomor. Tidak boleh ada teks tambahan setelah titik dua pada baris yang sama.

#### C. Titik Dua pada Label Nama Lokus
Pada mode numbering otomatis, nama lokus **tidak menggunakan titik dua** — nama lokus berdiri sebagai sub-heading bernomor pada paragraf tersendiri (Regular, tanpa Bold, tanpa titik dua), dan narasi mengikuti pada paragraf terpisah di bawahnya.

Pada mode manual (legacy/fallback), nama lokus diikuti titik dua lalu spasi sebelum narasi dalam satu paragraf yang sama. Nama lokus **Bold**, titik dua dan narasi **Regular**:
```
1) Provinsi Papua Tengah: [narasi kondisi riil...]
2) Kabupaten Nabire: [narasi kondisi riil...]
```
Format mode manual: `[Nomor Manual]\t[Nama Lokus]**:** [Narasi Regular]`. Titik dua langsung menempel setelah nama lokus tanpa spasi sebelum, lalu satu spasi sebelum narasi.

> **Mode otomatis lebih disukai** karena menghasilkan struktur yang lebih bersih: nama lokus sebagai paragraf bernomor tersendiri, narasi sebagai paragraf terpisah di bawahnya, tanpa titik dua.

#### D. Titik Dua pada Sumber Tabel
Format keterangan sumber data di bawah tabel menggunakan titik dua setelah kata "Sumber":
```
Sumber: Dinas Pertanian Kabupaten Nabire diolah, 2026
```
Dicetak miring (*Italic*), Arial 9 pt, tanpa indentasi.

#### E. Titik Dua pada Detail Item Bernomor
Pada baris detail item (`a)`, `b)`) yang memiliki judul butir, format: `[Nomor Otomatis]\t[Judul Butir]**:** [Isi Regular]`. Titik dua menempel setelah judul butir tanpa spasi sebelum, lalu satu spasi sebelum isi.

### 12.7 Aturan Huruf Cetak Bold (Bold Font)

Bold hanya digunakan untuk elemen struktural dan penanda, **bukan** untuk menonjolkan kata atau frasa dalam narasi body. Aturan rinci:

| Elemen | Bold? | Ukuran | Keterangan |
|---|---|---|---|
| Heading 1 (Judul BAB) | Ya | 12 pt | Seluruh teks tajuk |
| Heading 2 (Bagian BAB) | Ya | 12 pt | Seluruh teks tajuk |
| Heading 3 (Topik Utama) | Ya | 12 pt | Seluruh teks tajuk |
| Sub-Heading Temuan (`a.`, `b.`) | Ya | 12 pt | Seluruh teks: nomor + judul |
| Judul Bagian Non-Temuan (mis. "Tanggapan Mitra Evaluasi...") | Ya | 12 pt | Seluruh teks tajuk |
| Nama Lokus pada rincian (`Provinsi Papua Tengah`) | **TIDAK** | 12 pt | Regular — nama lokus berdiri sebagai sub-heading bernomor pada paragraf tersendiri (mode otomatis) |
| Judul Butir pada detail item (`Risiko:`) | Ya | 12 pt | Hanya judul butir yang Bold; titik dua dan isi Regular |
| Label Metadata Kop (`Nomor`, `Lampiran`, `Hal`) | Tidak | 12 pt | Regular; nilai juga Regular |
| Paragraf Narasi 5C (Kondisi, Kriteria, Sebab, Akibat, Rekomendasi) | **TIDAK** | 12 pt | 100% Regular, tanpa Bold |
| Awalan baku 5C ("Kondisi tersebut disebabkan oleh...", "Akibatnya,...") | **TIDAK** | 12 pt | Regular — bukan Bold |
| Isi Tabel Header | Ya | 10 pt | Header baris bold |
| Isi Tabel Body | Tidak | 10 pt | Regular |
| Nomor Halaman, Footer | Tidak | 9 pt | Regular |

**Larangan Bold:**
- DILARANG mem-BeBold kata atau frasa di tengah paragraf narasi untuk penekanan (mis. "**sangat** penting", "**belum** sesuai"). Penekanan dalam laporan dinas dilakukan melalui diksi tegas, bukan format.
- DILARANG mem-BeBold seluruh paragraf narasi (kecuali memang berfungsi sebagai sub-heading temuan).
- DILARANG mencampur Bold dan Regular dalam satu baris sub-heading temuan — seluruh baris harus Bold.
- DILARANG mem-BeBold nama lokus pada mode numbering otomatis — nama lokus adalah Regular dan berdiri sebagai paragraf tersendiri.

> **Catatan ukuran font:** Spesifikasi awal proyek menetapkan teks isi 11 pt dan heading 12 pt. Namun dalam implementasi kode aktual, seluruh teks (heading, sub-heading, body, narasi 5C, nama lokus) diseragamkan menjadi **12 pt** untuk konsistensi. Hanya tabel (10 pt) dan catatan kaki/sumber (9 pt) yang berbeda.

---

### 12.8 Penomoran Word Otomatis vs Penomoran Manual
- **Penomoran Otomatis Word Native:** Seluruh elemen penomoran otomatis Word (`w:numPr`, `numbering.xml`), hirarki *list level*, tabulasi, dan *indentation* asli dari template harus dipergunakan dan dipertahankan.
- **Fallback Standar Penomoran & Indentasi:** Apabila draf/template laporan tidak memiliki hirarki *list level*, tabulasi, dan *indentation* bawaan, gunakan formula cascade hanging indent & tab stops Bagian 12.3 atau sistem multilevel numbering Bagian 6 (Penomoran Bertingkat).
- **Larangan Penomoran Teks Ganda (*Double Numbering*):** DILARANG keras mengetik nomor manual teks (seperti `1. `, `a. `, `1) `) di dalam teks paragraf yang bertabrakan dengan penomoran otomatis Word (`w:numPr`). Jika paragraf sudah memiliki `w:numPr`, biarkan Word yang menghasilkan nomor. Jika menggunakan penomoran manual (legacy/fallback), jangan gunakan `w:numPr` pada paragraf yang sama.
- **Format Nomor Manual (Fallback):** Bila terpaksa menggunakan penomoran manual teks (karena keterbatasan template), format: `[nomor]\t[teks]` dengan tab stop eksplisit pada posisi teks level tersebut. Jangan gunakan spasi sebagai pemisah antara nomor dan teks. Contoh yang benar: `a.\tJudul Temuan` (dengan tab stop di 1080 dxa). Contoh yang salah: `a. Judul Temuan` (spasi biasa, tidak menjamin perataan).


---

### 12.9 Standar Kompatibilitas Google Workspace / Google Docs (GWS) & Tata Letak Tabel
Saat dokumen laporan pengawasan dikonversi, disinkronkan, atau diedit pada Google Docs melalui Google Workspace API / MCP:
1. **Pembersihan Indentasi dalam Sel Tabel (Anti-Loncatan Ruler):**
   - Setiap paragraf di dalam sel tabel wajib dideklarasikan indentasi nol eksplisit: `<w:ind w:left="0" w:right="0" w:firstLine="0"/>` (`indentStart: 0, indentFirstLine: 0`).
   - Paragraf di dalam sel dilarang mewarisi indentasi paragraf global agar penanda biru pada *ruler* Google Docs tidak bergeser ke tengah atau membuat *hanging indent* liar di kolom kedua/ketiga.
2. **Struktur Tabel Metadata & Kop Surat:**
   - **Tabel Nomor/Tanggal Cover (3 Kolom):** Kolom Label (`84 pt`), Kolom Separator `:` (`27.75 pt`), Kolom Nilai (`222.75 pt`). Paragraf sel berindentasi seragam (`14.17 pt`).
   - **Tabel Kop Surat (2 Kolom):** Kolom Logo (`86.7 pt`), Kolom Teks Lembaga (`366.3 pt`). Teks instansi rata tengah murni (`alignment: CENTER`), spasi baris 1.0 tunggal, dan indentasi 0.
   - **Tabel Metadata Surat Pengantar (4 Kolom Terpisah):**
     - Kolom 1 (`69 pt` / `2.43 cm`): Label (`Nomor`, `Lampiran`, `Hal`)
     - Kolom 2 (`18 pt` / `0.63 cm`): Pemisah `:`
     - Kolom 3 (`237.75 pt` / `8.39 cm`): Isi teks nomor/lampiran/judul laporan (*Justified*, indentasi 0)
     - Kolom 4 (`129.75 pt` / `4.58 cm`): Tanggal surat pada baris pertama (*Right-aligned*)
     - *Kaidah Penting:* Tanggal wajib diletakkan pada kolom ke-4 mandiri (bukan *right tab stop* di dalam teks) agar judul laporan pada baris `Hal` tidak mengalami *hanging indent* saat *line wrapping*.
3. **Penyelarasan Narasi di Bawah Sub-Heading Level 1 (`HEADING_3` / `1.`):**
   - Tajuk sub-bagian bernomor (seperti `1. Anggaran Ketahanan Pangan Daerah` pada Informasi Umum) memiliki nomor di `36 pt` dan teks judul di `54 pt`.
   - Paragraf narasi/isi di bawahnya wajib diset persis dengan **`indentStart: 54 pt` (0.75" / 1080 dxa) dan `indentFirstLine: 54 pt`**, sehingga seluruh baris narasi sejajar 100% dengan huruf pertama judul poinnya.


---

## 13. Modul Python Bawaan (Scripts) — Engine Otomatis

Skill ini membundel modul Python siap pakai di folder `scripts/` yang mengimplementasikan seluruh standar formatting di Bagian 12 secara otomatis. **Gunakan modul ini saat membuat dokumen Word (.docx) dari nol** — tidak perlu lagi menulis OOXML manual.

### 13.1 Paket & File

```
scripts/
├── __init__.py
├── bpkp_docx_engine.py    # Engine inti: create_document, numbering, heading, tabel, tanda tangan
└── lhp_builder.py          # Builder tingkat tinggi: BAB I, II, III + temuan 5C
```

### 13.2 Cara Mengimpor

Modul ini dapat diimpor baik dari dalam package maupun sebagai skrip mandiri di workspace penugasan:

```python
# Opsi A — impor langsung (jika sys.path sudah diset)
from bpkp_docx_engine import create_document, add_heading_1, new_bab_context
from lhp_builder import build_bab_i_template, build_bab_iii_temuan

# Opsi B — salin engine ke workspace penugasan lalu impor
sys.path.insert(0, "/path/to/workspace")
from bpkp_docx_engine import create_document
```

### 13.3 API Inti (`bpkp_docx_engine.py`)

| Fungsi | Kegunaan |
|---|---|
| `create_document()` | Buat dokumen kosong dengan A4, margin kiri/kanan/atas/bawah 3/2/2/2,5 cm, Arial 12pt, spasi 1.15, heading styles, dan infrastruktur numbering. |
| `new_bab_context(doc, "BAB I")` | Mulai Bab baru → restart semua level numbering ke 1. Kembalikan `num_id`. |
| `new_topic_context(doc, "Topik X")` | Mulai topik baru dalam Bab → nomor topik berlanjut sekuensial. Kembalikan `num_id` Bab. |
| `add_heading_1(doc, text)` | Heading 1 (judul BAB) → muncul di Navigation Panel. |
| `add_heading_2(doc, text, num_id)` | Heading 2 (bagian: A. Simpulan) + numbering level 0. |
| `add_heading_3(doc, text, num_id)` | Heading 3 (topik: 1. Lahan...) + numbering level 1. |
| `add_section_heading(doc, text, num_id, ilvl)` | Heading cetak tebal bernomor (A. / a.) tanpa style Word. |
| `add_topic_heading(doc, text, num_id, ilvl)` | Heading topik (1.) dengan style Heading 3 + numbering. |
| `add_numbered_item(doc, text, num_id, ilvl)` | Paragraf bernomor pada level tertentu. |
| `add_subheading(doc, "a.", text, num_id, ilvl)` | Sub-heading temuan (a. Kondisi). |
| `add_body_sub(doc, text, num_id, ilvl)` | Narasi isi di bawah sub-heading. |
| `add_locus(doc, prefix, name, text, num_id, ilvl)` | Rincian per lokus (1) Provinsi...). |
| `add_detail_item(doc, prefix, text, bold_title, num_id, ilvl)` | Detail item (a) Judul: teks). |
| `add_criteria(doc, text, num_id, ilvl)` | Paragraf Kriteria (merah). |
| `add_cause(doc, text, num_id, ilvl)` | Paragraf Sebab. |
| `add_effect(doc, text, num_id, ilvl)` | Paragraf Akibat. |
| `add_recommendation_block(doc, rec_list, num_id, ilvl)` | Blok rekomendasi (intro + item a) b) c)). |
| `add_signature_block(doc, date, title, name)` | Blok tanda tangan dinas + TTE. |
| `add_table_bordered(doc, rows, cols, col_widths)` | Tabel borderless-BPKP + header shading. Kembalikan (table, rows_data). |
| `set_table_flush_alignment(table, left_dxa, total_w)` | Penyelarasan rata kiri tabel sejajar teks narasi (tblInd=720, tblW=8318). |
| `add_runs_with_markdown(p, text, ...)` | Konversi `*miring*` dan `**tebal**` ke run native Word, cegah kebocoran asterisk. |
| `add_runs_with_italic(p, text, ...)` | Helper kompatibilitas untuk memecah teks dengan penanda miring ke run italic. |
| `clone_from_template(template_path)` | Copy-reference technique: kloning template valid dan bersihkan paragraf/tabel. |
| `get_unit_profile(unit_key)` | Ambil data identitas unit kerja seluruh Indonesia dari `unit_profiles.json`. |
| `audit_docx_deterministic(doc)` | Audit otomatis: pastikan em dash = 0, asterisk = 0, dan AI markers = 0. |
| `audit_text_deterministic(text)` | Audit string teks atas em dash, asterisk, dan leksikon penanda AI. |
| `add_p(doc, text, ...)` | Paragraf biasa dengan opsi numbering, indent, align, dan markdown parsing built-in. |
| `add_run(p, text, bold, italic, color, size)` | Tambah run ke paragraf dengan font Arial. |

### 13.4 API Builder (`lhp_builder.py`)

| Fungsi | Kegunaan |
|---|---|
| `build_bab_i_template(doc, simpulan_list, rekomendasi_list)` | BAB I: A. Simpulan + B. Rekomendasi. |
| `build_bab_ii_template(doc, latar_belakang, tujuan, ruang_lingkup, dasar_hukum, kelembagaan)` | BAB II: Umum/Pendahuluan. |
| `build_bab_iii_temuan(doc, temuan_list)` | BAB III: Hasil Evaluasi (list temuan 5C). |
| `build_temuan_5c(doc, temuan_dict, num_id)` | Satu temuan 5C: Kondisi, Kriteria, Sebab, Akibat, Rekomendasi. |

### 13.5 Contoh Penggunaan Lengkap

```python
import sys
sys.path.insert(0, r"<skills-dir>/laporan-pengawasan-bpkp/scripts")

from bpkp_docx_engine import create_document, add_p, add_heading_2, add_signature_block
from lhp_builder import build_bab_i_template, build_bab_ii_template, build_bab_iii_temuan

doc = create_document()

# BAB I
build_bab_i_template(
    doc,
    simpulan_list=[
        ("Tata Kelola Lahan Belum Efektif",
         "LP2B belum ditetapkan dengan dasar hukum definitif."),
        ("Program Benih Belum Mandiri",
         "Produksi benih bersertifikat tidak memenuhi kebutuhan."),
    ],
    rekomendasi_list=[
        ("Tata Kelola Lahan",
         ["Menetapkan Perda LP2B.", "Memutakhirkan data LBS."]),
        ("Program Benih",
         ["Mengaktifkan kembali BBU.", "Menyelenggarakan pelatihan penangkar benih."]),
    ],
)

# BAB II
build_bab_ii_template(
    doc,
    latar_belakang="Ketahanan pangan merupakan prioritas nasional...",
    tujuan=["Mengevaluasi tata kelola ketahanan pangan."],
    ruang_lingkup=["Pemerintah Provinsi Papua Tengah."],
    dasar_hukum=["UU Nomor 39 Tahun 2008.", "Perpres Nomor 2 Tahun 2026."],
    kelembagaan="Dinas Tanaman Pangan dan Ketahanan Pangan.",
)

# BAB III (temuan)
build_bab_iii_temuan(doc, temuan_list=[
    {
        "judul": "Tata Kelola Lahan Pertanian",
        "kondisi": "LP2B belum ditetapkan...",
        "kriteria": "(.) Peraturan Menteri Pertanian tentang LP2B.",
        "sebab": "Ketiadaan komitmen Pemda...",
        "akibat": "Lahan pertanian berpindah fungsi...",
        "rekomendasi": ["Menetapkan Perda LP2B.", "Memutakhirkan data LBS."],
    },
])

# Tanda tangan
add_p(doc, "")
add_signature_block(doc, date_text="Nabire, 31 Agustus 2026",
                    title="Kepala Perwakilan,", name="Kriso Wandi Siahaan")

doc.save("LHP.docx")
```

> **Catatan:** Modul ini hanya menyusun **kerangka struktur & format**. Isi/substansi temuan (Kondisi, Kriteria, Sebab, Akibat, Rekomendasi) harus diisi berdasarkan data penugasan aktual. Gunakan prinsip 5C di Bagian 3 dan kualitas komunikasi di Bagian 1 saat mengisi.

---

## 14. Dokumentasi Pengawasan: Notisi Pembahasan & Berita Acara Exit Meeting

Sesuai **Peraturan BPKP Nomor 4 Tahun 2026 BAB V-C.1**, Dokumentasi Pengawasan (Notisi Hasil Pengawasan, Berita Acara Pembahasan/Exit Meeting, Rencana Tindak Perbaikan, Pernyataan Kesanggupan) merupakan kategori naskah dinas khusus yang **tidak menggunakan penomoran surat dinas biasa** (tanpa kode jenis nomor keluar biasa) Notisi hasil pengawasan disampaikan secara sepihak dan **hanya memuat tanda tangan tim pengawasan**; Berita Acara Pembahasan ditandatangani kedua pihak (Pengendali Teknis/Ketua Tim bersama pimpinan entitas auditan).

### 14.1 Notisi Hasil Pengawasan (Notisi Pembahasan)

Dokumentasi pengawasan lapangan resmi untuk mengomunikasikan simpulan evaluasi dan temuan 5C kepada pimpinan auditan (Gubernur, Bupati, Kepala OPD) sebelum LHP final diterbitkan:

1. **Kepala Notisi & Kop**:
   - Menggunakan logo resmi BPKP dan kop unit perwakilan/pusat.
   - Judul: `NOTISI HASIL PENGAWASAN` (Semua huruf kapital, Bold 12 pt, Center).
2. **Tabel Identitas Penugasan**:
   - Program / Kegiatan Pengawasan (mis. Evaluasi Ketahanan Pangan, Tata Kelola Pendidikan).
   - Sasaran / Sub-Topik (mis. On-Farm & Off-Farm, Revitalisasi Sekolah).
   - Lokus Pengawasan (Provinsi dan/atau Kabupaten/Kota sasaran).
   - Periode Pengawasan (Triwulan / Semester / Tahun Anggaran).
   - Dasar Penugasan (Nomor dan Tanggal Surat Tugas BPKP).
3. **Rekapitulasi Pokok Permasalahan (Status Keterbuktian)**:
   - Tabel ringkas memuat Nomor, Topik Pengawasan, Simpulan Hasil, dan Status Simpulan.
   - **Prinsip Validitas**: Hanya isu dengan status **Terbukti** (didukung Kertas Kerja Evaluasi/KKE dan bukti fisik tervalidasi) yang dituangkan ke dalam uraian rinci temuan. Isu yang tidak terbukti atau sudah diselesaikan auditan didokumentasikan sebagai catatan evaluasi non-temuan.
4. **Uraian Rinci Temuan (Metode 5C Multi-Lokus)**:
   - Terapkan struktur baku: **Kondisi** (perbandingan Provinsi vs Kabupaten), **Kriteria** (rujukan regulasi definitif), **Sebab** (akar masalah sistemik), **Akibat** (dampak operasional/finansial), dan **Rekomendasi Berjenjang**.
5. **Rekomendasi Berjenjang (Strategic vs Operational)**:
   - **Level Pimpinan Daerah (Gubernur / Sekda / Bupati)**: Bersifat kebijakan strategis, pengalokasian anggaran APBD, penetapan Keputusan Kepala Daerah (Perda/Pergub/Perbup/SK), dan instruksi koordinasi lintas OPD.
   - **Level Kepala OPD / Teknis (Dinas Pertanian, Dinas Pendidikan, dsb.)**: Bersifat teknis operasional, penerbitan SOP petunjuk teknis pelaksanaan, validasi data penerima bantuan, pengawasan distribusi fisik barang, dan pemutakhiran berkala.
6. **Tanggapan Mitra & Rencana Aksi (Action Plan)**:
   - Memuat komitmen tindak lanjut dari OPD terkait, pejabat penanggung jawab (*Person in Charge* / PIC), dan target batas waktu penyelesaian (*deadline* bulan/tahun).
7. **Tanda Tangan Pembahasan**:
   - Notisi disampaikan secara sepihak dan hanya memuat tanda tangan tim pengawasan (Peraturan BPKP 4/2026 BAB V-C.1); penandatanganan bersama dengan pimpinan instansi mitra dilakukan pada Berita Acara Pembahasan (14.2).

---

### 14.2 Berita Acara (BA) Pembahasan Hasil Pengawasan / Exit Meeting

Berita Acara digunakan untuk mengikat kesepakatan formal antara Tim BPKP dan auditan atas simpulan serta rencana tindak lanjut hasil pembahasan:

1. **Format Pembuka**:
   - Menyebutkan hari, tanggal, bulan, tahun, dan tempat pelaksanaan pembahasan (*exit meeting*).
   - Contoh: *"Pada hari ini [Hari], tanggal [Tanggal] bulan [Bulan] tahun [Tahun], bertempat di [Lokasi/Ruang Rapat], kami yang bertanda tangan di bawah ini:"*
2. **Komparasi Pihak**:
   - **Pihak Pertama (Tim Pengawas BPKP)**:
     * Nama, NIP, Pangkat/Golongan, dan Jabatan dalam Tim (Pengendali Teknis / Ketua Tim).
     * Dasar penugasan: Surat Tugas Kepala Perwakilan BPKP Nomor [ST-xxx] tanggal [Tanggal ST].
   - **Pihak Kedua (Entitas Auditan / Pemda)**:
     * Nama, NIP, Jabatan resmi pimpinan mitra kerja (Sekretaris Daerah, Asisten Sekda, Kepala Dinas, atau Inspektur Daerah).
3. **Klausul Kesepakatan**:
   - Pihak Pertama telah memaparkan dan menyerahkan Notisi Hasil Pengawasan kepada Pihak Kedua.
   - Pihak Kedua telah membahas, memahami, dan menyepakati seluruh temuan dan rekomendasi yang tercantum dalam Notisi Hasil Pengawasan terlampir.
   - Pihak Kedua berkomitmen menyelesaikan tindak lanjut perbaikan sesuai dengan rencana aksi (*action plan*) dan batas waktu yang disepakati.
   - Notisi Hasil Pengawasan dan lembar tanggapan/rencana aksi merupakan bagian tidak terpisahkan dari Berita Acara ini.
4. **Kolom Tanda Tangan Komparatif**:
   - Disajikan dalam tabel 2 kolom (kiri: Pihak Pertama Tim BPKP, kanan: Pihak Kedua Pemerintah Daerah/Instansi Auditan) dilengkapi nama terang, NIP, dan jabatan.
