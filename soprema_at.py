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

def uss(f_path,searchText):#URSA-Soprema-Siniat
    for i in range(1,3):
        website='https://www.soprema.fr/_page='+str(i)
        html_p = urllib.request.urlopen(website)
        text = html_p.read()
        plaintext = text.decode('utf8')
        elems = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
        for elem in elems:
            if searchText in elem :
                name = os.path.basename(elem)
                print(name)
                try:
                    pdf_downloader(elem,f_path,name)
                except:
                    print("\n LINK CORRUPTED  ")
                    continue
            else:
                continue
        print("\nPAGE  "+str(i)+"  IS DONE")
uss("/directory/","File")
