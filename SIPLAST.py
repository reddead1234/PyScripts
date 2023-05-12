from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a web driver (e.g. Chrome)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://www.bmigroup.com/")

# Find the download button by its class name and click it
download_button = driver.find_element(By.CLASS_NAME, "MuiButton-label")
download_button.click()
