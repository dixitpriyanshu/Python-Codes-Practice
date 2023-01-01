from bs4 import BeautifulSoup
import requests
from pprint import pprint

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(selector= ".titleline a")
# pprint(articles)

article_texts = []
article_links = []


for article in articles:
    
    text = article.getText()
    article_texts.append(text)

    link = article.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_ = "score")]

largets_vote = max(article_upvote)
largest_index = article_upvote.index(largets_vote)

pprint(article_texts[largest_index])
pprint(article_links[largest_index])
pprint(article_upvote[largest_index])
