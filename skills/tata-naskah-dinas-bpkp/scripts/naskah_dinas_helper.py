# -*- coding: utf-8 -*-
"""
Naskah Dinas Helper - BPKP
==========================

Modul pembantu untuk menyusun komponen Tata Naskah Dinas BPKP sesuai
Peraturan BPKP Nomor 4 Tahun 2026 (menggantikan Perban 4/2022). Mencakup: kop surat, nota dinas,
surat tugas, dan lembar pengesahan.

Modul ini mengimpor engine inti (``bpkp_docx_engine``) untuk konsistensi
format (font, margin, heading styles). Ia menyediakan builder tingkat
tinggi untuk komponen naskah dinas yang sering dipakai berulang.
"""

from __future__ import annotations

from typing import Optional, List

import os
import sys
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# Impor engine inti - relatif jika dipanggil sebagai paket, absolut jika mandiri.
# Engine bpkp_docx_engine berada di skill laporan-pengawasan-bpkp.

try:
    from .bpkp_docx_engine import (
        # Engine core: document & style
        create_document, setup_heading_styles, setup_numbering_infrastructure,
        _fix_theme_fonts, _sync_styles_with_effects,
        reset_numbering_state, get_new_numbering_instance,
        new_bab_context, new_topic_context,
        # Constants & font helpers
        _apply_font, FONT_NAME, BLACK, RED,
        _ensure_style_font, _set_style_spacing,
        # Paragraph & run builders
        add_p, add_run, add_heading_1, add_heading_2, add_heading_3,
        add_heading_4, add_heading_bertingkat, add_section_heading, add_topic_heading,
        add_numbered_item, add_simple_numbered,
        add_subheading, add_body_sub, add_locus, add_detail_item,
        add_criteria, add_cause, add_effect,
        add_recommendation, add_recommendation_block,
        add_runs_with_markdown, add_runs_with_italic,
        # Numbering attachment
        _attach_numbering,
        # Cell & table helpers
        clean_cell_p, set_cell_margins, set_cell_shading,
        set_cell_bottom_border, set_table_borders, add_table_bordered,
        add_table_with_subheader, set_table_flush_alignment,
        # Other builders & audits
        add_signature_block, add_cover_page, add_daftar_isi, add_page_break,
        audit_text_deterministic, audit_docx_deterministic,
        _LEVEL_FMT,
    )
except ImportError:
    # Cari engine di skill laporan-pengawasan-bpkp (sibling directory)
    _here = os.path.dirname(os.path.abspath(__file__))
    _engine_dir = os.path.normpath(
        os.path.join(_here, '..', '..', 'laporan-pengawasan-bpkp', 'scripts')
    )
    if _engine_dir not in sys.path:
        sys.path.insert(0, _engine_dir)
    from bpkp_docx_engine import (
        # Engine core: document & style
        create_document, setup_heading_styles, setup_numbering_infrastructure,
        _fix_theme_fonts, _sync_styles_with_effects,
        reset_numbering_state, get_new_numbering_instance,
        new_bab_context, new_topic_context,
        # Constants & font helpers
        _apply_font, FONT_NAME, BLACK, RED,
        _ensure_style_font, _set_style_spacing,
        # Paragraph & run builders
        add_p, add_run, add_heading_1, add_heading_2, add_heading_3,
        add_heading_4, add_heading_bertingkat, add_section_heading, add_topic_heading,
        add_numbered_item, add_simple_numbered,
        add_subheading, add_body_sub, add_locus, add_detail_item,
        add_criteria, add_cause, add_effect,
        add_recommendation, add_recommendation_block,
        add_runs_with_markdown, add_runs_with_italic,
        # Numbering attachment
        _attach_numbering,
        # Cell & table helpers
        clean_cell_p, set_cell_margins, set_cell_shading,
        set_cell_bottom_border, set_table_borders, add_table_bordered,
        add_table_with_subheader, set_table_flush_alignment,
        # Other builders & audits
        add_signature_block, add_cover_page, add_daftar_isi, add_page_break,
        audit_text_deterministic, audit_docx_deterministic,
        _LEVEL_FMT,
    )

