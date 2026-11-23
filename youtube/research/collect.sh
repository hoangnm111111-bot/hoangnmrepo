#!/bin/bash
# usage: collect.sh DATA_DIR ; reads niches from niches.txt (slug|query)
D="$1"; T="$(dirname "$0")"
search() { slug="${1%%|*}"; q="${1#*|}"; qe=$(python3 -I -c 'import sys,urllib.parse;print(urllib.parse.quote_plus(sys.argv[1]))' "$q")
  timeout 120 yt-dlp "https://www.youtube.com/results?search_query=$qe&sp=EgIIBQ%253D%253D" --flat-playlist --playlist-end 40 -J > "$D/search/$slug.json" 2>/dev/null; }
export -f search; export D
xargs -P 6 -I{} bash -c 'search "$@"' _ {} < "$T/niches.txt"
python3 -I - "$D" <<'PY'
import json,sys,os,glob
D=sys.argv[1]; chans={}
for f in glob.glob(D+"/search/*.json"):
    slug=os.path.basename(f)[:-5]
    try: es=json.load(open(f)).get("entries") or []
    except Exception: continue
    seen=[]
    for e in es:
        c=e.get("channel_id")
        if c and c not in seen and (e.get("duration") or 0)>120: seen.append(c)
    for c in seen[:9]: chans.setdefault(c,set()).add(slug)
open(D+"/chanlist.txt","w").write("\n".join(f"{c} {','.join(sorted(s))}" for c,s in chans.items()))
print(len(chans),"channels")
PY
chan() { c="${1%% *}"; [ -s "$D/chan/$c.json" ] || timeout 120 yt-dlp "https://www.youtube.com/channel/$c/videos" --flat-playlist --playlist-end 15 -J > "$D/chan/$c.json" 2>/dev/null; }
export -f chan
xargs -P 8 -I{} bash -c 'chan "$@"' _ {} < "$D/chanlist.txt"
echo done
