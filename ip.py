import bs4
import requests

s = requests.get('https://2ip.ua/ru/')
b = bs4.BeautifulSoup(s.text, "html.parser")
a = b.select(" .ipblockgradient .ip")[0].getText()
#print(a)
# получение ip-адреса
import urllib.request
import re
res = urllib.request.urlopen('http://2ip.ru/').read()
print(re.search(b'\d+\.\d+\.\d+\.\d+', res).group())











