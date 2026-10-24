import re,json,time,subprocess,sys
chs=['cold-email','cold-dm','linkedin','reddit','facebook','forums','partnerships','seo','word-of-mouth','referral-program','hacker-news','product-hunt','twitter','tiktok','youtube','influencers','slack','discord','newsletter','content-marketing','meta-ads','google-ads','webinars','events','blog']
def get(u):
    r=subprocess.run(['curl','-sS','-m','40','-A','Mozilla/5.0',u],capture_output=True,text=True)
    return r.stdout
m={}
for c in chs:
    t=get(f'https://trustmrr.com/channels/{c}')
    s=list(dict.fromkeys(re.findall(r'/startup/([a-z0-9_\-]+)',t)))
    for x in s: m.setdefault(x,[]).append(c)
    print(c,len(s),flush=True); time.sleep(0.4)
json.dump(m,open('chan_map.json','w'))
print('unique',len(m))
data={}
for i,(slug,cs) in enumerate(m.items()):
    t=get(f'https://trustmrr.com/startup/{slug}.md')
    data[slug]={'channels':cs,'md':t}
    time.sleep(0.3)
    if i%40==0: print(i,flush=True)
json.dump(data,open('startups_raw.json','w'))
print('done')
