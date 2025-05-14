
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

movie_tag_list = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_name_list = reversed([movie.getText() for movie in movie_tag_list])

text_file_data = ""

for movie_name in movie_name_list:
    text_file_data = text_file_data + movie_name + "\n"

with open("top 100 movies list.txt", "w") as file:
    file.write(text_file_data)