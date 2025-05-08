# does it in place on all in directory

[CmdletBinding()]
param (
    [Parameter()][string]$Dirpath,
    [Parameter()][string]$Percentage=50
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
        $cmd = "magick '$($_.FullName)' -resize $Percentage% 'ignoreme\$($_.Name)'"
        Write-Host -ForegroundColor Cyan $cmd
        Invoke-Expression $cmd
        Write-Host "ignoreme\$($_.Name)"
    }
}
