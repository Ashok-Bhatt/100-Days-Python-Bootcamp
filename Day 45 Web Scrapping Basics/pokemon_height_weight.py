
from bs4 import BeautifulSoup
import requests

pokemon_name = input("Enter the name of pokemon: ")
response = requests.get(f"https://www.pokemon.com/us/pokedex/{pokemon_name}")
content = response.text

soup = BeautifulSoup(content, "html.parser")

pokedex_entry = soup.findAll(name="span", _class="attribute-value")
print(pokedex_entry)
for info in pokedex_entry:
    print(info.getText())