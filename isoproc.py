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
    # file = open(path, 'wb')
    # file.write(response.read())
    # file.close()

for i in range(0,108,18):
            lien="https://www.isoproc.be/solutions-downloads/overview/any/technische-fiches/any/P"+str(i)
            print('>>>>>>><<<<<<<<<<<<<<<<<<<<<<<>>>>>>>><>>>>>\n'+lien)
            page = requests.get(lien)
            tree = html.fromstring(page.content)
            elems = tree.xpath("//a[contains(@href, '.pdf?')]")
            for elem in elems:  
                emp=elem.attrib.get('href')
                #print(emp)
                temp= elem.text_content()
                name='k'+temp
                f_path='/home/reda/Desktop/ISOPROC_FT/'
                try:
                    pdf_downloader(emp,f_path,name)
                except:
                    print(name)