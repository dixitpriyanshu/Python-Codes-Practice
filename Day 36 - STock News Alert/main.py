import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "" #Your Stock API

account_sid = "" # Enter your sid
auth_token = "" ## Enter your authentication token

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "" #Your NEWS API

news_parameters = {
    "qInTitle" : COMPANY_NAME,
    "apikey" : NEWS_API
}

def send_msg(articles):
    client = Client(account_sid, auth_token)
    for article in articles:
        message = client.messages.create(
        body=article,
        from_="+19704324339",
        to="Your Verified Number"
        )
        print(message.sid)

def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params= news_parameters)
    articles = news_response.json()["articles"][:3]

    formatted_article = [f"{STOCK}: {updown}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}" for article in articles]
    return formatted_article

stock_parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey" : STOCK_API
}

stock_response = requests.get(STOCK_ENDPOINT, params= stock_parameters)

stock_data = stock_response.json()["Time Series (Daily)"]

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price

updown = None

if difference > 0:
    updown ="🔺"
else:
    updown = "🔻"

diff_percent = round((difference / yesterday_closing_price) * 100, 2)
print(diff_percent)

if abs(diff_percent) > 5:
    news_articles = get_news()
    send_msg(news_articles)