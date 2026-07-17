from pathlib import Path
import subprocess


WHISPER = Path(r"C:\Users\Administrator\Documents\Codex\2026-06-11\hugohe3-ppt-master-https-github-com\work\audio-tools\whisper-bin-x64\Release\whisper-cli.exe")
MODEL = Path(r"C:\Users\Administrator\Documents\Codex\2026-06-11\hugohe3-ppt-master-https-github-com\work\audio-tools\models\ggml-base.bin")
DIR = Path(r"D:\codex\work-content\运营复盘\录音转写_2026-06-11")
PROMPT = "不凡智库，郑总，彭工，嘉立创，工程师，电子工程，PCB，SMT，EDA，元器件，供应链，硬科技，社区运营，科学家，专家库"

for name in ["2026年06月11日 13点36分", "2026年06月11日 14点06分", "2026年06月11日 11点37分"]:
    input_file = DIR / f"{name}.wav"
    output_base = DIR / f"{name}.whisper"
    print(f"TRANSCRIBE {input_file}", flush=True)
    cmd = [
        str(WHISPER),
        "-m", str(MODEL),
        "-f", str(input_file),
        "-l", "zh",
        "-otxt",
        "-osrt",
        "-of", str(output_base),
        "-t", "8",
        "-bs", "5",
        "--prompt", PROMPT,
        "--print-progress",
    ]
    subprocess.run(cmd, check=True)
