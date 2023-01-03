from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
number.click()