__all__ = [
    # Engine core (re-export agar helper self-contained)
    "create_document", "setup_heading_styles", "setup_numbering_infrastructure",
    "reset_numbering_state", "get_new_numbering_instance",
    "new_bab_context", "new_topic_context",
    # Constants & font helpers
    "FONT_NAME", "BLACK", "RED", "_apply_font",
    "_ensure_style_font", "_set_style_spacing", "_LEVEL_FMT",
    # Paragraph & run builders (re-export)
    "add_p", "add_run",
    "add_heading_1", "add_heading_2", "add_heading_3", "add_heading_4",
    "add_heading_bertingkat",
    "add_section_heading", "add_topic_heading",
    "add_numbered_item", "add_simple_numbered",
    "add_subheading", "add_body_sub", "add_locus", "add_detail_item",
    "add_criteria", "add_cause", "add_effect",
    "add_recommendation", "add_recommendation_block",
    "add_runs_with_markdown", "add_runs_with_italic",
    "_attach_numbering",
    # Cell & table helpers (re-export)
    "clean_cell_p", "set_cell_margins", "set_cell_shading",
    "set_cell_bottom_border", "set_table_borders", "add_table_bordered",
    "add_table_with_subheader", "set_table_flush_alignment",
    # Other builders & audits (re-export)
    "add_signature_block", "add_cover_page", "add_daftar_isi", "add_page_break",
    "audit_text_deterministic", "audit_docx_deterministic",
    # Helper khusus naskah dinas
    "add_kop_surat",
    "add_kop_surat_table",
    "add_surat_pengantar_metadata",
    "add_nota_dinas_header",
    "add_surat_tugas_header",
    "add_lembar_pengesahan",
    "add_tte_marker",
    "get_default_logo",
    # Builder notisi pembahasan
    "build_notisi_pembahasan",
    "build_notisi_temuan_5c",
]

# =====================================================================
# HELPER PATH ASET (LOGO BPKP)
# =====================================================================

def get_default_logo(variant: str = "png") -> str:
    """
    Kembalikan path absolut ke file logo BPKP yang dibundel di folder
    ``assets/`` skill ini.

    Semua varian menggunakan master logo PNG transparan (assets/logo_bpkp.png)
    untuk kualitas render terbaik di kop surat dan cover page.

    Mengembalikan string kosong jika file tidak ditemukan.
    """
    _here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(_here, "..", "assets", "logo_bpkp.png")
    path = os.path.normpath(path)
    return path if os.path.exists(path) else ""


# =====================================================================
# KOP SURAT (LETTERHEAD) BPKP
# =====================================================================

def add_kop_surat(doc, unit_kerja: str, alamat: str = "", telepon: str = "",
                  email: str = "", website: str = "",
                  kode_pos: str = "", lembaga: str = "BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN"):
    """
    Tambahkan kop surat (letterhead) BPKP versi paragraf sederhana.

    Untuk kop surat resmi dengan logo dan garis bawah tebal, gunakan
    fungsi ``add_kop_surat_table``.

    Layout:
      Baris 1: LEMBAGA (huruf besar, bold 14pt, tengah)
      Baris 2: UNIT KERJA (huruf besar, bold 12pt, tengah)
      Baris 3: Alamat lengkap (italic 10pt, tengah)
      Garis pembatas tebal (bottom border sz=18)
    """
    # Baris 1: Nama Lembaga
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(lembaga)
    _apply_font(r1, bold=True, size=Pt(14))

    # Baris 2: Unit Kerja
    if unit_kerja:
        p2 = doc.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(0)
        r2 = p2.add_run(unit_kerja.upper())
        _apply_font(r2, bold=True, size=Pt(12))

    # Baris 3: Alamat
    alamat_parts = [alamat]
    if telepon:
        alamat_parts.append(f"Telp. {telepon}")
    if email:
        alamat_parts.append(f"Email: {email}")
    if website:
        alamat_parts.append(f"Website: {website}")
    alamat_line = " | ".join(part for part in alamat_parts if part)
    if kode_pos:
        alamat_line = f"{alamat_line} - Kode Pos {kode_pos}" if alamat_line else f"Kode Pos {kode_pos}"

    if alamat_line:
        p3 = doc.add_paragraph()
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p3.paragraph_format.space_before = Pt(0)
        p3.paragraph_format.space_after = Pt(0)
        r3 = p3.add_run(alamat_line)
        _apply_font(r3, italic=True, size=Pt(10))

    # Garis pembatas tebal (bottom border pada paragraf kosong)
    p_line = doc.add_paragraph()
    p_line.paragraph_format.space_before = Pt(0)
    p_line.paragraph_format.space_after = Pt(6)
    pPr = p_line._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="18" w:space="1" w:color="000000"/>'
        f'</w:pBdr>'
    )
    pPr.append(pBdr)


