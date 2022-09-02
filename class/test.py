
import random

import requests
from bs4 import BeautifulSoup as bs

# 头文件，防止被BAN
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70',
    # 'cookie': '__utmz=63332592.1657018303.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; sdc_session=1657786664335; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1657018281,1657786664; __utmc=63332592; motion_id=1657789251026_0.8240650468520039; __utma=63332592.1628587186.1657018303.1657786686.1657789264.4; __utmt=1; tgw_l7_route=cfc54d8963ffc9a6226b3055b0851e96; WT_FPC=id=undefined:lv=1657789323900:ss=1657789241859; sdc_userflag=1657789241861::1657789323902::4; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1657789324; __utmb=63332592.4.10.1657789264; CLICKSTRN_ID=117.139.220.75-1657018280.838495::4E4782FB186EBA42D661A2DE84708C35=',
    # 'referer': 'https://odds.500.com/fenxi/ouzhi-1037634.shtml'
}
# 网址
url = 'https://odds.500.com/fenxi/ouzhi-1037634.shtml'


# 利用requests库下载网页
page = requests.get(url, headers=headers)
# print(page.content)

# 利用beautifulSoup库解析页面
# soup = bs(page.content,'html.parser',from_encoding="gb18030")
soup = bs(page.content, 'html.parser', from_encoding="utf-8")

# 从解析的页面获得想要的数据
tabel = soup.find('table', id='datatb')
lines = tabel.find_all('tr')
for line in lines:
    # print(line)
    # print("---------------------------------")
    if temp := line.find("span", attrs={"class": "quancheng"}):
        print("赔率公司全称：" + temp.string)


def get_cookie(url):
    res = requests.get(url, headers=headers)
    cookies = res.cookies
    cookie = requests.utils.dict_from_cookiejar(cookies)
    return cookie
def get_ajax_page(url):
    # 网址
    standerd_page_url = 'https://odds.500.com/fenxi/ouzhi-1037634.shtml'
    cookie=get_cookie(standerd_page_url)
    # headers['content-type'] = r'application/x-www-form-urlencoded'
    headers['referer'] = 'https://odds.500.com/fenxi/ouzhi-1037634.shtml'
    # headers['cookie'] = 'sdc_session=1661931244972; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1661931245; __utma=63332592.874368.1661931246.1661931246.1661931246.1; __utmc=63332592; __utmz=63332592.1661931246.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; WT_FPC=id=undefined:lv=1661931271614:ss=1661931244969; sdc_userflag=1661931244972::1661931271629::2; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1661931272; __utmb=63332592.2.10.1661931246; CLICKSTRN_ID=117.177.111.25-1661931246.358615::9A4EEDAFB2CFDBF6F21EFCEF7F2F50C6'
    res = requests.get(url, headers=headers)
    soup = bs(res.content, 'html.parser', from_encoding="utf-8")
    lines = soup.find_all('tr')
    print('\n')
    for line in lines:
        # print(line)
        # print("---------------------------------")
        if temp := line.find("span", attrs={"class": "quancheng"}):
            print("赔率公司全称：" + temp.string)

url = 'https://odds.500.com/fenxi1/ouzhi.php?id=1037634&ctype=1&start=120&r=1&style=0&guojia=0&chupan=1'
get_ajax_page(url)


# 下载文件
def get_xls(id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
        # 'cookie': '__utmz=63332592.1657018303.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; sdc_session=1657786664335; Hm_lvt_4f816d475bb0b9ed640ae412d6b42cab=1657018281,1657786664; __utmc=63332592; __utma=63332592.1628587186.1657018303.1657786686.1657789264.4; WT_FPC=id=undefined:lv=1657789323900:ss=1657789241859; Hm_lpvt_4f816d475bb0b9ed640ae412d6b42cab=1657789324; CLICKSTRN_ID=117.139.220.75-1657018280.838495::4E4782FB186EBA42D661A2DE84708C35; motion_id=1657799234916_0.5429281969924591',
        # 'referer': 'https://odds.500.com/fenxi/ouzhi-1037634.shtml',
        # 'content-length':'1054',
        'content-type': 'application/x-www-form-urlencoded',
        'accept-language': 'zh-ch'
        # 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'accept-encoding':'gzip, deflate, br',
        # 'cache-control':'max-age=0',
        # 'origin': 'https://odds.500.com',
        # 'dnt': '1'
        # 'Connection': 'close'
    }

    # post提交的表单
    body = {
        'fixtureid': id,
        'excelst': 1,
        'style': 0,
        'ctype': 1,
        'dcid': None,
        'scid': None,
        'r': 1
    }

    # 随机选择一个agent
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    headers['User-Agent'] = random.choice(user_agent_list)
    url = 'https://odds.500.com/fenxi/europe_xls.php'
    file = requests.post(url, headers=headers, data=body)
    # file.content.decode(encoding='utf-8')
    # import cgi
    # header = file.headers.get('content-disposition')
    # print(header)
    # value, params = cgi.parse_header(header)
    # print(params)
    # file_name = params['filename']
    # # file_name = file_name.encode('utf-8').decode('gbk').encode('utf-8')
    # # file_name = file_name.encode('gb18030')
    # print(str(file_name))
    with open(str(id)+'.xls', mode='wb') as f:
        f.write(file.content)


# get_xls(1046235)
