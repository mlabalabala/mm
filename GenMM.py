import requests, re, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    s = requests.session()

    h = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    }

    mmu = 'http://www.ef323.com'

    r = r'https://www\.\w+\.com'

    mmstr = "{\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36\",\"homeUrl\":\"https://www.d75612f62232.com/index/home.html\",\"cateNode\":\"//*[@id='section-menu']/div/div[2]/ul/li[position()<8]/a[1]\",\"cateName\":\"/text()\",\"cateNameR\":\"(\\\\S+)\",\"cateId\":\"/@href\",\"cateIdR\":\"/shipin/list-(\\\\S+)-1.html\",\"homeVodNode\":\"//*[@id='section-menu']/div/div[2]/ul/li[position()<8]/a[1]\",\"homeVodName\":\"/text()\",\"homeVodNameR\":\"(\\\\S+)\",\"homeVodId\":\"/@href\",\"homeVodIdR\":\"(\\\\S+)\",\"homeVodImg\":\"/@href\",\"homeVodMark\":\"\",\"cateUrl\":\"https://www.d75612f62232.com/shipin/list-{cateId}-{catePg}.html\",\"cateVodNode\":\"//body\",\"cateVodName\":\"//a[contains(text(), '>') and not(contains(text(), '>>'))]/@href\",\"cateVodNameR\":\"/shipin/list-(\\\\S+).html\",\"cateVodId\":\"//a[contains(text(), '>') and not(contains(text(), '>>'))]/@href\",\"cateVodIdR\":\"(\\\\S+)\",\"cateVodImg\":\"//a[contains(text(), '>') and not(contains(text(), '>>'))]/@href\",\"cateVodMark\":\"\",\"dtUrl\":\"https://www.d75612f62232.com{vid}\",\"dtNode\":\"//body\",\"dtName\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtImg\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtCate\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtYear\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtArea\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtMark\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtActor\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtDirector\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtDesc\":\"//*[@id='section-menu']/div/div[2]/div/a/text()\",\"dtFromNode\":\"//*[@id='section-menu']/div/div[2]/div/a\",\"dtFromName\":\"/text()\",\"dtUrlNode\":\"//*[@id='main-container']/div[2]/div[2]/ul[1]\",\"dtUrlSubNode\":\"/li/a[1]\",\"dtUrlId\":\"/@href\",\"dtUrlIdR\":\"(\\\\S+)\",\"dtUrlName\":\"/@title\",\"dtUrlNameR\":\"(\\\\S+)\",\"playUrl\":\"https://www.d75612f62232.com{playUrl}\",\"playUa\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36\"}"

    mmres = s.get(mmu, headers=h, verify=False)
    mmurl = re.findall(r, mmres.url)[0]
    mmstrmod = re.sub(r, mmurl, mmstr, 0, re.MULTILINE)

    with open('mmzxsp', 'w', encoding='utf8') as w:
        w.write(mmstrmod)
    
    with open('sex5offline', 'r', encoding='utf8') as r:
        s0 = r.read()
    u = 'http://tz2023may.com'
    s1 = s.get(u, headers=h, verify=False).url
    r = r'www\.\S+\.com'
    s1 = re.findall(r, s1, re.MULTILINE)[0]
    s0 = re.sub(r, s1, s0, 0, re.MULTILINE)

    with open('sex5offline', 'w', encoding='utf8') as w:
        w.write(s0)
