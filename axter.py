from lxml import html
import requests
import os

# Define the directory to save the PDFs
directory = '/DIRECTORY/'
# Make a request to the website
url = 'https://www.axter.eu/'
response = requests.get(url)
# Parse the HTML content
tree = html.fromstring(response.content)
# Find all <a> elements that match the criteria
links = tree.xpath('//a[contains(@href, "/fichier-ged/")]')
# Download the links
for link in links:
    pdf_link = "https://www.axter.eu"+link.attrib.get('href')
    pdf_name = link.attrib.get('data-ged').split("/")[-1]
    print(pdf_name)
    # pdf_name = pdf_name.replace("®","").replace("é","e").strip().replace(" ","_").replace("è","e")
    pdf_name = directory+pdf_name
    # print(pdf_name)
    # if os.path.exists(pdf_name):
    #     print(pdf_name.split("/")[-1] + " already exists. Skipping...")
    #     continue
    pdf_response = requests.get(pdf_link, stream=True)
    try:
        with open(pdf_name, 'wb') as pdf_file:
            for chunk in pdf_response.iter_content(chunk_size=1024):
                if chunk:
                    pdf_file.write(chunk)
            pdf_file.write(pdf_response.content)
        print("Downloaded: " + pdf_name.split("/")[-1])
    except:
        print("NOT Downloaded: " + pdf_name.split("/")[-1])
