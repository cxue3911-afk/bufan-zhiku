from pathlib import Path
import wave

import av


FILES = [
    Path(r"D:\Users\abf2020\Documents\WXWork\1688857598847072\Cache\File\2026-06\2026年06月11日 13点36分.m4a"),
    Path(r"D:\Users\abf2020\Documents\WXWork\1688857598847072\Cache\File\2026-06\2026年06月11日 14点06分.m4a"),
    Path(r"D:\Users\abf2020\Documents\WXWork\1688857598847072\Cache\File\2026-06\2026年06月11日 11点37分.m4a"),
]

OUT_DIR = Path(r"D:\codex\work-content\运营复盘\录音转写_2026-06-11")
OUT_DIR.mkdir(parents=True, exist_ok=True)


def convert(src: Path, dst: Path) -> None:
    container = av.open(str(src))
    stream = container.streams.audio[0]
    resampler = av.AudioResampler(format="s16", layout="mono", rate=16000)
    with wave.open(str(dst), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        for packet in container.demux(stream):
            for frame in packet.decode():
                for out in resampler.resample(frame):
                    wf.writeframes(bytes(out.planes[0]))
        for out in resampler.resample(None):
            wf.writeframes(bytes(out.planes[0]))
    container.close()


for src in FILES:
    dst = OUT_DIR / f"{src.stem}.wav"
    print(f"CONVERT {src.name} -> {dst}", flush=True)
    convert(src, dst)
    print(f"SAVED {dst}", flush=True)