# =====================================================================
# KOP SURAT TABLE (dengan Logo + Garis Bawah)
# =====================================================================

def add_kop_surat_table(doc, logo_path: str = "",
                        lembaga: str = "BADAN PENGAWASAN KEUANGAN DAN PEMBANGUNAN",
                        unit_kerja: str = "PERWAKILAN PROVINSI PAPUA TENGAH",
                        alamat: str = "Jalan Sam Ratulangi, Kelurahan Oyehe, Distrik Nabire",
                        wilayah: str = "Kabupaten Nabire, Provinsi Papua Tengah, Kode Pos: 98816",
                        kontak: str = "Email: papua.tengah@bpkp.go.id, Website: www.bpkp.go.id/papua.tengah"):
    """
    Tambahkan kop surat (letterhead) BPKP versi tabel resmi dengan logo.

    Layout (tabel 1 baris x 2 kolom, borderless, dengan border bawah tebal):
      Kolom kiri  (3.2 cm): Logo BPKP (center)
      Kolom kanan (12.8 cm): 5 baris teks instansi
        - Baris 1: NAMA LEMBAGA       (bold 12pt, center, line 1.0)
        - Baris 2: UNIT KERJA          (bold 12pt, center, line 1.0)
        - Baris 3: Alamat jalan        (regular 10pt, center, line 1.0)
        - Baris 4: Wilayah + kode pos  (regular 10pt, center, line 1.0)
        - Baris 5: Email + Website     (regular 10pt, center, line 1.0)
      Garis bawah solid tebal (sz=18, hitam) pada kedua sel.
    """
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Borderless tabel, kecuali bottom border tebal di level tabel
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:bottom w:val="single" w:sz="18" w:space="0" w:color="000000"/>'
        f'<w:insideH w:val="none"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    # Kolom kiri: Logo
    cell_logo = table.cell(0, 0)
    cell_logo.width = Cm(3.2)
    set_cell_margins(cell_logo, top=40, bottom=80, left=40, right=40)
    set_cell_bottom_border(cell_logo, color="000000", sz="18")

    p_klogo = cell_logo.paragraphs[0]
    p_klogo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_klogo.paragraph_format.space_before = Pt(0)
    p_klogo.paragraph_format.space_after = Pt(2)
    clean_cell_p(p_klogo)
    # Gunakan logo default jika tidak diberikan
    if not logo_path:
        logo_path = get_default_logo(variant="jpg")
    if logo_path and os.path.exists(logo_path):
        r_klogo = p_klogo.add_run()
        # Kop Jabatan: logo 34x17 mm; Kop dengan alamat: logo 32x16 mm (Perban 4/2026 BAB II.A)
        r_klogo.add_picture(logo_path, width=Cm(3.2), height=Cm(1.6))

    # Kolom kanan: Teks instansi
    cell_ktxt = table.cell(0, 1)
    cell_ktxt.width = Cm(12.8)
    set_cell_margins(cell_ktxt, top=30, bottom=80, left=40, right=40)
    set_cell_bottom_border(cell_ktxt, color="000000", sz="18")

    lines = [
        {"text": lembaga, "bold": True, "size": 12, "sa": 1},
        {"text": unit_kerja, "bold": True, "size": 12, "sa": 3},
        {"text": alamat, "bold": False, "size": 10, "sa": 1},
        {"text": wilayah, "bold": False, "size": 10, "sa": 1},
        {"text": kontak, "bold": False, "size": 10, "sa": 4},
    ]
    for i, line in enumerate(lines):
        if i == 0:
            p = cell_ktxt.paragraphs[0]
        else:
            p = cell_ktxt.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(line["sa"])
        p.paragraph_format.line_spacing = 1.0
        clean_cell_p(p)
        add_run(p, line["text"], bold=line["bold"], size=Pt(line["size"]))

    # Ultra-thin separator paragraph
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(0)
    p_sep.paragraph_format.space_after = Pt(4)
    pPr_sep = p_sep._p.get_or_add_pPr()
    pPr_sep.append(parse_xml(
        f'<w:spacing {nsdecls("w")} w:before="0" w:after="80" w:line="40" w:lineRule="exact"/>'
    ))
    r_sep = p_sep.add_run()
    rPr_sep = r_sep._r.get_or_add_rPr()
    rPr_sep.append(parse_xml(f'<w:sz {nsdecls("w")} w:val="2"/>'))
    rPr_sep.append(parse_xml(f'<w:szCs {nsdecls("w")} w:val="2"/>'))


