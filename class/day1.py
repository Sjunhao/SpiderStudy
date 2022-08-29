
import random
from urllib import parse

import requests
from bs4 import BeautifulSoup as bs
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.read)

# data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read().decode('utf-8'))

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url,data=data, headers=headers)
response = request.urlopen(req)
print(response.read().decode('utf-8'))