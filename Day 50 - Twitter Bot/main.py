import time

from internetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_UP = 30
PROMISED_DOWN = 30
CHROME_DRIVER_PATH = "/Development/chromedriver"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
up, down = twitter_bot.get_internet_speed()
print(up)
print(down)

if up < PROMISED_UP or down < PROMISED_DOWN:
    twitter_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)

time.sleep(5)