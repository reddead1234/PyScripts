import json,requests
from lxml import html
import urllib
import os
import re
import unicodedata
import cgi
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By

def pdf_finder():
    elems = driver.find_elements(By.XPATH,"//a[contains(@href, '/-/')]")
    print(len(elems))
    for elem in elems:
        name='/home/reda/Desktop/SINIAT_FT/'+ str(elem.get_attribute('data-download'))
        url=elem.get_attribute('href')
        response=requests.get(url)
        #open(name, 'wb').write(response.content)
def downloader(website):
    driver.get(website) 
    l=input("done")
    pdf_finder()
website = 'https://www.siniat.fr/fr-fr/documentation/?filter=documentType.eq.TechnicalSystemCard&page=1&page_size=50&sort=contextorder_web_siniat_france&sort_type=asc'
driver = webdriver.Chrome('/home/reda/Desktop/chromedriver')
downloader(website=website)


# def pdf_downloader(url,f_path,f_name):
#     response = urllib.request.urlopen(url)
#     path=f_path + f_name
#     file = open(path, 'wb')
#     file.write(response.read())
#     file.close()
# def download_pdf(url):
#     get_url= webbrowser.open(url)

# lien='https://www.siniat.fr/fr-fr/documentation/?filter=documentType.eq.DeclarationOfPerformance&page=4&page_size=50&sort=contextorder_web_siniat_france&sort_type=asc&view_size=200'
# page = requests.get(lien)
# tree = html.fromstring(page.content)
# mores=tree.xpath("//button[.//span[text()[contains(.,'Voir plus de documents')]]]")
# for more in mores:
#     print(more.attrib.get('href'))
# print(mores)
# elems = tree.xpath("//a[contains(@href, 'dop')]")
# #print(elems)
# print(len(elems))
# for elem in elems:
#     #print(elem)
#     if '.pdf' in elem:
#         print(elem)        
#            # k=0
           # for t in elems:
           #      l=t.attrib.get("href")
           #      print(l)
           #      site='http://knauf.fr'+l
           #      #download_pdf(site)
           #      k=k+1
           # print('je trouve  '+str(k)+' liens de telechargement sur cette page')


# def uss(f_path,searchText):#URSA-Soprema-Siniat
#     website='https://www.siniat.fr/fr-fr/documentation/?filter=documentType.eq.DeclarationOfPerformance&page=4&page_size=50&sort=contextorder_web_siniat_france&sort_type=asc&view_size=200'
#     html_p = urllib.request.urlopen(website)
#     text = html_p.read()
#     plaintext = text.decode('utf8')
#     elems = re.findall("href=[\"\'](.*?)[\"\']", plaintext)
#     h=0
#     for elem in elems:
#         if searchText in elem :
#             name = os.path.basename(elem)
#             print(name)
#             try:
#                 #pdf_downloader(elem,f_path,name)
#                 print(++h)
#             except:
#                 print("\n LINK CORRUPTED  ")
#                 continue
#         else:
#             continue
#     print("\nPAGE  "+str(i)+"  IS DONE")
# uss("/home/reda/Desktop/SINIAT_DOP/","dam")