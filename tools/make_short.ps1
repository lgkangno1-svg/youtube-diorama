param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$EpisodeId
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Manifest = Join-Path $Root "episodes/$EpisodeId.yaml"
$OperatorCard = Join-Path $Root "production/${EpisodeId}_OPERATOR_CARD.md"

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
if (Test-Path $OperatorCard) {
    Write-Host "PRIMARY RUNBOOK" -ForegroundColor Green
    Write-Host "Open production/${EpisodeId}_OPERATOR_CARD.md first."
    Write-Host "It is the fastest quality-first path: do the section marked NOW/current action, then follow its exact KF/G order and PASS criteria."
    Write-Host ""
    Write-Host "Fallback/reference only:" -ForegroundColor DarkGray
    Write-Host "- generated/${EpisodeId}_bundle.md"
    Write-Host "- generated/${EpisodeId}_flow_pack.md"
} else {
    Write-Host "NEXT" -ForegroundColor Green
    Write-Host "1. Open generated/${EpisodeId}_bundle.md"
    Write-Host "2. Follow generated/${EpisodeId}_flow_pack.md scene by scene."
}

Write-Host ""
Write-Host "PRODUCTION RULES" -ForegroundColor Yellow
Write-Host "1. Build/approve the strongest planned keyframe chain before paid video; prioritize hook, miniature scale, tactile transformation, paw anatomy, fixed props and continuity."
Write-Host "2. Generate only the next paid scene allowed by the manifest. G1 first; do not generate G2/G3/G4 before the previous scene passes QC."
Write-Host "3. Save the previous PASS scene's actual last usable native frame whenever the next scene requires it as First frame."
Write-Host "4. Do not reroll good motion for audio-only defects; replace bad audio in edit when practical."
Write-Host "5. Do not add/drop a scene merely to hit target length; G4 must earn independent payoff value."
Write-Host "6. Nano Banana is a free quality/continuity preflight in the user's current Google workflow. Existing UI/model checks are safety rails, not the production focus."
Write-Host "7. Paid Veo generation and publishing still require explicit user action."
