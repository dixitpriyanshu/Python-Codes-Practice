from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
#
# button = driver.find_element(By.LINK_TEXT, "Schengen Area")
# button.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

while True:
    pass
