# from selenium import webdriver

# chrome_driver_path = "/Development/chromedriver"

# driver = webdriver.Chrome(executable_path= chrome_driver_path)

# driver.get("https://www.amazon.com/")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.amazon.com/")

driver.quit()
