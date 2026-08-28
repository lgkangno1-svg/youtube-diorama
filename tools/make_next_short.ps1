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
Write-Host "PROGRESSIVE FLOW SPEND" -ForegroundColor Yellow
Write-Host "A. Approve the free reference/keyframe images first."
Write-Host "B. Generate G1 only (Veo 3.1 Lite, output count 1, current displayed cost verified). Stop if maker-view composition / paws-only identity / tiny scale / anatomy is structurally wrong. A non-first-person camera is not itself a failure."
Write-Host "C. After each PASS, save that scene's actual last usable frame when the Flow pack requires it for the next First frame."
Write-Host "D. Continue one scene at a time. Never spend G2 before G1 PASS or G3 before G2 PASS."
Write-Host "E. If the manifest/runtime is compact_h30, normally finish at G3. If it is immersive_h40, G4 is allowed only after G3 PASS and only for its documented independent world-resolution beat."
Write-Host "F. generated/${EpisodeId}_flow_pack.md and ${EpisodeId}_bundle.md are the episode-specific source of truth for scene count, frame inputs, and runtime intent."
Write-Host "G. After the continuity chain is complete, Plus/Pro/Ultra users may upscale QC-PASS clips to 1080p only when Flow currently shows 0 credits. Do not upscale rejects, and never use an upscaled/re-encoded export as the next-scene continuity bridge; the native saved PASS frame remains the bridge."
Write-Host ""
Write-Host "Do not force every episode into H30 or H40. Follow the current manifest and stop rather than pad." -ForegroundColor Green
