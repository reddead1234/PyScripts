import json,requests
from lxml import html
import urllib
import os
import re
import unicodedata
import cgi


def pdf_downloader(url,f_path,f_name):
    response = urllib.request.urlopen(url)
    path=f_path + f_name
    file = open(path, 'wb')
    file.write(response.read())
    file.close()

for i in range(1,8):
    lien="https://www.fermacell.com/en/downloads?documentTypeId=40&language=English,French&page="+str(i)
    print('>>>>>>><<<<<<<<<<<<<<<<<<<<<<<>>>>>>>><>>>>>\n'+lien+"\n")
    page = requests.get(lien)
    tree = html.fromstring(page.content)
    elems = tree.xpath("//div[class='download']")
    print(elems)
    k=0
#     for elem in elems:  
#         emp="https://www.fermacell.com"+elem.get_attribute('href')
#         print(emp)
#         name = os.path.basename(emp)
#         k=k+1
#         print(name)
#         f_path='/home/reda/Desktop/fermacell_FT/'
#         try:
#             pdf_downloader(emp,f_path,name)
#         except:
#             print(name+"NOT DOWNLOADED")
# print("\n>>>>>>>>>>>>>>>>> K= "+str(k))