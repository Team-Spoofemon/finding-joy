$rpy = "game\assets\background\background.rpy"
$extensions = @(
    ".png",
    ".jpg"
)
$startwith = "image"


$dirpath = [IO.Path]::GetDirectoryName($rpy)

$lines = @()
Get-ChildItem -Path $dirpath | ForEach-Object {
    $extension = [IO.Path]::GetExtension($_.Name)
    $ext = ($extensions -Contains $extension)
    $cont = ($_.Name.Contains(' '))  # $_.Name.Contains('reversed') -Or
    Write-Host "$($_.Name) $extension, $ext, $cont"

    if ($ext -And (-Not $cont)) {
        $relpath = (Resolve-Path -Path $_.FullName -Relative)
        $relpath = $relpath.Substring(7).Replace("\", "/")
        $filename = [IO.Path]::GetFileNameWithoutExtension($_.Name)
        $lines += @("$startwith $filename = `"$relpath`"")
    }
}

Set-Content -Path $rpy -Value $lines

# foreach ($file in $files) {
#     $dirname = [IO.Path]::GetDirectoryName($file).Split('\')
#     $dirname = $dirname[$dirname.Count - 1]
#     # Write-Host $dirname
#     New-Item -ItemType Directory "ignoreme/$dirname" -ErrorAction SilentlyContinue
#     Copy-Item -Path $file -Destination "ignoreme/$dirname"
# }
