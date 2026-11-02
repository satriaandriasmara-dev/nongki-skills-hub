---
name: humanizer-indonesia
description: Tulis ulang teks bahasa Indonesia agar alami, manusiawi, spesifik, sesuai konteks tanpa mengubah makna (humanize/naturalisasi), bebas artefak AI, serta bersih dari tanda pisah (em dash). Termasuk audit deterministik penanda AI pada naskah panjang dan konversi penanda miring markdown ke run italic asli pada DOCX/Google Docs.
tags: [indonesian, humanizer, naturalize, eyd, docx]
---

# Humanizer Indonesia

## Sasaran

Hasilkan tulisan yang terasa ditulis seseorang untuk audiens tertentu, bukan teks yang sekadar dibuat lebih santai. Pertahankan tingkat formalitas, tujuan, fakta, istilah, kutipan, dan suara penulis.

Baca [pola dan padanan Indonesia](references/pola-bahasa-indonesia.md) sebelum mengerjakan teks panjang atau teks yang sangat terasa seperti keluaran AI.

## Alur kerja

1. Kenali jenis teks, audiens, hubungan penulis–pembaca, nada, dan batas panjang.
2. Tandai ciri mekanis: pembuka generik, klaim besar tanpa bukti, abstraksi berlebihan, daftar tiga serangkai yang dipaksakan, sinonim bergilir, pengulangan kesimpulan, transisi kaku, kalimat dengan irama seragam, serta penggunaan tanda pisah (em dash `—`) yang merupakan artefak bawaan terjemahan/AI kaku. Untuk naskah laporan formal (telaah, laporan pengawasan, hasil evaluasi), gunakan pula daftar periksa khusus ragam laporan pada referensi pola bahasa.
3. Tulis ulang hanya bagian yang membutuhkan perubahan. Gunakan kata konkret, subjek yang jelas, verba langsung, dan detail yang tersedia dalam sumber.
4. Variasikan panjang serta bentuk kalimat secara wajar. Jangan sengaja menambahkan kesalahan, slang, humor, opini, atau pengalaman pribadi yang tidak berasal dari penulis.
5. Baca keras secara mental. Hapus kalimat yang terdengar seperti slogan, presentasi korporat, atau respons chatbot.
6. Eliminasi seluruh tanda pisah (em dash `—`): ubah menjadi tanda koma, tanda kurung, atau restrukturisasi susunan kalimat menjadi lugas dan formal.
7. Untuk naskah laporan formal, jalankan daftar periksa audit cepat di bagian akhir referensi pola bahasa sebelum menyatakan selesai.
8. Lakukan audit makna: angka, nama, negasi, tingkat kepastian, hubungan sebab-akibat, dan kutipan harus tetap sama.
9. Jika pengguna juga meminta ejaan baku, jalankan pemeriksaan dengan skill `eyd-indonesia` setelah humanisasi.

## Eliminasi Tanda Pisah (Em Dash `—`)

Dalam ragam formal bahasa Indonesia (terutama naskah dinas, laporan pengawasan/audit, dan karya akademik), penggunaan tanda pisah panjang (*em dash* `—`) merupakan salah satu indikasi paling kuat dari luaran AI mentah atau terjemahan harfiah bahasa Inggris.

### Pedoman Penggantian Em Dash:
1. **Gunakan Tanda Koma (`,`)**: Apabila tanda pisah dipakai untuk aposisi atau klausa selaan sederhana.
   - *Ciri AI*: "Pemerintah daerah—melalui Dinas Pertanian—belum menetapkan target produksi."
   - *Alami & Baku*: "Pemerintah daerah, melalui Dinas Pertanian, belum menetapkan target produksi."
2. **Gunakan Tanda Kurung (`(...)`)**: Apabila keterangan sela bersifat penjelasan teknis pelengkap atau rincian opsional.
   - *Ciri AI*: "Penyaluran bantuan pupuk—khususnya NPK dan urea—tidak tepat waktu."
   - *Alami & Baku*: "Penyaluran bantuan pupuk (khususnya NPK dan urea) tidak tepat waktu."
