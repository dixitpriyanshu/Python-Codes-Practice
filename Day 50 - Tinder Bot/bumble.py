import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Development/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)


driver.get("https://bumble.com/")

sign_in = driver.find_element(
    by=By.XPATH,
    value='//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a',
)
sign_in.click()

time.sleep(2)

facebook_button = driver.find_element(
    by=By.XPATH,
    value='//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div',
)

facebook_button.click()

window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

email = driver.find_element(by=By.NAME, value="email")
password = driver.find_element(by=By.NAME, value="pass")

email.send_keys("")# your email
password.send_keys("")#your password
password.send_keys(Keys.ENTER)

driver.switch_to.window(window_before)


count = 0
while True:
    try:

        time.sleep(2)
        like = driver.find_element(
            by=By.XPATH,
            value='//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span',
        )
        like.click()
    except NoSuchElementException:
        if count >= 5:
            break

        count += 1
        print("No such element! Waiiting...")
        time.sleep(5)
        continue