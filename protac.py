import json,requests
from lxml import html
import urllib
import os
import re
import unicodedata
import cgi

def pdf_downloader(url,f_path,f_name):
    print(f_name)
    response = urllib.request.urlopen(url)
    path=f_path + f_name
    print(path)
    file = open(path, 'wb')
    file.write(response.read())
    file.close()

lien="https://www.udirev.com/sols-pvc/?page=2"
print('>>>>>>><<<<<<<<<<<<<<<<<<<<<<<>>>>>>>><thumbnail product-thumbnail>>>>>\n'+lien+"\n")
page = requests.get(lien)
tree = html.fromstring(page.content)
elems = tree.xpath("//a[contains(@href,'.html')]")
for elem in elems:
    emp=elem.attrib.get('href')
    pdf_page=requests.get(emp)
    pdf_tree=html.fromstring(pdf_page.content)
    datasheets=pdf_tree.xpath("//a[@class='btn']")
    for datasheet in datasheets :
        if "Avis technique" in datasheet.text_content():
            link=datasheet.attrib.get("href")
            if link.startswith("//"):
                link = "https:" + link
            res = requests.get(link)
            name = res.headers.get('Content-Disposition').split('filename=')[-1].strip('"')
            # name = emp.split('/')[-1]
            print(link)
            f_path='/home/reda/Desktop/UDIREV_AT/'

            pdf_downloader(link,f_path,name)