#!/usr/bin/env python3
"""Add a Debunked entry. The image must ALREADY be redacted (use tools/redact.py) and reviewed.
Usage: add_debunk.py IMAGE [--rarity "text|label|url"] [--health "text|label|url"] --claim "..." --fact "..." --source "Label|url" [--source ...] [--date YYYY-MM-DD] [--alt "..."]
Source urls may be site-relative, e.g. "Ovotesticular DSD|conditions.html#c8". Rebuilds the site; does not commit or push."""
import argparse, datetime, json, shutil, subprocess, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument('image'); ap.add_argument('--claim', required=True)
ap.add_argument('--fact', required=True); ap.add_argument('--source', action='append', default=[])
ap.add_argument('--rarity', action='append', default=[], help='"text|source label|url" (repeatable)')
ap.add_argument('--health', action='append', default=[], help='"text|source label|url" (repeatable)')
ap.add_argument('--date', default=datetime.date.today().isoformat()); ap.add_argument('--alt', default='Redacted screenshot of the social media post')
a = ap.parse_args()
if 'originals' in Path(a.image).resolve().parts: raise SystemExit('Refusing: that is an unredacted original. Run redact.py first.')
db = ROOT/'debunked'/'entries.json'; entries = json.loads(db.read_text()) if db.exists() else []
n = len(entries) + 1; src = Path(a.image)
name = f"{a.date}-{n:03d}{src.suffix.lower()}"; shutil.copy2(src, ROOT/'debunked'/'img'/name)
srcs = [dict(zip(('label','url'), s.split('|', 1))) if '|' in s else {'label': s, 'url': s} for s in a.source]
entries.append(dict(id=n, date=a.date, image=f'debunked/img/{name}', alt=a.alt, claim=a.claim, fact=a.fact, sources=srcs))
def trip(v):
    p = v.split('|')
    if len(p) != 3: raise SystemExit(f'Need "text|label|url": {v}')
    return dict(text=p[0], label=p[1], url=p[2])
entries[-1]['rarity'] = [trip(v) for v in a.rarity]; entries[-1]['health'] = [trip(v) for v in a.health]
db.write_text(json.dumps(entries, indent=2)); subprocess.run(['python3', 'build.py'], cwd=ROOT, check=True)
print(f'Added entry #{n}: debunked/img/{name}. Review debunked.html, then commit and push.')
