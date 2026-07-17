$ErrorActionPreference = "Stop"

$Whisper = "C:\Users\Administrator\Documents\Codex\2026-06-11\hugohe3-ppt-master-https-github-com\work\audio-tools\whisper-bin-x64\Release\whisper-cli.exe"
$Model = "C:\Users\Administrator\Documents\Codex\2026-06-11\hugohe3-ppt-master-https-github-com\work\audio-tools\models\ggml-small.bin"
$Dir = "D:\codex\work-content\运营复盘\录音转写_2026-06-11"

$Files = @(
  "2026年06月11日 13点36分",
  "2026年06月11日 14点06分",
  "2026年06月11日 11点37分"
)

foreach ($Name in $Files) {
  $InputFile = Join-Path $Dir "$Name.wav"
  $OutputBase = Join-Path $Dir "$Name.whisper"
  Write-Host "TRANSCRIBE $InputFile"
  & $Whisper -m $Model -f $InputFile -l zh -otxt -osrt -of $OutputBase -t 8 -bs 5 --prompt "不凡智库，郑总，彭工，嘉立创，工程师，电子工程，PCB，SMT，EDA，元器件，供应链，硬科技，社区运营，科学家，专家库" --print-progress
}
