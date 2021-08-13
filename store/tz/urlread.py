import urllib
from urllib.request import urlopen
from xml.dom import minidom

source = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
xmldoc = minidom.parse(source)
list_ids = ['R01820']
valutes = xmldoc.getElementsByTagName("Valute")
for valute in valutes:
    id1 = valute.getAttribute("ID")
    value = valute.getElementsByTagName("Value")[0]
    char_code = valute.getElementsByTagName("CharCode")[0]
    if id1 in list_ids:
        print("exchange rate:%s, char code:%s" %
              (value.firstChild.data, char_code.firstChild.data))