# =====================================================================
# TABEL METADATA SURAT PENGANTAR (4 Kolom)
# =====================================================================

def add_surat_pengantar_metadata(doc, nomor: str, lampiran: str, hal: str,
                                 tanggal: str = ""):
    """
    Tambahkan tabel metadata surat pengantar (4 kolom) standar BPKP.

    Layout (tabel 3 baris x 4 kolom, borderless):
      Kolom 1 (2.43 cm): Label (Nomor, Lampiran, Hal)      — left, 11pt
      Kolom 2 (0.63 cm): Separator ':'                      — center, 11pt
      Kolom 3 (8.39 cm): Isi teks                            — justified, 11pt
      Kolom 4 (4.58 cm): Tanggal (hanya baris pertama)       — right, 11pt

    Aturan: Tanggal ditempatkan pada kolom ke-4 mandiri agar judul
    laporan pada baris 'Hal' tidak mengalami hanging indent.
    """
    table = doc.add_table(rows=3, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    # Borderless
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/><w:left w:val="none"/>'
        f'<w:right w:val="none"/><w:bottom w:val="none"/>'
        f'<w:insideH w:val="none"/><w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

    meta_w = [Cm(2.43), Cm(0.63), Cm(8.39), Cm(4.58)]
    meta_rows = [
        ("Nomor", ":", nomor, tanggal),
        ("Lampiran", ":", lampiran, ""),
        ("Hal", ":", hal, ""),
    ]

    for r_idx, (label, sep, content, date_val) in enumerate(meta_rows):
        cells = table.rows[r_idx].cells
        for c_idx, w in enumerate(meta_w):
            cells[c_idx].width = w
            set_cell_margins(cells[c_idx], top=20, bottom=20, left=10, right=10)

        # Col 0: Label
        p0 = cells[0].paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(2)
        p0.paragraph_format.line_spacing = 1.15
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        clean_cell_p(p0)
        add_run(p0, label, bold=False, size=Pt(11))

        # Col 1: Separator ':'
        p1 = cells[1].paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(2)
        p1.paragraph_format.line_spacing = 1.15
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        clean_cell_p(p1)
        add_run(p1, sep, bold=False, size=Pt(11))

        # Col 2: Content
        p2 = cells[2].paragraphs[0]
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(2)
        p2.paragraph_format.line_spacing = 1.15
        p2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        clean_cell_p(p2)
        add_run(p2, content, bold=False, size=Pt(11))

        # Col 3: Tanggal (kanan)
        p3 = cells[3].paragraphs[0]
        p3.paragraph_format.space_before = Pt(0)
        p3.paragraph_format.space_after = Pt(2)
        p3.paragraph_format.line_spacing = 1.15
        p3.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        clean_cell_p(p3)
        if date_val:
            add_run(p3, date_val, bold=False, size=Pt(11))


# =====================================================================
# NOTA DINAS - HEADER
# =====================================================================

def add_nota_dinas_header(doc, nomor: str, sifat: str = "Biasa",
                          lampiran: str = "-", hal: str = "",
                          kepada: str = "", dari: str = "",
                          tempat_tanggal: str = ""):
    """
    Tambahkan header nota dinas standar BPKP.

    Layout (tabel 2 kolom):
      Kiri: Nomor, Sifat, Lampiran, Hal
      Kanan: Kepada (yth), Dari, Tempat/Tanggal
    """
    table = doc.add_table(rows=5, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color="FFFFFF", val="none")  # borderless

    # Lebar kolom: kiri 7 cm, kanan 9 cm
    for row in table.rows:
        row.cells[0].width = Cm(7)
        row.cells[1].width = Cm(9)

    labels_left = ["Nomor", "Sifat", "Lampiran", "Hal"]
    values_left = [nomor, sifat, lampiran, hal]
    labels_right = ["Kepada Yth.", "", "Dari", "Tempat/Tanggal"]
    values_right = [kepada, "", dari, tempat_tanggal]

    for i in range(4):
        # Kolom kiri
        cell_l = table.rows[i].cells[0]
        set_cell_margins(cell_l, top=40, bottom=40, left=0, right=100)
        p_l = cell_l.paragraphs[0]
        clean_cell_p(p_l)
        p_l.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        add_run(p_l, f"{labels_left[i]} : ", bold=False, size=Pt(12))
        add_run(p_l, values_left[i], bold=False, size=Pt(12))

        # Kolom kanan
        cell_r = table.rows[i].cells[1]
        set_cell_margins(cell_r, top=40, bottom=40, left=100, right=0)
        p_r = cell_r.paragraphs[0]
        clean_cell_p(p_r)
        p_r.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_r.paragraph_format.space_before = Pt(2)
        p_r.paragraph_format.space_after = Pt(0)
        if labels_right[i]:
            add_run(p_r, f"{labels_right[i]} : ", bold=False, size=Pt(12))
        add_run(p_r, values_right[i], bold=False, size=Pt(12))

    # Baris terakhir: garis pemisah
    cell_sep = table.rows[4].cells[0]
    # Merge seluruh baris terakhir
    cell_sep.merge(table.rows[4].cells[1])
    set_cell_margins(cell_sep, top=0, bottom=0, left=0, right=0)
    p_sep = cell_sep.paragraphs[0]
    clean_cell_p(p_sep)
    p_sep.paragraph_format.space_before = Pt(6)
    p_sep.paragraph_format.space_after = Pt(0)
    pPr_sep = p_sep._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="6" w:space="1" w:color="000000"/>'
        f'</w:pBdr>'
    )
    pPr_sep.append(pBdr)


