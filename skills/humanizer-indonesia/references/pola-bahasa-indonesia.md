# Pola yang perlu diperiksa

Gunakan daftar ini sebagai alat diagnosis, bukan daftar kata terlarang.

## Artefak chatbot

- Pembuka seperti "Tentu", "Baik", atau "Berikut adalah" ketika teks dapat langsung dimulai.
- Penutup seperti "Semoga bermanfaat" atau tawaran bantuan yang bukan bagian dari naskah.
- Sapaan dan pujian generik yang tidak cocok dengan genre.

## Klaim dan abstraksi

- "merupakan bukti nyata", "memainkan peran penting", "menjadi tonggak", "di tengah lanskap yang terus berkembang" tanpa informasi konkret.
- Kata evaluatif seperti "sangat penting", "komprehensif", "inovatif", atau "strategis" tanpa ukuran atau bukti.
- Atribusi kabur: "para ahli mengatakan", "banyak pihak menilai", atau "berbagai penelitian" tanpa sumber.

### Klaim evaluatif menggantung (ragam laporan dinas)

Klaim berderajat tanpa ukuran atau fakta pendamping sering muncul dalam laporan telaah/audit dan merupakan artefak AI yang halus:

- **"belum berjalan optimal"** tanpa disebutkan optimal seperti apa atau jumlah pastinya.
  - *Perbaikan*: ikat klaim ke fakta. "Dukungan administratif pemerintah daerah belum optimal" -> "Dari delapan kabupaten, baru dua yang menetapkan SK Satgas MBG".
- **"berjalan cukup pesat"**, "menunjukkan kemajuan signifikan", "berpotensi memengaruhi ketepatan pelaksanaan" tanpa angka pembanding.
  - *Perbaikan*: sebutkan angka atau hapus derajatnya. "Berjalan cukup pesat" -> cukup "berjalan dengan dukungan X, Y, dan Z" bila tidak ada ukuran kecepatan.
- **Aposisi menggantung / meta-komentar**: kalimat yang menilai relevansi tulisannya sendiri, misalnya "..., kondisi yang relevan untuk ditelaah pada aspek kesesuaian antara A dan B".
  - *Perbaikan*: ubah menjadi isi nyata, misalnya mengutip pertanyaan pengawasan yang dijawab: "... berkaitan langsung dengan pertanyaan pengawasan, yaitu apakah seluruh SPPG yang menerima pencairan telah memberikan layanan".

## Struktur mekanis

- Paragraf dengan pola pembuka–tiga butir–kesimpulan yang berulang.
- Setiap bagian diakhiri rangkuman yang hanya mengulang isinya.
- Kalimat berpanjang hampir sama dan selalu memakai pola subjek–predikat–objek.
- Penggunaan "selain itu", "lebih lanjut", "di sisi lain", dan "oleh karena itu" secara beruntun meski hubungan antarkalimat sudah jelas.
- Konstruksi "bukan hanya ..., melainkan juga ..." yang dipakai sebagai hiasan.
- **Tanda Pisah (Em Dash `—`)**: Sering muncul otomatis dari model bahasa asing untuk menyelipkan anak kalimat. Dalam teks dinas/audit formal, tanda pisah ini terasa canggung dan harus diganti dengan koma, kurung, atau kalimat aktif yang ditata ulang.
- **Pleonasme & Kerancuan Konjungsi ("dan serta")**:
  - Penggunaan *"dan serta"* secara bergandengan tanpa struktur jeda (misal: *"menyediakan bibit dan serta pupuk"*) merupakan pleonasme/artefak mekanis yang salah kaprah.
  - Pengabaian distingsi makna antara *"dan"* (penambahan murni berbobot setara) dengan *"serta"* (penyertaan tokoh/dokumen/unsur pengikut atau pendamping).
  - Kesalahan tanda koma: menambahkan koma sebelum konjungsi pada 2 unsur (*"ayah, dan ibu"* -> salah), atau justru menghilangkan koma sebelum unsur terakhir pada perincian $\ge 3$ unsur (*"buku, pena dan pensil"* -> salah EYD V, harus *"buku, pena, dan pensil"*).

### Pola naskah laporan formal (telaah, laporan pengawasan, laporan hasil evaluasi)

Pola berikut muncul khas pada laporan formal AI dan paling sering lolos pemeriksaan karena bahasanya sudah baku. Periksa satu per satu:

