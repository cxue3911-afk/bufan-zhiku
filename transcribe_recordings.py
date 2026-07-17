from pathlib import Path
from faster_whisper import WhisperModel


FILES = [
    Path(r"D:\Users\abf2020\Documents\WXWork\1688857598847072\Cache\File\2026-06\2026年06月11日 13点36分.m4a"),
    Path(r"D:\Users\abf2020\Documents\WXWork\1688857598847072\Cache\File\2026-06\2026年06月11日 14点06分.m4a"),
    Path(r"D:\Users\abf2020\Documents\WXWork\1688857598847072\Cache\File\2026-06\2026年06月11日 11点37分.m4a"),
]

OUT_DIR = Path(r"D:\codex\work-content\运营复盘\录音转写_2026-06-11")
OUT_DIR.mkdir(parents=True, exist_ok=True)

model = WhisperModel("small", device="cpu", compute_type="int8")

for audio in FILES:
    print(f"TRANSCRIBING {audio.name}", flush=True)
    segments, info = model.transcribe(
        str(audio),
        language="zh",
        beam_size=5,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 700},
    )
    out = OUT_DIR / f"{audio.stem}.txt"
    with out.open("w", encoding="utf-8") as f:
        f.write(f"# {audio.name}\n")
        f.write(f"language={info.language}; probability={info.language_probability:.4f}; duration={info.duration:.2f}\n\n")
        for seg in segments:
            f.write(f"[{seg.start:0.2f}-{seg.end:0.2f}] {seg.text.strip()}\n")
    print(f"SAVED {out}", flush=True)
