"""Copy only the public files of Unity Lab into _build/site_unitylab/ (the folder that gets deployed).

    python _build/stage_unitylab.py
    netlify deploy --prod --dir _build/site_unitylab --site unitylab-hcm202

03_UnityLab/README.md (internal notes) is deliberately not published.
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "03_UnityLab"
OUT = ROOT / "_build" / "site_unitylab"
PUBLIC = ["index.html", "style.css", "script.js", "assets"]

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)
for name in PUBLIC:
    src = SRC / name
    if src.is_dir():
        shutil.copytree(src, OUT / name)
    else:
        shutil.copy2(src, OUT / name)
files = sorted(p.relative_to(OUT).as_posix() for p in OUT.rglob("*") if p.is_file())
print(f"staged {len(files)} files -> {OUT}")
for f in files:
    print("  ", f)