1. **Pembuka dengan keterangan menumpuk sebelum subjek.**
   - *Ciri AI*: "Berdasarkan hasil pembahasan dengan Kepala Regional BGN, Program MBG telah dilaksanakan dengan terbangunnya 36 SPPG." / "Sejauh pengumpulan informasi awal di Kabupaten Nabire, capaian penyaluran MBG menunjukkan bahwa ..."
   - *Perbaikan*: dahulukan subjek, keterangan menyusul sebagai penjelas. "Program MBG telah berjalan dengan terbangunnya 36 SPPG berdasarkan pembahasan dengan Kepala Regional BGN." Kalimat aktif juga memungkinkan: "Koordinator Wilayah BGN mengidentifikasi kendala pada 8 SPPG" menggantikan "Berdasarkan hasil pemantauan ..., teridentifikasi sejumlah kendala ...".
2. **Pembingkaian evaluatif.** Kalimat pembuka simpulan yang merangkum nilai keseluruhan sebelum mengatakan apa pun.
   - *Ciri AI*: "Secara keseluruhan, informasi dari A, B, dan C memperlihatkan dua sisi pelaksanaan program."
   - *Perbaikan*: langsung ke isi. "Dari informasi yang terkumpul, pembangunan SPPG berjalan dengan dukungan ..."
3. **Kalimat rujukan-diri (kalimat pengisi).** Kalimat yang isinya hanya menegaskan kesesuaian dengan bagian lain dokumen tanpa menambah informasi.
   - *Ciri AI*: "Pengumpulan informasi awal tersebut sejalan dengan penugasan insilwas sebagaimana diuraikan pada bagian sebelumnya."
   - *Perbaikan*: hapus; nyatakan status yang belum dikatakan, misalnya mana pertanyaan yang sudah terjawab dan mana yang menunggu data.
4. **Simpulan yang menyalin bagian isi.** Rangkuman yang mengulang angka atau daftar verifikasi secara kata per kata.
   - *Perbaikan*: simpulan memberi penilaian atau arah, bukan menyalin. Jika perlu merujuk, cukup sekali dan singkat ("sesuai penugasan pada bagian sebelumnya").
5. **Transisi ritual beruntun.** "Adapun ...", "Di samping itu ...", "Selain itu ... Sementara itu ...", "Untuk memenuhi X tersebut, ...", "Secara ringkas, ..." dipakai berurutan sebagai jeda hafalan.
   - *Perbaikan*: variasikan atau hilangkan; banyak kalimat justru lebih kuat tanpa penghubung.
6. **Penutup formulaik yang menilai nilai laporan itu sendiri.**
   - *Ciri AI*: "Hasil telaah ini selanjutnya menjadi dasar pertimbangan pimpinan dalam menentukan kegiatan pengawasan pada triwulan berikutnya."
   - *Perbaikan*: beri fungsi nyata pada objeknya. "Indikasi mark-up menjadi bahan pengujian kewajaran harga pada kegiatan pengawasan triwulan berikutnya."
7. **Kausalitas formulaik dengan abstraksi berlapis.**
   - *Ciri AI*: "Ketiadaan Satgas ini berdampak pada rendahnya peningkatan dan pemerataan cakupan realisasi program."
   - *Perbaikan*: tunjukkan mekanismenya. "Tanpa Satgas, koordinasi dan dukungan daerah sulit berjalan sehingga cakupan program terhambat."
8. **Padatan pasif berlapis.**
   - *Ciri AI*: "Terdapat indikasi pembelanjaan ... yang berpotensi menimbulkan ... serta membuka ruang terjadinya ..."
   - *Perbaikan*: aktifkan subjek dan rapat padatannya. "Pembelanjaan diarahkan ke koperasi internal (self-dealing), yang berpotensi menimbulkan benturan kepentingan dan penggelembungan harga."
9. **Fakta beruntun dalam kalimat terpisah yang polanya sama.** "X telah selesai ... dan menunggu ... serta telah berlangsung ... " lalu "Selain itu, ... telah dibangun ..." lalu "Sementara itu, ... juga terdapat ...".
   - *Perbaikan*: gunakan kontras ("sementara", "sedangkan") atau titik koma untuk menggabung fakta sejenis; kalimat pendek penutup tanpa penghubung sering terdengar paling manusiawi.
