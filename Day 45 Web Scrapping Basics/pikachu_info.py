
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.pokemon.com/us/pokedex/raichu")
content = response.text

soup = BeautifulSoup(content, "html.parser")

pokedex_entry = soup.select(selector="p.version-x")
for info in pokedex_entry:
    print(info.getText())