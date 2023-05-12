from lxml import html
import requests
import re
import os
import urllib
from urllib.parse import urlparse
import unicodedata

def pdf_downloader(url,f_path,f_name):
    response = urllib.request.urlopen(url)
    path=f_path + f_name
    file = open(path, 'wb')
    file.write(response.read())
    file.close()

url="https://www.ursa.fr"
# response = requests.get(url)
# tree = html.fromstring(response.content)
# links = tree.xpath("//a[contains(@href, '/wp-content/uploads/')]")
html_p = urllib.request.urlopen(url)
text = html_p.read()
plaintext = text.decode('utf8')
links = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
print(links)
k=0
for link in links:
    if "uploads" in link :
            name = os.path.basename(link)
            print(name)
            f_path='/directory/'
            pdf_downloader(link,f_path,name)
            k+=1
    else:
        continue