10. **Pengulangan kata yang sama dalam satu kalimat.** "Terdapat indikasi ... (indikasi self-dealing)", "Mengacu pada ... penugasan mengacu pada ...".
    - *Perbaikan*: hapus salah satu; koreksi ini aman karena tidak menyentuh makna.


## Perbaikan yang aman

- Ganti abstraksi dengan siapa melakukan apa, jika informasinya memang tersedia.
- Gabungkan kalimat yang mengulang; pecah kalimat yang menanggung terlalu banyak gagasan.
- Pakai kata "adalah", "ialah", "punya", atau verba langsung ketika lebih alami untuk ragam yang dipilih.
- Pertahankan istilah resmi dan teknis. Jangan mengarang contoh, statistik, pengalaman, atau sikap penulis.
- Ikat setiap klaim evaluatif (optimal, pesat, merata, signifikan) ke angka, jumlah, atau fakta pendamping; jika tidak ada ukurannya, turunkan derajat klaim.
- Dalam teks akademik dan dinas, manusiawi berarti jernih dan tidak mekanis, bukan percakapan santai.

## Daftar periksa audit cepat naskah laporan formal

1. Pembuka paragraf: apakah subjek muncul sebelum keterangan panjang?
2. Apakah ada kalimat yang isinya hanya merujuk bagian lain dokumen tanpa informasi baru?
3. Apakah simpulan menyalin angka/daftar dari bagian isi kata per kata?
4. Apakah setiap klaim evaluatif punya angka atau fakta pendamping?
5. Apakah transisi (Adapun/Di samping itu/Selain itu/Untuk memenuhi X tersebut) muncul beruntun?
6. Apakah ada kalimat penutup yang menilai nilai laporan itu sendiri ("menjadi dasar pertimbangan pimpinan ...")?
7. Apakah sebab-akibat menunjukkan mekanisme, bukan sekadar "X berdampak pada rendahnya Y"?
8. Apakah ada kata yang sama berulang dalam satu kalimat (di luar istilah teknis)?

## Kosakata Penanda AI yang Sering Lolos Pemolesan (Terverifikasi Lapangan)

Daftar berikut dikumpulkan dari temuan nyata yang lolos beberapa putaran pemolesan sub-agent dan baru tertangkap mata manusia. Gunakan sebagai pola regex pada audit deterministik.

| Penanda | Contoh keluaran | Perbaikan |
| :--- | :--- | :--- |
| `turut + verba` | "kendala ... turut menyulitkan tim survei", "literasi ... turut menghambat pengumpulan nota" | Hapus "turut", pakai verba langsung: "menyulitkan", "menghambat" |
| `nyaris tidak` | "KPB nyaris tidak memiliki pilihan rekanan" | "hampir tidak punya pilihan" |
| `tercermin dari` | "kondisi ini tercermin dari data portal" | Pecah kalimat: "sering terlambat. Portal masih mencatat ..." |
| `telah terpetakan` | "jumlah unit ... telah terpetakan" | "sudah terjawab dari data yang terkumpul" / "telah terhimpun" |
| `menyimpan risiko` | "menyimpan risiko sengketa tanah" | "berisiko menimbulkan sengketa tanah" (risiko bukan benda yang disimpan) |
| `perlu diwaspadai` | "beberapa risiko ... perlu diwaspadai" | "risiko yang perlu diuji lebih lanjut" |
| `perlu dilakukan` | "Langkah selanjutnya yang perlu dilakukan X adalah" | "Langkah selanjutnya bagi X adalah" |
| Kata ganda satu klausa | "Sebagian pertanyaan ... telah terjawab sebagian" | Pecah kontras: "X sudah terjawab. Y belum: ..." |
| Kolon dramatis | "berjalan lambat: 77,17% unit masih ..." | "belum berjalan sesuai rencana. Hambatan yang menonjol adalah ..." |
| Keterangan menumpuk sebelum subjek | "Berdasarkan KAP ..., unit kerja ... bertugas melaksanakan" | "Sesuai KAP ..., unit kerja hanya membawa ..." |

Kata baku yang **jangan** ditandai sebagai AI (muncul di naskah dinas resmi): "merupakan", "menunjukkan", "bertujuan", "guna memastikan". Ketikanya baku, bukan penanda mesin.
