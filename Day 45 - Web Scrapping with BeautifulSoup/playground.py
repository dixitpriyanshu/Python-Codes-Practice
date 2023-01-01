from bs4 import BeautifulSoup
import lxml

with open("Day 45 - Web Scrapping with BeautifulSoup/website.html", "r", encoding= "utf-8") as file1:
    contents = file1.read()

soup = BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)

# print(soup.prettify())

# print(soup.a)
# print(soup.p)
# print(soup.li)
# print(soup.h1)

# all_anchor_tags = soup.find_all(name= "a")
# # print(all_anchor_tags)

# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name= "h1", id = "name")

print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

print(soup.select_one(selector="p a"))
print(soup.select("a"))
