#!/usr/bin/env python3
"""Make the app pages' extra screenshots and walkthrough clips.

    python3 scripts/build-media.py

Run this only when the sources change; the output is checked in. It reads
the guide screenshots and recordings under guides/ and writes:

    assets/shots/<app>-<name>-1440.webp and -720.webp
    assets/video/<app>-<name>.mp4 and a poster .webp beside it

The guide recordings hold each step for about nine seconds. The clips here
play at twice that speed, which still leaves time to read each caption.
Needs Pillow and ffmpeg.
"""
import pathlib
import subprocess

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHOTS = ROOT / "assets/shots"
VIDEO = ROOT / "assets/video"

# (app, output name, source image)
STILLS = [
    ("cold-open", "templates", "guides/cold-open/images/cmd-template.new.png"),
    ("cold-open", "breakdown", "guides/cold-open/images/panel-breakdown.png"),
    ("cold-open", "revisions", "guides/cold-open/images/cmd-revisions.newSet.png"),
    ("cold-open", "dictation", "guides/cold-open/images/panel-dictation.png"),
    ("backlot", "budget", "guides/backlot/images/budget.png"),
    ("backlot", "breakdown", "guides/backlot/images/breakdown-stripboard.png"),
    ("backlot", "call-sheets", "guides/backlot/images/call-sheets.png"),
    ("backlot", "dood", "guides/backlot/images/dood.png"),
]

# (app, output name, source recording, second to take the poster from)
CLIPS = [
    ("cold-open", "editor", "guides/cold-open/videos/getting-started.mp4", 44),
    ("cold-open", "dictation", "guides/cold-open/videos/format-draft-dictation.mp4", 40),
    ("cold-open", "breakdown", "guides/cold-open/videos/breakdown-to-backlot.mp4", 30),
    ("cold-open", "movie-magic", "guides/cold-open/videos/movie-magic-export.mp4", 30),
    ("backlot", "import", "guides/backlot/videos/import-tagged-script.mp4", 40),
    ("backlot", "schedule", "guides/backlot/videos/building-a-schedule.mp4", 24),
    ("backlot", "call-sheets", "guides/backlot/videos/call-sheets.mp4", 40),
]


def still(app, name, source):
    im = Image.open(ROOT / source).convert("RGB")
    for width in (1440, 720):
        out = im if im.width == width else im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
        out.save(SHOTS / f"{app}-{name}-{width}.webp", quality=82, method=6)


def clip(app, name, source, poster_at):
    out = VIDEO / f"{app}-{name}.mp4"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", str(ROOT / source),
        "-vf", "setpts=PTS/2,fps=12,scale=1280:-2", "-an",
        "-c:v", "libx264", "-preset", "slow", "-crf", "25", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(out)], check=True)
    png = VIDEO / f"{app}-{name}.png"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-ss", str(poster_at), "-i", str(ROOT / source),
        "-frames:v", "1", "-vf", "scale=1280:-2", str(png)], check=True)
    Image.open(png).convert("RGB").save(VIDEO / f"{app}-{name}.webp", quality=80, method=6)
    png.unlink()


if __name__ == "__main__":
    VIDEO.mkdir(exist_ok=True)
    for row in STILLS:
        still(*row)
    for row in CLIPS:
        clip(*row)
    print(f"wrote {len(STILLS)} screenshots and {len(CLIPS)} clips")