# =====================================================================
# SURAT TUGAS - HEADER
# =====================================================================

def add_surat_tugas_header(doc, nomor: str, sifat: str = "Biasa",
                           lampiran: str = "-", hal: str = "Surat Tugas"):
    """
    Tambahkan header surat tugas standar BPKP.
    Mirip dengan nota dinas namun lebih sederhana (tanpa Dari/Kepada).
    """
    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color="FFFFFF", val="none")

    for row in table.rows:
        row.cells[0].width = Cm(3.5)
        row.cells[1].width = Cm(12.5)

    labels = ["Nomor", "Sifat", "Lampiran", "Hal"]
    values = [nomor, sifat, lampiran, hal]

    for i in range(4):
        cell_l = table.rows[i].cells[0]
        set_cell_margins(cell_l, top=40, bottom=40, left=0, right=100)
        p_l = cell_l.paragraphs[0]
        clean_cell_p(p_l)
        p_l.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_l.paragraph_format.space_before = Pt(0)
        p_l.paragraph_format.space_after = Pt(0)
        add_run(p_l, f"{labels[i]} : ", bold=False, size=Pt(12))
        add_run(p_l, values[i], bold=False, size=Pt(12))

        # Kolom kanan kosong (untuk surat tugas, info pejabat ada di body)
        cell_r = table.rows[i].cells[1]
        set_cell_margins(cell_r, top=40, bottom=40, left=0, right=0)
        p_r = cell_r.paragraphs[0]
        clean_cell_p(p_r)
        add_run(p_r, "", size=Pt(12))

    # Garis pemisah
    p_sep = doc.add_paragraph()
    p_sep.paragraph_format.space_before = Pt(6)
    p_sep.paragraph_format.space_after = Pt(6)
    pPr_sep = p_sep._p.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'<w:bottom w:val="single" w:sz="6" w:space="1" w:color="000000"/>'
        f'</w:pBdr>'
    )
    pPr_sep.append(pBdr)


# =====================================================================
# LEMBAR PENGESAHAN
# =====================================================================

