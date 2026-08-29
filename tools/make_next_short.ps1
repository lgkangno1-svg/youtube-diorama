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

$OperatorCard = Join-Path $Root "production/${EpisodeId}_OPERATOR_CARD.md"

Write-Host "Tiny Cat Kitchen — next episode: $EpisodeId" -ForegroundColor Cyan
Write-Host "This command spends 0 Flow credits. It only prepares local production files." -ForegroundColor DarkGray
Write-Host ""

python (Join-Path $PSScriptRoot "validate_maker_view_manifest.py") $EpisodeId
if ($LASTEXITCODE -ne 0) {
    Write-Error "Episode manifest is stale or incompatible with the current Mini Forest-style maker-view standard. Ask ChatGPT: 다음 영상 준비해줘"
    exit $LASTEXITCODE
}

& (Join-Path $PSScriptRoot "make_short.ps1") $EpisodeId
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host ""
Write-Host "YOUR NEXT ACTION" -ForegroundColor Green
if (Test-Path $OperatorCard) {
    Write-Host "Open production/${EpisodeId}_OPERATOR_CARD.md and do only its NOW/current-action section first."
    Write-Host "For TK-005 this means: make/approve the strongest KF0 scale-hook anchor before any paid G1."
} else {
    Write-Host "Open generated/${EpisodeId}_bundle.md and start at its first planned-keyframe action."
}

Write-Host ""
Write-Host "QUALITY-FIRST PROGRESSIVE FLOW" -ForegroundColor Yellow
Write-Host "A. Free visual preflight: use Nano Banana/reference frames to lock the hook, absurd tiny scale, feline paws, maker-view composition, fixed props and lighting."
Write-Host "B. Generate G1 only after the planned visual chain passes. Judge the first 1–2 seconds for immediate premise/scale readability and the tactile action for believable feline motion."
Write-Host "C. PASS → native Save frame → next paid scene. Structural FAIL → stop; do not spend the next scene."
Write-Host "D. Continue one scene at a time. G4 is optional and only earns a generation when real G3 footage still benefits from an independent resolution/payoff beat."
Write-Host "E. generated/${EpisodeId}_bundle.md and generated/${EpisodeId}_flow_pack.md remain technical reference/fallback artifacts; the episode Operator Card is the primary fast-production surface when present."
Write-Host "F. Do not reroll good motion for audio-only defects; repair/replace audio in edit when practical."
Write-Host "G. Paid Veo generation and YouTube publishing remain explicit user actions."
Write-Host ""
Write-Host "Do not force runtime. Optimize the actual Short: hook → visible transformation → scale proof → payoff." -ForegroundColor Green
