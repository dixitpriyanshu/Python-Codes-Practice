from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pprint import pprint

chrome_driver_path = "/Development/chromedriver"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event_dict = {}

for n in range(0, len(dates)):
    event_dict[n] = {
        "time" :dates[n].text,
        "name" : events[n].text
    }

pprint(event_dict)