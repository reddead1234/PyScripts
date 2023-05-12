import json,requests
from lxml import html
import urllib
import os
import re
import unicodedata
import cgi
import webbrowser

def download_pdf(url):


for i in range(0,1):
           lien='https://www.placo.fr/&page='+str(i)
           page = requests.get(lien)
           tree = html.fromstring(page.content)
           elems = tree.xpath("/html/body/div[2]/div/main/div/div/div[2]/article/div/div[2]/div[2]/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/a")
           print(elems)
           k=0
           # for t in elems:
           #      l=t.attrib.get("href")
           #      print(l)
           #      site='http://knauf.fr'+l
           #      #download_pdf(site)
           #      k=k+1
           # print('je trouve  '+str(k)+' liens de telechargement sur cette page')
