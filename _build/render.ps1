# Render a .pptx with the locally installed PowerPoint:
#   - re-save with TrueType fonts embedded (so Constantia / Segoe UI travel with the file)
#   - export PDF
#   - export every slide as PNG (1920x1080)
# Usage: powershell -ExecutionPolicy Bypass -File render.ps1 -Pptx deck.pptx -Pdf out.pdf -PngDir dir [-Embed]
param(
  [Parameter(Mandatory = $true)][string]$Pptx,
  [string]$Pdf = "",
  [string]$PngDir = "",
  [switch]$Embed
)
$ErrorActionPreference = "Stop"
$Pptx = (Resolve-Path $Pptx).Path

# Make the deck fonts (Phudu, Be Vietnam Pro — 12_assets/fonts/src) available to PowerPoint for this Windows session,
# even if the per-user font install has not been loaded yet. Nothing is copied or installed.
$fontDir = Join-Path (Split-Path $PSScriptRoot -Parent) "12_assets\fonts\src"
if (Test-Path $fontDir) {
  Add-Type -TypeDefinition @"
using System; using System.Runtime.InteropServices;
public static class DeckFonts {
  [DllImport("gdi32.dll", CharSet = CharSet.Unicode)] public static extern int AddFontResource(string file);
  [DllImport("user32.dll", CharSet = CharSet.Auto)] public static extern IntPtr SendMessageTimeout(IntPtr h, uint m, UIntPtr w, IntPtr l, uint f, uint t, out UIntPtr r);
}
"@ -ErrorAction SilentlyContinue
  $loaded = 0
  Get-ChildItem $fontDir -Filter "*.ttf" | Where-Object { $_.Name -notmatch "VF" } | ForEach-Object { $loaded += [DeckFonts]::AddFontResource($_.FullName) }
  $res = [UIntPtr]::Zero
  [void][DeckFonts]::SendMessageTimeout([IntPtr]0xffff, 0x001D, [UIntPtr]::Zero, [IntPtr]::Zero, 2, 2000, [ref]$res)
  Write-Output "fonts loaded for this session: $loaded"
}
$ppt = New-Object -ComObject PowerPoint.Application
try {
  # Open(FileName, ReadOnly, Untitled, WithWindow)
  $pres = $ppt.Presentations.Open($Pptx, 0, 0, 0)
  if ($Embed) {
    # SaveAs(FileName, ppSaveAsOpenXMLPresentation=24, EmbedTrueTypeFonts=msoTrue(-1))
    $pres.SaveAs($Pptx, 24, -1)
    Write-Output "saved with embedded fonts: $Pptx"
  }
  if ($Pdf -ne "") {
    $pdfFull = [System.IO.Path]::GetFullPath($Pdf)
    $pres.SaveAs($pdfFull, 32)   # ppSaveAsPDF
    Write-Output "pdf: $pdfFull"
  }
  if ($PngDir -ne "") {
    $dir = [System.IO.Path]::GetFullPath($PngDir)
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    Get-ChildItem $dir -Filter "slide-*.png" -ErrorAction SilentlyContinue | Remove-Item -Force
    $n = $pres.Slides.Count
    for ($i = 1; $i -le $n; $i++) {
      $f = Join-Path $dir ("slide-{0:D2}.png" -f $i)
      $pres.Slides.Item($i).Export($f, "PNG", 1920, 1080)
    }
    Write-Output "png: $n slides -> $dir"
  }
  $pres.Close()
}
finally {
  $ppt.Quit()
  [System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
}
