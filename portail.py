from lxml import html
import requests
import os

# Define the directory to save the PDFs
directory = '/directory/'

# Make a request to the website
for i in range(1,152):
    url = 'https://portailbatiment.fr/q/REFIN/'+str(i)
    print(url)
    response = requests.get(url)

    # Parse the HTML content
    tree = html.fromstring(response.content)

    # Find all <a> elements that match the criteria
    links = tree.xpath('//a[contains(@href, ".pdf")]')
    # Download the links
    for link in links:
        pdf_link = link.attrib.get('href')
        pdf_name = directory + pdf_link.split("/")[-1]

        # Check if the file already exists
        if os.path.exists(pdf_name):
            print(pdf_name.split("/")[-1] + " already exists.")
            continue

        pdf_response = requests.get(pdf_link)
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print("Downloaded: " + pdf_name.split("/")[-1])
