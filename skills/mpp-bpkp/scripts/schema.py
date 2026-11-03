"""Kontrak isian MPP v1. Sel DATA lama dipertahankan bila maknanya sama."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.1'
DATA = {
    29: ('BIDANG', 'Bidang', '', True),
    30: ('NAMA_PENUGASAN', 'Nama lengkap penugasan / judul folder', '', True),
    31: ('SASARAN_PENGAWASAN', 'Sasaran pengawasan', '', True),
    32: ('NOMOR_KP', 'Nomor kartu penugasan', '', False),
    33: ('DAFTAR_OBJEK_PENGAWASAN', 'Nama objek/entitas pengawasan', '', True),
    34: ('PERIODE_OBJEK', 'Tahun anggaran/periode objek', '', True),
    35: ('NOMOR_RENCANA', 'Nomor rencana pengawasan', '', False),
    36: ('TINGKAT_RISIKO', 'Tingkat risiko', 'Sedang', False),
    37: ('ALAMAT_OBJEK', 'Alamat dan telepon objek', '', True),
    39: ('TANGGAL_ST', 'Tanggal konsep surat tugas', '', True),
    40: ('TANGGAL_PENGESAHAN', 'Tanggal pengesahan perencanaan', '', True),
    41: ('HARI_PERSIAPAN', 'Hari kerja kalender fase persiapan', '', True),
    42: ('HARI_PELAKSANAAN', 'Hari kerja kalender fase pelaksanaan', '', True),
    43: ('HARI_PENYELESAIAN', 'Hari kerja kalender fase penyelesaian', '', True),
    44: ('PERS_MULAI', 'Mulai persiapan', '', True),
    45: ('PERS_SELESAI', 'Selesai persiapan', '', True),
    46: ('LAKS_MULAI', 'Mulai pelaksanaan', '', True),
    47: ('LAKS_SELESAI', 'Selesai pelaksanaan', '', True),
    48: ('SELESAI_MULAI', 'Mulai penyelesaian', '', True),
    49: ('SELESAI_AKHIR', 'Selesai penyelesaian', '', True),
    50: ('TANGGAL_SELESAI', 'Direncanakan selesai penugasan', '', True),
    51: ('RPL', 'Rencana penerbitan laporan (RPL)', '', True),
    53: ('JAM_PER_HARI', 'Jam pengawasan per hari orang', 6.5, True),
    54: ('JUMLAH_AT', 'Jumlah anggota tim (otomatis)', '', False),
    56: ('JENIS_PENUGASAN', 'Jenis penugasan: PIA / PENGAWASAN', '', True),
    57: ('BENTUK_PENGAWASAN', 'Bentuk penugasan: EVALUASI / AUDIT / PIA / LAINNYA', '', False),
    58: ('SEKTOR', 'Sektor', '', True),
    59: ('TEMA', 'Tema', '', True),
    60: ('TOPIK', 'Topik', '', True),
    61: ('TUJUAN_PENGAWASAN', 'Tujuan pengawasan', '', True),
    62: ('RUANG_LINGKUP', 'Ruang lingkup pengawasan', '', True),
    63: ('PENERIMA_LAPORAN', 'Jabatan penerima laporan', '', True),
    64: ('SUMBER_PEMBIAYAAN', 'Sumber pembiayaan', '', True),
    65: ('DASAR_HUKUM_RINGKAS', 'Dasar penugasan/peraturan (teks lengkap)', '', True),
    66: ('PEDOMAN_PENGAWASAN', 'Nama pedoman/panduan teknis', '', True),
    67: ('JABATAN_PENERIMA', 'Jabatan penerima surat pengantar', '', True),
    68: ('KOTA_PENERIMA', 'Tempat/kota penerima surat', '', True),
    69: ('HAL_SURAT_PENGANTAR', 'Hal surat pengantar (kosong = nama penugasan)', '', False),
    70: ('NOMOR_SURAT_PENGANTAR', 'Nomor surat pengantar (boleh kosong saat konsep)', '', False),
    71: ('TANGGAL_SURAT_PENGANTAR', 'Tanggal surat pengantar', '', True),
    72: ('NOMOR_ST', 'Nomor ST (boleh kosong saat konsep)', '', False),
    73: ('JABATAN_KAPER', 'Jabatan penandatangan ST/pengantar', 'Kepala Perwakilan', False),
    74: ('TANGGAL_PAKTA', 'Tanggal pakta integritas', '', True),
    75: ('TANGGAL_MULAI', 'Mulai periode ST', '', True),
    76: ('JUMLAH_HARI', 'Hari kerja ST (otomatis, Sabtu/Minggu dikecualikan)', '', True),
    77: ('RMP_PKPT', 'RMP menurut PKPT (jika ada)', '', False),
    78: ('RPL_PKPT', 'RPL menurut PKPT (jika ada)', '', False),
    79: ('RPL_NON_PKPT', 'RPL non-PKPT (jika ada)', '', False),
    80: ('TGL_KONSEP_LAPORAN', 'Target selesai konsep laporan', '', True),
}
NARASI = {
    'LATAR_BELAKANG': ('Latar belakang dan dasar kebutuhan penugasan', True),
    'METODOLOGI': ('Metodologi penugasan pengawasan', True),
    'BATAS_TANGGUNG_JAWAB_PENUGASAN': ('Batas tanggung jawab penugasan', True),
    'PERTIMBANGAN_SUMBER_DAYA': ('Pertimbangan penentuan sumber daya', True),
    'STRATEGI_PENGAWASAN': ('Strategi/tujuan penugasan pengawasan', True),
    'FOKUS_PENGAWASAN': ('Fokus pengawasan', True),
    'LOKUS_DAN_DASAR_PEMILIHAN': ('Lokus dan dasar pemilihannya', True),
    'PENGANTAR_RISIKO_KLIEN': ('Pengantar tabel risiko klien', False),
    'PENGANTAR_RISIKO_PENUGASAN': ('Pengantar tabel risiko penugasan', False),
    'METODOLOGI_TAMBAHAN': ('Uraian metodologi tambahan', False),
    'JENIS_DAN_TINGKAT_KEYAKINAN': ('Jenis penugasan dan tingkat keyakinan; jangan otomatis limited assurance', True),
    'LANGKAH_PERSIAPAN': ('Langkah persiapan KM 6; satu langkah per baris', True),
    'LANGKAH_SIMPULAN': ('Langkah penyusunan simpulan KM 6', True),
    'LANGKAH_FINAL_KK': ('Langkah finalisasi kertas kerja KM 6', True),
    'LANGKAH_LAPORAN': ('Langkah penyusunan laporan KM 6', True),
    'PROSEDUR_LAIN': ('Prosedur persiapan lain (opsional)', False),
}
TABLES = {
    'IHP': ['Informasi Hasil Pengawasan (Insilwas)'],
    'PROSES_BISNIS': ['Tahap proses', 'Tujuan tahap', 'Aktivitas utama', 'Input', 'Output'],
    'RISIKO_KLIEN': ['Risiko klien', 'Uraian risiko', 'Dampak'],
    'RISIKO_PENUGASAN': ['Pernyataan risiko', 'Dampak terhadap penugasan', 'Rencana tindak pengendalian'],
    'PROGRAM_KERJA': ['Kode uji', 'Uraian/tujuan pengujian', 'Langkah kerja (Alt+Enter)', 'Pelaksana (nama/peran)', 'Jam', 'HP (otomatis)', 'Ref. KKA'],
    'TEMBUSAN': ['Jabatan/instansi penerima tembusan'],
    'Pegawai': ['Nama', 'NIP', 'NIP Lama', 'Bidang'],
}
BASE_ROLES = ['Wakil Penanggung Jawab', 'Pengendali Teknis', 'Ketua Tim'] + ['Anggota Tim'] * 20
# Batas jam pengawasan per hari orang BPKP (dikonfirmasi pemelihara skill).
JAM_MAKS_PER_HARI = 6.5
JAM_HARI_CATATAN = 'Jam pengawasan per hari orang maksimal 6,5 jam (nilai bawaan 6,5).'
# Teks identitas yang tertulis apa adanya di DOCX assets/templates (Papua Tengah). Ini kunci
# penggantian, terpisah dari profil_unit.json yang boleh diubah ke unit lain.
TEMPLATE_IDENTITY = {
    'unit': 'Perwakilan BPKP Provinsi Papua Tengah',
    'nama_kop_baris1': 'BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN',
    'nama_kop_baris2': 'PERWAKILAN PROVINSI PAPUA TENGAH',
    'alamat': 'Jalan Sam Ratulangi, Kelurahan Oyehe, Distrik Nabire',
    'wilayah_kodepos': 'Kabupaten Nabire, Provinsi Papua Tengah, Kode Pos: 98816',
    'email': 'papua.tengah@bpkp.go.id',
    'website': 'www.bpkp.go.id/papua.tengah',
    'kota': 'Nabire',
}
# Kunci DATA (opsional, kolom E) -> field profil_unit.json; urutan = urutan penggantian, kota terakhir.
PROFILE_FIELDS = {'UNIT_KERJA': 'unit', 'KOP_BARIS1': 'nama_kop_baris1', 'KOP_BARIS2': 'nama_kop_baris2', 'ALAMAT_UNIT': 'alamat', 'WILAYAH_KODEPOS': 'wilayah_kodepos', 'EMAIL_UNIT': 'email', 'WEBSITE_UNIT': 'website', 'KOTA_UNIT': 'kota'}
PIA_REQUIRED = ['TOPIK_PIA','NOMOR_ST_PIA','TANGGAL_ST_PIA','TANGGAL_MULAI_PIA','TANGGAL_SELESAI_PIA','TUJUAN_PIA','LINGKUP_PIA','GAMBARAN_UMUM_PIA','HASIL_TELAAH_PIA','HASIL_KONFIRMASI_PIA','KECUKUPAN_INFORMASI_PIA','SIMPULAN_RINGKAS_PIA','SIMPULAN_KELAYAKAN_PENGAWASAN','USULAN_KEPUTUSAN_PENGAWASAN','BATAS_TANGGUNG_JAWAB_PIA','METODE_PIA_1','NAMA_PENANDATANGAN_ND','JABATAN_PENANDATANGAN_ND','JABATAN_PENERIMA_ND','TANGGAL_ND_PIA','NAMA_KT_PIA','NIP_KT_PIA','NAMA_KORWAS_PIA','NIP_KORWAS_PIA','HARI_PIA_TERBILANG','KENDALA_DAN_PENANGANAN_PIA','DASAR_PIA_1']
