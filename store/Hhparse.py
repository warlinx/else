
from parse_hh_data import download, parse

vacancy = download.vacancy("36070814")

print(vacancy)
name = str(vacancy['name'])
descript = str(vacancy['description'])
print(name)
print(descript)