# Draws resources/icon/icon.jpg (256x256, the NRO / forwarder icon): the app's own orange-pink
# play disc on a dark-red gradient, with "ยูทูปไทย" under it. Windows' text engine shapes the
# Thai vowels and tone marks correctly.
param([string]$Out = (Join-Path $PSScriptRoot '..\resources\icon\icon.jpg'), [string]$Preview = '')
Add-Type -AssemblyName System.Drawing

$size = 256
$bmp = New-Object Drawing.Bitmap $size, $size
$g = [Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = 'AntiAlias'
$g.TextRenderingHint = 'AntiAliasGridFit'
$g.InterpolationMode = 'HighQualityBicubic'

# background: deep wine to near black
$bg = New-Object Drawing.Drawing2D.LinearGradientBrush (New-Object Drawing.Point 0, 0), (New-Object Drawing.Point 0, $size), ([Drawing.Color]::FromArgb(122, 20, 60)), ([Drawing.Color]::FromArgb(24, 10, 20))
$g.FillRectangle($bg, 0, 0, $size, $size)

# play disc (the app's gradient) with a soft shadow
$disc = New-Object Drawing.Rectangle 68, 26, 120, 120
$shadow = New-Object Drawing.SolidBrush ([Drawing.Color]::FromArgb(90, 0, 0, 0))
$g.FillEllipse($shadow, $disc.X + 3, $disc.Y + 6, $disc.Width, $disc.Height)
$discBrush = New-Object Drawing.Drawing2D.LinearGradientBrush $disc, ([Drawing.Color]::FromArgb(255, 138, 36)), ([Drawing.Color]::FromArgb(233, 30, 99)), 45
$g.FillEllipse($discBrush, $disc)

# rounded white triangle
$cx = $disc.X + $disc.Width / 2 + 6; $cy = $disc.Y + $disc.Height / 2
$tri = [Drawing.PointF[]]@(
    (New-Object Drawing.PointF ($cx - 20), ($cy - 26)),
    (New-Object Drawing.PointF ($cx + 26), $cy),
    (New-Object Drawing.PointF ($cx - 20), ($cy + 26)))
$pen = New-Object Drawing.Pen ([Drawing.Color]::White), 12
$pen.LineJoin = 'Round'
$g.DrawPolygon($pen, $tri)
$g.FillPolygon([Drawing.Brushes]::White, $tri)

# title and shop line
$fmt = New-Object Drawing.StringFormat
$fmt.Alignment = 'Center'
$title = New-Object Drawing.Font 'Leelawadee UI', 34, ([Drawing.FontStyle]::Bold), ([Drawing.GraphicsUnit]::Pixel)
$g.DrawString('ยูทูปไทย', $title, [Drawing.Brushes]::White, (New-Object Drawing.RectangleF 0, 158, $size, 50), $fmt)
$small = New-Object Drawing.Font 'Leelawadee UI', 15, ([Drawing.FontStyle]::Bold), ([Drawing.GraphicsUnit]::Pixel)
$tint = New-Object Drawing.SolidBrush ([Drawing.Color]::FromArgb(255, 176, 120))
$g.DrawString('by Ommamm', $small, $tint, (New-Object Drawing.RectangleF 0, 210, $size, 24), $fmt)
$g.Dispose()

$codec = [Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object MimeType -eq 'image/jpeg'
$params = New-Object Drawing.Imaging.EncoderParameters 1
$params.Param[0] = New-Object Drawing.Imaging.EncoderParameter ([Drawing.Imaging.Encoder]::Quality), 95L
$bmp.Save([IO.Path]::GetFullPath($Out), $codec, $params)
if ($Preview) { $bmp.Save($Preview, [Drawing.Imaging.ImageFormat]::Png) }
$bmp.Dispose()
"icon: $([IO.Path]::GetFullPath($Out)) ($((Get-Item $Out).Length) bytes)"
