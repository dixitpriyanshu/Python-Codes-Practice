import time

from internetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_UP = 30
PROMISED_DOWN = 30
CHROME_DRIVER_PATH = "/Development/chromedriver"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
twitter_bot.get_internet_speed()


time.sleep(5)