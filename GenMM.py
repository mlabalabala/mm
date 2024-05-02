import requests, urllib3, json
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

h = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A"}
session = requests.Session()
# 设置重试次数、间隔时间
retry = Retry(total=3, backoff_factor=1,connect=8)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

if __name__ == '__main__':

    # def_urls = ["dh44u","2cdas","rgcqe","pupbx","e8jt5"]
    def_urls_res_url = "http://www.bunnyabc.eu.org:5002/chfs/shared/share/res/4hu_url_sub_string.json"
    res = session.get(url=def_urls_res_url,headers=h,verify=False)
    def_urls = json.loads(res.text)
    print("def_urls:", def_urls)
    redirect_urls = set()
    for def_url in def_urls:
        try:
            print(f'ori: {def_url}')
            res = session.get(url=def_url,headers=h,verify=False,allow_redirects=True,timeout=3)
            print(res.url)
            if def_url != res.url:
               redirect_urls.add(res.url)
        except:
            continue
    json_str = json.dumps(list(redirect_urls))
    print("json_str:", json_str)
    with open("4hu_home_urls","w+",encoding="UTF-8") as w:
        w.write(json_str)

    '''
    import re
    mmu = 'http://www.ef323.com'
    r = r'https://www\.\w+\.com'
    mmres = session.get(mmu, headers=h, verify=False)
    mmurl = re.findall(r, mmres.url)[0]

    with open('mmzxsp', 'w', encoding='utf8') as w:
        w.write(mmstrmod)
    '''
    
    '''
    with open('sex5offline', 'r', encoding='utf8') as r:
        s0 = r.read()
    u = 'http://tz2023may.com'
    s1 = s.get(u, headers=h, verify=False).url
    r = r'www\.\S+\.com'
    s1 = re.findall(r, s1, re.MULTILINE)[0]
    s0 = re.sub(r, s1, s0, 0, re.MULTILINE)

    with open('sex5offline', 'w', encoding='utf8') as w:
        w.write(s0)
    '''
