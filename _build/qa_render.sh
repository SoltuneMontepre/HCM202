#!/usr/bin/env bash
# Rebuild deck, render PNGs (via PowerPoint, from an ASCII temp path) and make a contact sheet.
# Usage: bash _build/qa_render.sh <tag>
set -e
export PYTHONIOENCODING=utf-8
ROOT="/f/Download/Slide thuyết trình"
S="${QA_DIR:-/c/Users/lengu/AppData/Local/Temp/claude/F--Download-Slide-thuy-t-tr-nh/873b9672-a056-448d-b544-e5844c6c2863/scratchpad}"
TAG="${1:-v}"
cd "$ROOT"
python _build/build_deck.py
cp "01_Tu_tuong_HCM_Dai_doan_ket.pptx" "$S/deck.pptx"
powershell.exe -ExecutionPolicy Bypass -File "F:/Download/Slide thuyết trình/_build/render.ps1" -Pptx "$(cygpath -w "$S/deck.pptx")" -PngDir "$(cygpath -w "$S/render")" | tail -1
python _build/contact_sheet.py "$S/render" "$S/sheet_$TAG.png" 3 600
