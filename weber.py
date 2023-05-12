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

for i in range(0,10):
    lien="https://www.fr.weber/search-document/content_type/product/product_datasheet_type/fiche-produit-267?page="+str(i)
    print('>>>>>>><<<<<<<<<<<<<<<<<<<<<<<>>>>>>>><>>>>>\n'+lien+"\n")
    page = requests.get(lien)
    tree = html.fromstring(page.content)
    elems = tree.xpath("//a[contains(@href, '.pdf' ) and @target='_blank' and text()='Télécharger']")
    k=0
    for elem in elems:  
        emp=elem.attrib.get('href')
        #print(emp)
        name = os.path.basename(emp)
        k=k+1
        print(name)
        f_path='/home/reda/Desktop/WEBER_FT/'
        try:
            pdf_downloader(emp,f_path,name)
        except:
            print(name)
print("\n>>>>>>>>>>>>>>>>> K= "+str(k))