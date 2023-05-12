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


lien="https://www.steico.com/fr/telechargements/documents/archives-declarations-de-performances"
#print(lien)
page = requests.get(lien)
tree = html.fromstring(page.content)
elems = tree.xpath("//a[contains(@href, '/DoP_Archive/')]")
k=0
for elem in elems:  
    emp=elem.attrib.get('href')
    k=k+1
    #print(emp)
    name = os.path.basename(emp)
    print(name)
    link='https://www.steico.com/'+emp
    f_path='/home/reda/Desktop/STEICO_DOP/'
    pdf_downloader(link,f_path,name)
print('\n>>>>'+str(k))



