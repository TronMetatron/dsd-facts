#!/usr/bin/env python3
"""Black-box @handles, nearby display names, and avatars in a social media screenshot.
Usage: redact.py INPUT [-o OUTPUT] [--box x,y,w,h ...] [--debug]
OCR: RapidOCR (pip rapidocr_onnxruntime); falls back to tesseract via pytesseract.
ALWAYS review the output by eye before publishing; OCR can miss text."""
import argparse, re, sys
from pathlib import Path
from PIL import Image, ImageDraw
HANDLE = re.compile(r'@\w{2,}')

def ocr(path):
    try:
        from rapidocr_onnxruntime import RapidOCR
        res, _ = RapidOCR()(str(path))
        out = []
        for pts, txt, conf in res or []:
            xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
            out.append((int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys)), txt))
        return out
    except ImportError:
        import pytesseract
        d = pytesseract.image_to_data(Image.open(path), output_type=pytesseract.Output.DICT)
        return [(d['left'][i], d['top'][i], d['left'][i]+d['width'][i], d['top'][i]+d['height'][i], d['text'][i])
                for i in range(len(d['text'])) if d['text'][i].strip()]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('-o', '--output')
    ap.add_argument('--box', action='append', default=[], help='extra manual box x,y,w,h')
    ap.add_argument('--debug', action='store_true'); a = ap.parse_args()
    src = Path(a.input); img = Image.open(src).convert('RGB'); W, H = img.size
    lines = ocr(src); boxes = []
    for i, (x0, y0, x1, y1, t) in enumerate(lines):
        if not HANDLE.search(t): continue
        h = y1 - y0; pad = max(4, h // 3); mine = [(x0-pad, y0-pad, x1+pad, y1+pad)]   # handle (often with name on same row)
        for (a0, b0, a1, b1, t2) in lines:                       # display name: same row to the left, or directly above
            same_row = abs((b0+b1)/2 - (y0+y1)/2) < h and a1 < x0 + 5 and x0 - a1 < 6*h
            above = 0 <= y0 - b1 < 1.5*h and abs(a0 - x0) < 4*h
            if same_row or above: mine.append((a0-pad, b0-pad, a1+pad, b1+pad))
        left = min(b[0] for b in mine) + pad; top = min(b[1] for b in mine); bot = max(b[3] for b in mine)
        if left > 2*h:                                            # avatar: generous square left of the name block
            s = max(int(4.2*h), bot - top + 2*h); cy = (top + bot)//2
            mine.append((max(0, left - s - pad), max(0, cy - s//2), left - pad//2, min(H, cy + s//2)))
        boxes += mine
        if a.debug: print('handle:', t, (x0, y0, x1, y1), file=sys.stderr)
    for b in a.box:
        x, y, w, h = map(int, b.split(',')); boxes.append((x, y, x+w, y+h))
    d = ImageDraw.Draw(img)
    for b in boxes: d.rectangle([max(0,b[0]), max(0,b[1]), min(W,b[2]), min(H,b[3])], fill='black')
    out = Path(a.output) if a.output else src.with_name(src.stem + '.redacted.png')
    img.save(out); print(f'{out}  ({len(boxes)} boxes; handles found: {sum(bool(HANDLE.search(l[4])) for l in lines)})')
    if not any(HANDLE.search(l[4]) for l in lines): print('WARNING: no @handle detected; redact manually with --box', file=sys.stderr)
if __name__ == '__main__': main()