3. **Restrukturisasi Kalimat**: Pecah kalimat yang terlalu berbelit atau ganti menjadi konstruksi aktif langsung tanpa tanda pisah.
   - *Ciri AI*: "Strategi ini diterapkan untuk mendorong pertumbuhan ekonomi—suatu target yang telah dicanangkan sejak tahun lalu."
   - *Alami & Baku*: "Strategi ini diterapkan guna mendorong pertumbuhan ekonomi sesuai target yang dicanangkan sejak tahun lalu."
4. **Rentang Nilai atau Waktu**: Dalam naskah dinas dan pelaporan audit formal, gunakan kata "sampai dengan" (atau singkatan baku `s.d.`) daripada tanda pisah.
   - *Ciri AI*: "Periode pelaksanaan tahun 2024—2026."
   - *Alami & Baku*: "Periode pelaksanaan tahun 2024 s.d. 2026."

## Pilihan keluaran

- Secara default, berikan versi akhir saja.
- Jika diminta transparansi, berikan versi akhir dan ringkasan perubahan utama; jangan membebani pengguna dengan seluruh proses internal.
- Jika ada bagian yang tidak dapat dinaturalisasi tanpa mengubah maksud, pertahankan bagian itu dan beri catatan singkat.

## Mode DOCX

Gunakan bersama skill `docx` atau `editor-docx-indonesia`. Pertahankan format dokumen dan ubah hanya isi yang disetujui. Jangan mengubah kutipan, bibliografi, tabel data, rumus, kode, atau metadata secara otomatis.

### Konversi Penanda Miring Markdown ke Run Italic Asli (Kebocoran Asterisk)

Output sub-agent LLM sering memakai penanda markdown `*kata*` atau `_kata_`. Jika teks semacam itu ditanam langsung ke docx/Google Docs sebagai string, asterisknya tercetak literal (contoh nyata yang lolos dua puturan pemolesan: "data kebutuhan riil perumahan (*backlog*)").

**Aturan baku:**
1. Sebelum menulis ke docx, pecah teks menjadi segmen dan buat *run* terpisah dengan properti `run.italic = True` — jangan pernah menanam karakter `*` ke dalam dokumen.
2. Jika frasa yang akan diganti terpecah antar-*run* (karena di dalamnya ada istilah italic), penggantian string satu *run* akan gagal diam-diam. Solusi terverifikasi: hapus seluruh *run* paragraf, lalu susun ulang dari daftar segmen `(teks, is_italic)`.
3. Selalu verifikasi pasca-rakit: jumlah karakter `*` di seluruh dokumen wajib 0.

```python
def add_runs_with_italic(p, text):
    """Teks memakai <i>...</i>; sisanya regular. Font diset per run."""
    import re
    for part in re.split(r'(<i>.*?</i>)', text):
        if not part:
            continue
        if part.startswith('<i>') and part.endswith('</i>'):
            r = p.add_run(part[3:-4]); r.italic = True
        else:
            r = p.add_run(part)
        r.font.name = 'Arial'; r.font.size = Pt(12)
```

### Audit Deterministik Wajib (Bukan Opsional)

Pemolesan oleh sub-agent `editor` secara berulang terbukti masih meloloskan kosakata penanda AI. Sebelum menyatakan naskah selesai, jalankan pemindaian *regex* deterministik atas teks penuh (lihat daftar kosakata pada `references/pola-bahasa-indonesia.md`), lalu perbaiki temuan secara manual terarah. Pemindaian juga menghitung: jumlah `—`/`–` (wajib 0), jumlah `*` (wajib 0), dan panjang kalimat (>60 kata = kandidat pemecahan, kecuali deret angka wajib ala tabel-narasi).
