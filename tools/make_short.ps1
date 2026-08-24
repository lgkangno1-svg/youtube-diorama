param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$EpisodeId
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Manifest = Join-Path $Root "episodes/$EpisodeId.yaml"

if (-not (Test-Path $Manifest)) {
    Write-Error "Episode manifest not found: $Manifest`nAsk ChatGPT to prepare the next episode manifest first."
    exit 2
}

Set-Location $Root

Write-Host "Tiny Cat Kitchen production prep: $EpisodeId" -ForegroundColor Cyan
Write-Host "No Flow credits, uploads, or LLM/API calls will be used by this script." -ForegroundColor DarkGray

python tools/build_episode_bundle.py "episodes/$EpisodeId.yaml"
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "NEXT:" -ForegroundColor Green
Write-Host "1. Open generated/${EpisodeId}_bundle.md"
Write-Host "2. Approve the keyframes/contact sheet before spending Flow credits."
Write-Host "3. Follow generated/${EpisodeId}_flow_pack.md and aim for three 8-second Lite generations (H30)."
Write-Host "4. Do not reroll a whole episode for one bad shot."
