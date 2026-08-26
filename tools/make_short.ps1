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
Write-Host "2. Approve the free keyframes/contact sheet before spending Flow credits."
Write-Host "3. Follow generated/${EpisodeId}_flow_pack.md scene by scene; do not assume every episode is H30/three generations."
Write-Host "4. Generate only the next scene allowed by the manifest/runtime gate, and only after the previous scene passes QC."
Write-Host "5. Save the previous scene's actual last usable frame whenever the Flow pack requires it for the next First frame."
Write-Host "6. Do not reroll a whole episode for one bad shot or add/drop a scene merely to hit a target length."
