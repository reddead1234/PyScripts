import json
import requests
from lxml import html
import os
import re

def download_pdf_files(url,file_path):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    pdf_links = tree.xpath("//a[contains(@href, '.pdf')]")
    for pdf_link in pdf_links:
        pdf_url = pdf_link.attrib.get('href')
        pdf_name = os.path.basename(pdf_url)
        pdf_name = re.sub(r'[^\w\s-]','',pdf_name) #removing special characters
        pdf_name = pdf_name.replace(" ","_") #replacing spaces with _
        try:
            with open(f"{file_path}{pdf_name}", 'wb') as pdf_file:
                pdf_file.write(requests.get(pdf_url).content)
            print(f"Downloaded: {pdf_name}")
        except:
            print(f"Error downloading {pdf_name}")

for i in range(1,4):
    url = f"https://www.example.com/page/{i}/?document_search&example"
    file_path = '/Directory/'
    download_pdf_files(url,file_path)
