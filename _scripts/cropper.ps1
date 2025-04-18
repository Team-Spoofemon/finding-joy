[CmdletBinding()]
param (
    [Parameter()][string]$WidthOffset=0,
    [Parameter()][string]$HeightOffset=0,
    [Parameter()][string]$Dirpath,
    [Parameter()][string]$WidthXHeight
)
$extensions = @(
    ".png",
    ".jpg"
)

Get-ChildItem -Path $Dirpath | ForEach-Object {
    $extension = [IO.Path]::GetExtension($_.Name)
    $ext = ($extensions -Contains $extension)

    if ($ext) {
        # 984x620+0+50
        $cmd = "magick '$($_.FullName)' -crop $WidthXHeight+$WidthOffset+$HeightOffset +repage 'ignoreme\$($_.Name)'"
        Write-Host -ForegroundColor Cyan $cmd
        Invoke-Expression $cmd
        Write-Host "ignoreme\$($_.Name)"
    }
}