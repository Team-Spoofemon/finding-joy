<#
https://www.renpy.org/doc/html/cli.html
#>

[CmdletBinding()]
param (
    [Parameter()][String]$RenpyProjectRoot = "$PSScriptRoot\..\..\",
    [Parameter()][String]$Project = "finding-joy",
    [Parameter(Mandatory=$true)][String][ValidateSet("clean", "lint", "ogg", "run", "build", "todo")]$Action,
    [Parameter()][switch]$Force
)

$ProjectDirpath = [IO.Path]::GetFullPath("$RenpyProjectRoot/$Project")

function Start-Clean {
    Write-Host -ForegroundColor Cyan "Cleaning..."

    # delete persistent files
    $ProjectPersistent = [IO.Path]::GetFullPath("$RenpyProjectRoot/$Project/game/saves/persistent")
    if (Test-Path -Path $ProjectPersistent -ErrorAction SilentlyContinue) {
        Write-Host $ProjectPersistent
        Remove-Item $ProjectPersistent -Force
    }
    # this is a folder like "finding_joy-1740528823"
    Get-ChildItem -Path "$env:APPDATA/Renpy" -Filter "$($Project -replace "-", "_")*" | ForEach-Object {
        Write-Host $_.FullName
        Remove-Item $_.FullName -Recurse -Force
    }

    Get-ChildItem -Path $ProjectDirpath -Recurse -Filter "*.rpyc" | ForEach-Object {
        Write-Host $_.FullName
        Remove-Item $_.FullName
    }
    Write-Host -ForegroundColor Yellow "Result: $LASTEXITCODE"
}


function Start-Lint {
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
    code "$ProjectDirpath\lint.txt"
    code "$ProjectDirpath\errors.txt"
}


function Start-Todo {
    & python "$PSScriptRoot/assets-todo.py"
    Write-Host -ForegroundColor Yellow "Result: $LASTEXITCODE"
}



function Start-Run {
    Write-Host -ForegroundColor Cyan "Running..."
    # usually pythonw.exe
    taskkill /f /t /im pythonw.exe
    & "C:\tools\renpy-8.3.4-sdk\lib\py3-windows-x86_64\pythonw.exe"  `
        "C:\tools\renpy-8.3.4-sdk\renpy.py"  `
        $ProjectDirpath  `
        --json-dump  `
        "$ProjectDirpath\game\saves\navigation.json"  `
        --errors-in-editor
}

function Start-Build {
    Write-Host -ForegroundColor Cyan "Building..."
    & "C:\tools\renpy-8.3.4-sdk\lib\py3-windows-x86_64\pythonw.exe"  `
        "C:\tools\renpy-8.3.4-sdk\renpy.py"  `
        $ProjectDirpath  `
        compile  `
        --keep-orphan-rpyc  `
        "$ProjectDirpath\game\saves\navigation.json"  `
        --errors-in-editor
}



function Convert-Ogg {
    $generated = @()
    $cwd = Get-Location
    $items = get-childitem -Path $ProjectDirpath -Recurse | Where-Object {
        $_.Name -match '^.*\.flac|^.*\.aiff|^.*\.mp3'
    }
    try {
        $items | ForEach-Object {
            $dirname = [IO.Path]::GetDirectoryName($_.FullName)
            $filename = [IO.Path]::GetFileNameWithoutExtension($_.Name)

            Set-Location $dirname

            if ($Force -or (-Not (Test-Path -Path "$filename.ogg" -ErrorAction SilentlyContinue))) {
                $cmd = "ffmpeg -y -i '$($_.Name)' '$filename.ogg'"
                Write-Host -ForegroundColor Green $cmd
                Invoke-Expression $cmd

                $generated += @("$filename.ogg")
            }

            if ($Force -or (-Not (Test-Path -Path "$filename (reversed).ogg" -ErrorAction SilentlyContinue))) {
                $cmd = "ffmpeg -y -i '$($_.Name)' -af 'areverse' '$filename (reversed).ogg'"
                Write-Host -ForegroundColor Green $cmd
                Invoke-Expression $cmd

                $generated += @("$filename (reversed).ogg")
            }
        }
    }
    finally {
        Set-Location $cwd
    }

    $generated | ForEach-Object {
        Write-Host -ForegroundColor Cyan $_
    }
}


if ($Action.ToLower() -eq "clean") {
    Start-Clean
} elseif ($Action.ToLower() -eq "lint") {
    Start-Clean
    Start-Lint
} elseif ($Action.ToLower() -eq "todo") {
    Start-Clean
    Start-Lint
    Start-Todo
} elseif ($Action.ToLower() -eq "ogg") {
    Convert-Ogg
} elseif ($Action.ToLower() -eq "run") {
    Start-Clean
    Start-Run
} elseif ($Action.ToLower() -eq "build") {
    # TODO: doesnt actually build anything, just "compile" and no outputs. maybe gui is the only way.
    Start-Clean
    Start-Build
}


Write-Host -ForegroundColor Cyan "Done..."
