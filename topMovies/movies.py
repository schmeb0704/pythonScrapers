import requests
import lxml
from bs4 import BeautifulSoup
from operator import itemgetter

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/"
).text


soup = BeautifulSoup(response, "html.parser")


movie_list = soup.find(name="div", class_="listicle-container")
ind_movie = movie_list.find_all(name="div", class_="jsx-3523802742 listicle-item")


titles = []

for i in range(len(ind_movie) - 1, -1, -1):
    title = ind_movie[i].find(name="img").get("alt")
    rank = len(ind_movie) - i
    titles.append(f"{rank}) {title}")


# sort_by_rank = sorted(titles, key=itemgetter("rank"))


with open("movies.txt", mode="w") as file:
    for movie in titles:
        file.write(f"{movie}\n")
