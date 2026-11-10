<#
Render .docx ke PDF memakai Microsoft Word (COM), sama seperti tampilan yang dilihat pembaca.

Pemakaian (PowerShell):
  powershell -ExecutionPolicy Bypass -File render_pdf.ps1 -Docx "D:\folder\Laporan (Draf v3).docx" -Pdf "C:\scratch\draf_v3.pdf"

Dokumen dibuka read-only sehingga berkas asli tidak berubah. Simpan PDF hasil reviu di folder kerja
(scratchpad), bukan di folder pengguna, kecuali PDF itu memang akan diserahkan.
Bila Word tidak tersedia: soffice --headless --convert-to pdf --outdir <folder> <berkas.docx>
#>
param(
  [Parameter(Mandatory = $true)][string]$Docx,
  [string]$Pdf
)
$Docx = (Resolve-Path -LiteralPath $Docx).Path
if (-not $Pdf) { $Pdf = [IO.Path]::ChangeExtension($Docx, '.pdf') }
$Pdf = [IO.Path]::GetFullPath($Pdf)
$w = New-Object -ComObject Word.Application
$w.Visible = $false
$w.DisplayAlerts = 0
try {
  $d = $w.Documents.Open($Docx, $false, $true)
  $d.SaveAs([ref]$Pdf, [ref]17)
  $n = $d.ComputeStatistics(2)
  $d.Close([ref]0)
  "PDF: $Pdf"
  "Halaman: $n"
} finally {
  $w.Quit()
}
