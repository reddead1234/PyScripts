from lxml import html
import requests
import re

# Make a request to the website
for i in range(3):
    url = 'https://www.soprema.fr/fr/documentation/search-strict-product?query=&query_type=18&language=&document_page='+str(i)+'#documents'
    response = requests.get(url)

    # Parse the HTML content
    tree = html.fromstring(response.content)

    # Find all <a> elements that match the criteria
    links = tree.xpath('//a[contains(@href, "PAVA")]')
    # Download the links
    for link in links:
        pdf_link= link.attrib.get('href')
        pdf_response = requests.get(pdf_link)
        pdf_name = '/home/reda/Desktop/PAVATEX_AT/'+pdf_link.split("/")[-1]
        print(pdf_name)
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print("Downloaded: " + pdf_name)











# import json,requests
# from lxml import html
# import urllib
# import os
# import re
# import unicodedata
# import cgi


# def pdf_downloader(url,f_path,f_name):
#     response = urllib.request.urlopen(url)
#     path=f_path + f_name
#     # file = open(path, 'wb')
#     # file.write(response.read())
#     # file.close()


# lien="https://www.soprema.fr/fr/dop-archive"
# print('>>>>>>><<<<<<<<<<<<<<<<<<<<<<<>>>>>>>><>>>>>\n'+lien)
# page = requests.get(lien)
# tree = html.fromstring(page.content)
# elems = tree.xpath("//td[contains(text(),'PAVA') and a[contains(@href, 'DOP')]]")
# for elem in elems:  
#     emp=elem.attrib.get('href')
#     print(emp)
#     temp= elem.text_content()
#     name='k'+temp
#     # f_path='/home/reda/Desktop/ISOPROC_FT/'
#     try:
#         pdf_downloader(emp,f_path,name)
#     except:
#         print(name)