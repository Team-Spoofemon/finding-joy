[CmdletBinding()]
param (
    [Parameter()][String]$RenpyProjectRoot = "$PSScriptRoot\..\..\",
    [Parameter()][String]$Project = "finding-joy",
    [Parameter(Mandatory=$true)][String][ValidateSet("clean", "lint", "ogg")]$Action
)

$ProjectDirpath = [IO.Path]::GetFullPath("$RenpyProjectRoot/$Project")

function Run-Clean {
    Write-Host -ForegroundColor Cyan "Cleaning..."
    Get-ChildItem -Path $ProjectDirpath -Recurse -Filter "*.rpyc" | ForEach-Object {
        Write-Host $_.FullName
        Remove-Item $_.FullName
    }
    Write-Host -ForegroundColor Yellow "Result: $LASTEXITCODE"
}


function Run-Lint {
    Write-Host -ForegroundColor Cyan "Linting..."
    # usually pythonw.exe, but here we can just use python.exe
    & "C:\tools\renpy-8.3.4-sdk\lib\py3-windows-x86_64\python.exe"  `
        "C:\tools\renpy-8.3.4-sdk\renpy.py"  `
        $ProjectDirpath  `
        lint  `
        "$ProjectDirpath\lint.txt"  `
        --json-dump  `
        "$ProjectDirpath\game\saves\navigation.json"
        # --errors-in-editor
    Write-Host -ForegroundColor Yellow "Result: $LASTEXITCODE"
}


function Convert-Ogg {
    $pwd = Get-Location
    $items = get-childitem -Path $ProjectDirpath -Recurse | Where-Object {
        $_.Name -match '^.*\.flac|^.*\.aiff'
    }
    try {
        $items | ForEach-Object {
            $dirname = [IO.Path]::GetDirectoryName($_.FullName)
            $filename = [IO.Path]::GetFileNameWithoutExtension($_.Name)

            Set-Location $dirname

            $cmd = "ffmpeg -y -i '$($_.Name)' '$filename.ogg'"
            Write-Host -ForegroundColor Green $cmd
            Invoke-Expression $cmd
        }
    }
    finally {
        Set-Location $pwd
    }

}



# run the game at all
# C:\tools\renpy-8.3.4-sdk\lib\py3-windows-x86_64\pythonw.exe
#     C:\tools\renpy-8.3.4-sdk\renpy.py
#     "E:\Shared drives\Team Spoofymon\renpy_projects\finding_joy"
#     --json-dump
#     "E:\Shared drives\Team Spoofymon\renpy_projects\finding_joy\game\saves\navigation.json"
#     --errors-in-editor


if ($Action.ToLower() -eq "clean") {
    Run-Clean
} elseif ($Action.ToLower() -eq "lint") {
    Run-Clean
    Run-Lint
} elseif ($Action.ToLower() -eq "ogg") {
    Convert-Ogg
}


Write-Host -ForegroundColor Cyan "Done..."
