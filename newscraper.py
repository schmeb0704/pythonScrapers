from bs4 import BeautifulSoup
import lxml
import requests
from operator import itemgetter

response = requests.get("https://news.ycombinator.com/")
data = response.text

soup = BeautifulSoup(data, "lxml")

upvotes = soup.find_all(name="span", class_="score")
articles = soup.find_all(name="span", class_="titleline")

articles_obj = []

for i in range(0, len(articles), 1):
    article_link = articles[i].find(name="a").get("href")
    article_title = articles[i].find(name="a").getText()
    upvote = int(upvotes[i].getText().split()[0])

    indv_article = {"title": article_title, "link": article_link, "score": upvote}
    articles_obj.append(indv_article)


sorted_by_upvotes = sorted(articles_obj, key=itemgetter("score"), reverse=True)

for i in range(0, 5, 1):
    print(sorted_by_upvotes[i])
