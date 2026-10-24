import json,re,csv
d=json.load(open('startups_raw.json'))
def money(s):
    if not s: return None
    s=s.replace(',','').replace('$','').strip()
    try: return float(s)
    except: return None
def f(pat,t,flags=0):
    m=re.search(pat,t,flags); return m.group(1).strip() if m else None
rows=[]
for slug,v in d.items():
    t=v['md']
    if len(t)<300 or 'Profile' not in t: continue
    r={'slug':slug,'channels':'|'.join(v['channels'])}
    r['name']=f(r'^# (.+)$',t,re.M)
    r['desc']=(f(r'- Description: (.+)',t) or '')[:240]
    r['country']=f(r'- Country: (\w+)',t)
    r['founded']=f(r'- Founded date: (\d{4}-\d{2}-\d{2})',t)
    r['audience']=f(r'- Audience type: \[?([A-Za-z0-9/ ]+)',t)
    r['team']=f(r'- Team size: (.+)',t)
    r['price']=(f(r'- Pricing model: (.+)',t) or '')[:200]
    r['persona']=(f(r'- Target persona: (.+)',t) or '')[:150]
    r['mrr']=money(f(r'- Current MRR: (\$[\d,\.]+)',t))
    r['rev30']=money(f(r'- Last 30 days revenue snapshot: (\$[\d,\.]+)',t))
    r['alltime']=money(f(r'- All-time revenue snapshot: (\$[\d,\.]+)',t))
    r['subs']=money(f(r'- Current active subscriptions: ([\d,]+)',t))
    r['margin']=f(r'- Last 30 days profit margin: ([\-\d\.]+%)',t)
    r['funding']=f(r'- Funding: (.+)',t)
    r['sale']='Listed for sale' in t
    r['cat']=f(r'^- Markets: \[([^\]]+)\]',t,re.M)
    rows.append(r)
json.dump(rows,open('rows.json','w'))
print(len(rows))
import collections
print(collections.Counter(r['audience'] for r in rows))
print(collections.Counter(r['team'] for r in rows).most_common(8))
print(sum(1 for r in rows if r['subs']),sum(1 for r in rows if r['price']),sum(1 for r in rows if r['founded']))
