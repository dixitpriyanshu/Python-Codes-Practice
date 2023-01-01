import requests
from bs4 import BeautifulSoup
from pprint import pprint
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup =  BeautifulSoup(web_page, "html.parser")

movie_list = [movie_item.get_text() for movie_item in soup.find_all(name= "h3", class_ = "title")]

movies = movie_list[::-1]
pprint(movies)
# with open("Day 45 - Web Scrapping with BeautifulSoup/movie.txt", "w") as movie_file:
#     for movie in movies:
#         movie_file.write(f"{movie}\n")