def add_lembar_pengesahan(doc, judul_laporan: str, tempat_tanggal: str = "",
                          pejabat_list: Optional[List[dict]] = None):
    """
    Tambahkan halaman Lembar Pengesahan standar BPKP.

    pejabat_list: list of dict dengan keys:
      - nama    : nama pejabat
      - jabatan : jabatan pejabat
      - nip     : NIP pejabat (opsional)
    """
    if pejabat_list is None:
        pejabat_list = []

    # Judul
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("LEMBAR PENGESAHAN")
    _apply_font(r_title, bold=True, size=Pt(14))

    # Judul laporan
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run(judul_laporan)
    _apply_font(r_sub, bold=True, size=Pt(12))

    # Tabel pengesahan
    n_rows = max(len(pejabat_list), 1) + 1  # +1 untuk header
    table = doc.add_table(rows=n_rows, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_borders(table, color="000000", sz="6")

    col_widths = [Cm(6), Cm(7), Cm(4)]
    for row in table.rows:
        for i, w in enumerate(col_widths):
            row.cells[i].width = w

    # Header
    headers = ["Nama", "Jabatan", "Tanda Tangan"]
    hdr = table.rows[0].cells
    for i, h in enumerate(headers):
        set_cell_margins(hdr[i], top=100, bottom=100, left=100, right=100)
        set_cell_shading(hdr[i], "EAEAEA")
        p = hdr[i].paragraphs[0]
        clean_cell_p(p)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_run(p, h, bold=True, size=Pt(11))

    # Isi
    for idx, pj in enumerate(pejabat_list, 1):
        row_cells = table.rows[idx].cells
        for c_idx in range(3):
            set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=100, right=100)
            p = row_cells[c_idx].paragraphs[0]
            clean_cell_p(p)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        add_run(row_cells[0].paragraphs[0], pj.get("nama", ""), size=Pt(11))
        add_run(row_cells[1].paragraphs[0], pj.get("jabatan", ""), size=Pt(11))
        # Kolom tanda tangan dibiarkan kosong
        add_run(row_cells[2].paragraphs[0], "", size=Pt(11))

    # Tempat/tanggal dan tanda tangan di bawah tabel
    if tempat_tanggal:
        add_p(doc, "", space_before=Pt(24))
        p_date = doc.add_paragraph()
        p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_date.paragraph_format.space_before = Pt(0)
        p_date.paragraph_format.space_after = Pt(0)
        r_date = p_date.add_run(tempat_tanggal)
        _apply_font(r_date, size=Pt(12))

        p_role = doc.add_paragraph()
        p_role.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_role.paragraph_format.space_before = Pt(0)
        p_role.paragraph_format.space_after = Pt(48)  # space untuk TTE
        r_role = p_role.add_run(pejabat_list[0].get("jabatan", "") if pejabat_list else "")
        _apply_font(r_role, size=Pt(12))

        # TTE marker
        add_tte_marker(doc)

        p_name = doc.add_paragraph()
        p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_name.paragraph_format.space_before = Pt(0)
        p_name.paragraph_format.space_after = Pt(0)
        r_name = p_name.add_run(pejabat_list[0].get("nama", "") if pejabat_list else "")
        _apply_font(r_name, bold=True, size=Pt(12))

        p_nip = doc.add_paragraph()
        p_nip.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_nip.paragraph_format.space_before = Pt(0)
        p_nip.paragraph_format.space_after = Pt(0)
        nip_text = pejabat_list[0].get("nip", "")
        if nip_text:
            r_nip = p_nip.add_run(f"NIP. {nip_text}")
            _apply_font(r_nip, size=Pt(12))


# =====================================================================
# TTE MARKER (Tanda Tangan Elektronik)
# =====================================================================

