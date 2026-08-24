$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Pointer = Join-Path $Root "production/NEXT_EPISODE.txt"

if (-not (Test-Path $Pointer)) {
    Write-Error "Missing production/NEXT_EPISODE.txt. Ask ChatGPT: 다음 영상 준비해줘"
    exit 2
}

$EpisodeId = (Get-Content $Pointer -Raw).Trim()
if ([string]::IsNullOrWhiteSpace($EpisodeId)) {
    Write-Error "production/NEXT_EPISODE.txt is empty. Ask ChatGPT: 다음 영상 준비해줘"
    exit 2
}

Write-Host "Tiny Cat Kitchen — next episode: $EpisodeId" -ForegroundColor Cyan
Write-Host "This command spends 0 Flow credits. It only prepares local production files." -ForegroundColor DarkGray
Write-Host ""

& (Join-Path $PSScriptRoot "make_short.ps1") $EpisodeId
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "PROGRESSIVE FLOW SPEND" -ForegroundColor Yellow
Write-Host "A. Approve free reference/keyframe images first."
Write-Host "B. Generate G1 only (8s Lite, output count 1). Stop if identity/scale is wrong."
Write-Host "C. Save G1's actual last usable frame in Flow and use it as G2 First frame."
Write-Host "D. Generate G2 only after G1 passes."
Write-Host "E. Save G2's actual last usable frame and use it as G3 First frame."
Write-Host "F. Generate G3 only if the final Short still needs the payoff/resolution motion."
Write-Host ""
Write-Host "Default ceiling: H30 = three 8-second Veo 3.1 Lite generations." -ForegroundColor Green
Write-Host "Do not spend the next 10 credits just because they are available."
