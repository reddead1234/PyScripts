import requests
from lxml import html
import urllib

def pdf_downloader(url, f_path, f_name):
    response = urllib.request.urlopen(url)
    path = f_path + f_name
    with open(path, 'wb') as file:
        file.write(response.read())

page_url = "https://fibranatur.fr/page={}"
f_path = '/home/reda/Desktop/FIBRANATURE_AT/'
k = 0
for i in range(13):
    page = requests.get(page_url.format(i))
    tree = html.fromstring(page.content)
    elems = tree.xpath("//a[contains(@class,'thumbnail product')]")
    for elem in elems:
        page_p = requests.get(elem.attrib.get('href'))
        tree_p = html.fromstring(page_p.content)
        fiches = tree_p.xpath("//a[contains(text(), 'Avis technique')]")
        for fiche in fiches:
            fib_file = 'https://fibranatur.fr/' + fiche.attrib.get('href')
            name = fiche.text_content().split("(")[0] + '.pdf'
            try:
                pdf_downloader(fib_file, f_path, name)
                k += 1
            except:
                print(name)
    print("\n Number of files downloaded: " + str(k))
