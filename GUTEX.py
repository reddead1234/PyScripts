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


lien="https://gutex.fr/service/telechargements/"
#print(lien)
page = requests.get(lien)
tree = html.fromstring(page.content)
elems = tree.xpath("//div[@id='panel-485']//a")
print(elems)
k=0
for elem in elems:  
    emp=elem.attrib.get('href')
    k=k+1
    #print(emp)
    name = os.path.basename(emp)
    print(name)
    link='https://www.gutex.fr/'+emp
    f_path='/home/reda/Desktop/GUTEX_FT/'
    pdf_downloader(link,f_path,name)
print('\n>>>>'+str(k))