def add_tte_marker(doc):
    """
    Tambahkan placeholder Tanda Tangan Elektronik (TTE).
    Diberi warna abu-abu italic sebagai indikasi visual.
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run("[Tanda Tangan Elektronik]")
    _apply_font(r, italic=True, color=RGBColor(89, 89, 89), size=Pt(10))


# =====================================================================
# BUILDER NOTISI PEMBAHASAN
# =====================================================================
#
# Notisi Pembahasan adalah Naskah Dinas Khusus (Dokumentasi Pengawasan)
# tanpa nomor, tanpa kode jenis. Berisi hasil pembahasan evaluasi dengan
# struktur: Kepala (kop + tanggal + pembehasan) -> Batang Tubuh
# (A. Hasil Laporan Evaluasi -> butir-butir temuan) -> Kaki (tanda tangan).
#
# Butir temuan memakai multilevel numbering native Word:
#   - Heading 2 level 0: A.  (seksi utama)
#   - Heading 3 level 1: 1.  (butir temuan -- judul)
#   - Paragraf narasi 5C sejajar indent level 1 (1,25" / 1800 dxa)
# =====================================================================

from docx.shared import Inches as _Inches
from docx.shared import Pt as _Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH as _WAP


def build_notisi_pembahasan(
    doc,
    judul_utama: str,
    opening_text: str,
    temuan_list,
    closing_text: str,
    signature_left: list = None,
    signature_right: list = None,
    tanggal: str = "",
    sections: list = None,
):
    """
    Bangun Notisi Pembahasan hasil evaluasi standar BPKP.

    Parameter
    ---------
    doc : Document (hasil create_document())
    judul_utama : str  -- judul notisi (mis. "NOTISI PEMBAHASAN")
    opening_text : str  -- paragraf pembuka (tanggal & dasar surat tugas)
    temuan_list : list[dict]
        Setiap dict dengan keys:
          - title : str  -- judul butir temuan (TANPA nomor manual)
          - kondisi : str
          - sebab : str
          - akibat : str
          - rekomendasi : str
          - table : dict | None  (headers, rows, widths)
    closing_text : str
    signature_left / signature_right : list[(text, opts)]
    tanggal : str  -- tempat & tanggal notisi (mis. "Nabire, 7 September 2026")
    sections : list[(str, list[dict])] | None
        Jika diberikan, akan membuat beberapa Heading 2 bersesuaian
        (mis. [("Cadangan Pangan", [...]), ("Stabilisasi Harga", [...])]).
        Setiap elemen: (judul_seksi, daftar_temuan).
        Jika None, pakai temuan_list dengan heading "Hasil Laporan Evaluasi".
    """
    # Heading 2 untuk seksi A (restart numbering semua level)
    nid = new_bab_context(doc, "NOTISI")

    # --- Kepala Notisi ---
    if judul_utama:
        add_heading_1(doc, judul_utama)

    add_p(doc, opening_text, space_before=_Pt(0), space_after=_Pt(12),
          align=_WAP.JUSTIFY)

    if sections:
        # --- Multi-section mode (A. ..., B. ...) ---
        for sec_title, sec_temuan in sections:
            add_heading_2(doc, sec_title, num_id=nid)
            for f in sec_temuan:
                build_notisi_temuan_5c(doc, f, num_id=nid)
    else:
        # --- Seksi A. Hasil Laporan Evaluasi (Heading 2 + numbering level 0) ---
        add_heading_2(doc, "Hasil Laporan Evaluasi", num_id=nid)

        # --- Butir-butir temuan (Heading 3 + numbering level 1) ---
        for f in temuan_list:
            build_notisi_temuan_5c(doc, f, num_id=nid)

    # --- Kaki / Penutup ---
    add_p(doc, "", space_after=_Pt(4))
    add_p(doc, closing_text, space_after=_Pt(24), align=_WAP.JUSTIFY)

    # --- Blok tanda tangan ---
    _add_signature_grid(doc, signature_left, signature_right, tanggal)


def build_notisi_temuan_5c(doc, temuan: dict, num_id: int):
    """
    Bangun satu butir temuan pada Notisi Pembahasan.

    Struktur per butir (auto-numbering 1., 2., ...):
      [Heading 3 + num_id level 1] <judul temuan>
      [paragraf kondisi]  -- sejajar indent level 1 (1,25" / 1800 dxa)
      [tabel data bila ada]
      [paragraf sebab]
      [paragraf akibat]
      [paragraf rekomendasi]
    """
    judul = temuan.get("title", "")
    kondisi = temuan.get("kondisi", "")
    sebab = temuan.get("sebab", "")
    akibat = temuan.get("akibat", "")
    rekom = temuan.get("rekom", "")
    table_data = temuan.get("table")

    # Judul butir temuan: Heading 3 + numbering level 1 (1.)
    # Word akan men-generate "1.", "2.", ... secara otomatis.
    add_topic_heading(doc, judul, num_id=num_id, ilvl=1)

    # Paragraf Kondisi (sejajar indent teks level 1)
    add_body_sub(doc, kondisi, num_id=num_id, ilvl=1)

    # Tabel pendukung bila ada
    if table_data:
        headers = table_data.get("headers", [])
        rows = table_data.get("rows", [])
        widths = table_data.get("widths", [])
        col_widths = [Cm(w) for w in widths] if widths else None
        _add_data_table(doc, headers, rows, col_widths)
        add_p(doc, "", space_after=_Pt(2))

    # Paragraf Sebab (sejajar indent level 1)
    # Data temuan sudah memuat awalan "Hal ini disebabkan oleh", jadi pakai add_p
    # biasa (bukan add_cause yang menambah awalan baku) untuk menghindari duplikasi.
    add_p(doc, sebab, space_after=_Pt(6), num_id=num_id, ilvl=1,
          align=_WAP.JUSTIFY)

    # Paragraf Akibat
    # Data temuan sudah memuat awalan "Akibatnya,".
    add_p(doc, akibat, space_after=_Pt(6), num_id=num_id, ilvl=1,
          align=_WAP.JUSTIFY)

    # Paragraf Rekomendasi
    add_p(doc, rekom, space_after=_Pt(6), num_id=num_id, ilvl=1,
          align=_WAP.JUSTIFY)

    # Baris Tanggapan (placeholder untuk Mitra Evaluasi)
    add_p(doc, "Tanggapan :", space_before=_Pt(2), space_after=_Pt(2),
          num_id=num_id, ilvl=1, bold=True, align=_WAP.LEFT)
    add_p(
        doc,
        "\u2026" * 120,
        space_after=_Pt(10),
        num_id=num_id,
        ilvl=1,
        align=_WAP.LEFT,
    )


def _add_data_table(doc, headers, rows, col_widths):
    """Bungkus add_table_bordered untuk data table notisi.

    Tabel diindentasi sejajar dengan hanging indent level 1 (1080 dxa = 0.75").
    """
    from docx.oxml import parse_xml as _parse_xml
    from docx.oxml.ns import nsdecls as _nsdecls

    n_cols = len(headers)
    n_rows = 1 + len(rows)
    table, rows_data = add_table_bordered(
        doc, rows=n_rows, cols=n_cols,
        col_widths=col_widths, header_rows=1,
        shade_header="EAEAEA", border_color="B0B0B0"
    )
    # Set table indent to align with hanging indent level 1 (1080 dxa)
    tbl = table._tbl
    tblPr = tbl.tblPr
    tblInd = _parse_xml(
        f'<w:tblInd {_nsdecls("w")} w:w="1080" w:type="dxa"/>'
    )
    tblPr.append(tblInd)
    # Isi header (bold, center)
    for i, h in enumerate(headers):
        cell = rows_data[0][i]
        p = cell.paragraphs[0]
        p.alignment = _WAP.CENTER
        add_run(p, h, bold=True, size=_Pt(10))
    # Isi data
    for r_idx, row_vals in enumerate(rows, 1):
        for c_idx, val in enumerate(row_vals):
            cell = rows_data[r_idx][c_idx]
            p = cell.paragraphs[0]
            if c_idx == 0:
                p.alignment = _WAP.CENTER
            else:
                p.alignment = _WAP.LEFT
            add_run(p, str(val), size=_Pt(10))


def _add_signature_grid(doc, left_lines, right_lines, tanggal=""):
    """
    Tambahkan grid tanda tangan dua kolom (borderless) di akhir notisi.
    left_lines / right_lines : list of (text, opts_dict)
    """
    from docx.enum.table import WD_TABLE_ALIGNMENT as _WDTA
    from docx.oxml import parse_xml as _parse_xml
    from docx.oxml.ns import nsdecls as _nsdecls

    if not left_lines and not right_lines:
        return

    table = doc.add_table(rows=1, cols=2)
    table.alignment = _WDTA.CENTER
    left, right = table.rows[0].cells
    left.width = Cm(8.5)
    right.width = Cm(8.5)

    for cell, lines in ((left, left_lines or []), (right, right_lines or [])):
        cell.text = ""
        first = True
        for text, opts in lines:
            p = cell.paragraphs[0] if first else cell.add_paragraph()
            first = False
            p.alignment = _WAP.CENTER
            p.paragraph_format.space_after = _Pt(0)
            p.paragraph_format.space_before = _Pt(0)
            p.paragraph_format.line_spacing = 1.15
            # add_run engine tidak mendukung underline; terapkan manual
            r = p.add_run(text)
            _apply_font(
                r,
                bold=opts.get("bold", False),
                italic=opts.get("italic", False),
                color=opts.get("color", BLACK),
                size=opts.get("size", _Pt(12)),
            )
            if opts.get("underline", False):
                r.font.underline = True

    # Borderless
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = _parse_xml(
        f'<w:tblBorders {_nsdecls("w")}>'
        f'<w:top w:val="none"/><w:left w:val="none"/>'
        f'<w:bottom w:val="none"/><w:right w:val="none"/>'
        f'<w:insideH w:val="none"/><w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


print("naskah_dinas_helper.py loaded - BPKP Tata Naskah Dinas helper ready.")


# =====================================================================
# STANDAR STYLE HEADINGS (ARIAL 12 PT BOLD HITAM) & NAVIGASI PANEL
# =====================================================================
#
# Fungsi setup_heading_styles, add_heading_1, add_heading_2,
# add_heading_3, add_heading_4 sudah diimpor langsung dari
# bpkp_docx_engine di blok atas dan ikut di-export via __all__.
# Tidak perlu redefinisi/alias terpisah di sini.
# =====================================================================
