from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
from lxml import html

# Define the directory to save the PDFs
directory = '/DIRECTORY/'

# Initialize the web driver
driver = webdriver.Firefox()

# Loop over the range of values
url = 'https://www.pointp.fr/search/page-2?q=RAGNO'
print(url)
driver.get(url)
input()
# Find all elements that match the criteria
links = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/")]')
# Extract the href attribute from the links
link_urls = [link.get_attribute("href") for link in links]
for link_url in link_urls:
    response = requests.get(link_url)
    tree = html.fromstring(response.content)
    print(html.tostring(tree).decode("utf-8"))
    pdfs=tree.xpath("//a[contains(@href, '/asset/')]")
    print(pdfs)
    for pdf in pdfs:
        pdf_link = pdf.attrib.get('href')
        pdf_name = directory + pdf_link.split("/")[-1]

        # Check if the file already exists
        if os.path.exists(pdf_name):
            print(pdf_name.split("/")[-1] + " already exists.")
            continue

        pdf_response = requests.get(pdf_link)
        with open(pdf_name, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print("Downloaded: " + pdf_name.split("/")[-1])

driver.quit()
