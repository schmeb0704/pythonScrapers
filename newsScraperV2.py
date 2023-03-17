import sys
from bs4 import BeautifulSoup
import requests

def main():
  response = requests.get("https://news.ycombinator.com/").text
  soup = BeautifulSoup(response, "html.parser")
  title_elements = soup.find_all("span", class_ = "titleline")
  score_elements = soup.find_all("span", class_ = "score")
  news_titles = make_news_objs(title_elements, score_elements)

  for news in news_titles:
    print(news)

def make_news_objs(titles, score_elements):
  title_texts = []
  counter = 0

  for title in titles:
    string_score = score_elements[counter].get_text().split() 
    link_element = title.find("a")
    link = link_element.get("href")
    text = title.get_text()
    title_texts.append({"title": text, "site": link, "score": int(string_score[0])})
    counter += 1
  
  return title_texts

if __name__ == "__main__":
  main()
