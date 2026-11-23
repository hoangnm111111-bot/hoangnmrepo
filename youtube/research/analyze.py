import json,sys,os,statistics as st
D=sys.argv[1]; out=sys.argv[2]
niche={}
for line in open(D+"/chanlist.txt"):
    c,s=line.split(); 
    for n in s.split(","): niche.setdefault(n,[]).append(c)
allrows={}; summary=[]
for n,cs in sorted(niche.items()):
    rows=[]; subs=[]; meds=[]; small_ok=0; small=0; ratios=[]
    for c in cs:
        f=f"{D}/chan/{c}.json"
        try: j=json.load(open(f))
        except Exception: continue
        sc=j.get("channel_follower_count") or 0
        es=[e for e in (j.get("entries") or []) if e.get("view_count") is not None]
        if len(es)<4: continue
        name=j.get("channel") or j.get("uploader") or c
        v=[e["view_count"] for e in es]; m=st.median(v)
        subs.append(sc); meds.append(m)
        if sc and sc<100000:
            small+=1
            if m>=20000: small_ok+=1
        if sc: ratios.append(m/sc)
        for e in es: rows.append({"channel":name,"subs":sc,"title":e.get("title",""),"views":e["view_count"],"url":e.get("url",""),"duration":e.get("duration")})
    allrows[n]=rows
    outl=0
    by={}
    for r in rows: by.setdefault(r["channel"],[]).append(r["views"])
    for r in rows:
        md=st.median(by[r["channel"]])
        if md and r["views"]/md>=3: outl+=1
    summary.append(dict(niche=n,channels=len(meds),med_subs=int(st.median(subs)) if subs else 0,
        med_views=int(st.median(meds)) if meds else 0,small_ch=small,small_ch_20k=small_ok,
        views_per_sub=round(st.median(ratios),3) if ratios else 0,outliers_3x=outl,videos=len(rows)))
    json.dump(rows,open(f"{out}/{n}.json","w"))
summary.sort(key=lambda x:-(x["views_per_sub"]))
print(f"{'niche':15}{'ch':>4}{'medSubs':>10}{'medViews':>10}{'v/sub':>7}{'small':>6}{'sm20k':>6}{'3x':>5}")
for s in summary: print(f"{s['niche']:15}{s['channels']:>4}{s['med_subs']:>10,}{s['med_views']:>10,}{s['views_per_sub']:>7}{s['small_ch']:>6}{s['small_ch_20k']:>6}{s['outliers_3x']:>5}")
json.dump(summary,open(out+"/summary.json","w"),indent=1)
