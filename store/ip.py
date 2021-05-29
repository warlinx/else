import urllib.request
import re

ip = urllib.request.urlopen('http://2ip.ru/').read()
print(re.search(b'\d+\.\d+\.\d+\.\d+', ip).group())
