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

for i in range(0,14):
            lien="https://www.recticelinsulation.com/fr/documentation-technique"
            print(lien)
            page = requests.get(lien)
            tree = html.fromstring(page.content)
            elems = tree.xpath("//a[contains(@href, '/-/')]")
            for elem in elems:  
                emp=elem.attrib.get('href')
                print(emp)
                #name = os.path.basename(emp)
                #f_path='/home/reda/Desktop/RECTICEL_DOP/'
                #print(name)
                #pdf_downloader(emp,f_path,name)