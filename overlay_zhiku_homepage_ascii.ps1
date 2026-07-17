Add-Type -AssemblyName System.Drawing

$basePath = "zhiku_homepage_base.png"
$mallPath = "mall_insert.png"
$expertPath = "expert_insert.png"
$outPath = "zhiku_homepage_screenshot.png"

function Draw-CoverImage($g, $img, [int]$x, [int]$y, [int]$w, [int]$h) {
    $srcRatio = $img.Width / $img.Height
    $dstRatio = $w / $h
    if ($srcRatio -gt $dstRatio) {
        $sw = [int]($img.Height * $dstRatio)
        $sx = [int](($img.Width - $sw) / 2)
        $src = New-Object System.Drawing.Rectangle($sx, 0, $sw, $img.Height)
    } else {
        $sh = [int]($img.Width / $dstRatio)
        $sy = [int](($img.Height - $sh) / 2)
        $src = New-Object System.Drawing.Rectangle(0, $sy, $img.Width, $sh)
    }
    $dst = New-Object System.Drawing.Rectangle($x, $y, $w, $h)
    $g.DrawImage($img, $dst, $src, [System.Drawing.GraphicsUnit]::Pixel)
}

$base = [System.Drawing.Image]::FromFile((Resolve-Path $basePath))
$bmp = New-Object System.Drawing.Bitmap $base.Width, $base.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.DrawImage($base, 0, 0, $base.Width, $base.Height)

$mall = [System.Drawing.Image]::FromFile((Resolve-Path $mallPath))
$expert = [System.Drawing.Image]::FromFile((Resolve-Path $expertPath))

$white = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::White)
$g.FillRectangle($white, 1432, 129, 446, 230)
Draw-CoverImage $g $mall 1458 145 392 238

$g.FillRectangle($white, 1432, 381, 446, 432)
Draw-CoverImage $g $expert 1458 404 396 254

# Remove the small pinned-post note and the partially visible task card.
$panelBrush = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(248, 250, 252))
$g.FillRectangle($white, 1080, 708, 330, 40)
$g.FillRectangle($panelBrush, 1432, 836, 446, 45)

$bmp.Save((Join-Path (Get-Location) $outPath), [System.Drawing.Imaging.ImageFormat]::Png)

$expert.Dispose()
$mall.Dispose()
$white.Dispose()
$g.Dispose()
$bmp.Dispose()
$base.Dispose()

Write-Output (Join-Path (Get-Location) $outPath)
