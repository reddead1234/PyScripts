from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome()

# Navigate to the website
for i in range(1,5):

    driver.get("https://www.cedeo.fr/search/page-"+str(i)+"?filters=f/catalogue_xml_lb_marque/century&q=century")
    input()
# Find the download button by its class name and click it
    elems = driver.find_elements(By.XPATH, "//a[@href]")
    for elem in elems:
        if "/p/"in elem.get_attribute("href"):
            print(elem.get_attribute("href"))
            # wait = WebDriverWait(driver, 10)
            # file = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()=' D.O.P. ']")))
            # print(file.get_attribute("href"))
directory = '/DDIRECTORY/ARTE_ONE_FT/'
