import urllib.request
import re

res = urllib.request.urlopen('http://2ip.ru/').read()
print(re.search(b'\d+\.\d+\.\d+\.\d+', res).group())
