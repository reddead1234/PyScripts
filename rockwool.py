
from lxml import html
import requests
import re
import os
import urllib


def pdf_downloader(url,f_path,f_name):
    response = urllib.request.urlopen(url)
    path=f_path + f_name
    file = open(path, 'wb')
    file.write(response.read())
    file.close()

url="https://www.rockwool.com"
response = requests.get(url)
tree = html.fromstring(response.content)
links = tree.xpath('//a[contains(@href, "datasheet.pdf")]')
k=0
for link in links:
    emp=link.attrib.get('href')
    emp = "https://www.rockwool.com" + emp
    name = os.path.basename(emp)
    k=k+1
    f_path='/directory/'
    pdf_downloader(emp,f_path,name)
