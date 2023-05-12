from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.bmigroup.com/fr/documentation/fiches-produits/?filters=%5B%7B%22name%22%3A%22Brand%22%2C%22value%22%3A%5B%22Siplast%22%5D%7D%5D")

# Find the download button by its class name and click it
download_button = driver.find_element(By.CLASS_NAME, "MuiButton-label")
download_button.click()



