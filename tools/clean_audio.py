"""Build copyright-safe audio: isolated voice (from audio-separator vocal stem) + original synthesized SFX.
Usage: python3 clean_audio.py SPEC.json VOCALS.wav OUT.wav
No third-party music is kept: the SFX (pop on each reveal, whoosh on title scenes) are generated here with numpy.
"""
import sys, json, wave, subprocess, numpy as np

SR = 44100


def pop(n):
    t = np.arange(int(0.22 * SR)) / SR
    f = 640 + 70 * n
    x = np.sin(2 * np.pi * f * t) * np.exp(-t * 24) + 0.5 * np.sin(2 * np.pi * f * 2.01 * t) * np.exp(-t * 40)
    x[:60] += np.linspace(0.6, 0, 60)
    return x * 0.55


def whoosh():
    n = int(0.32 * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(7)
    noise = rng.standard_normal(n)
    # sweep via moving-average lowpass that opens up, enveloped
    k = np.clip((np.linspace(40, 4, n)).astype(int), 2, 60)
    out = np.empty(n)
    c = np.cumsum(noise)
    for i in range(n):
        a = max(0, i - k[i])
        out[i] = (c[i] - c[a]) / max(1, k[i])
    env = np.sin(np.pi * np.clip(t / 0.32, 0, 1)) ** 2
    out = out / (np.abs(out).max() + 1e-9) * env
    return out * 0.5


def main(spec_path, vocals, out):
    spec = json.load(open(spec_path))
    tmp = out + ".voice.wav"
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", vocals, "-ac", "1", "-ar", str(SR),
                           "-af", "highpass=f=70,loudnorm=I=-15:TP=-1.5:LRA=9", tmp])
    w = wave.open(tmp)
    v = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    sfx = np.zeros_like(v)
    n = 0
    for sc in spec["scenes"]:
        if sc["k"] == "pair":
            n += 1
            s = pop(n % 9)
            i = int(sc["r"] * SR)
            sfx[i:i + len(s)] += s[:max(0, len(sfx) - i)]
        elif sc["k"] in ("title", "sent", "end") and sc["t0"] > 0.2:
            s = whoosh()
            i = int(max(0, sc["t0"] - 0.08) * SR)
            sfx[i:i + len(s)] += s[:max(0, len(sfx) - i)]
    mix = v + sfx * 0.16
    peak = np.abs(mix).max()
    if peak > 0.97:
        mix *= 0.97 / peak
    pcm = (mix * 32767).astype(np.int16)
    wo = wave.open(out, "wb")
    wo.setnchannels(1); wo.setsampwidth(2); wo.setframerate(SR); wo.writeframes(pcm.tobytes()); wo.close()
    print(out, round(len(mix) / SR, 2), "s peak", round(float(np.abs(mix).max()), 2))


if __name__ == "__main__":
    main(*sys.argv[1:4])
