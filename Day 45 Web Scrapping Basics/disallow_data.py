
import requests
from bs4 import BeautifulSoup

response = requests.get(input("Enter the url of required website: ")+"/robots.txt")
web_text = response.text.split("\n")
not_allowed = [line for line in web_text if line.startswith("Disallow:")]

for line in not_allowed:
    print(line)

print(f"\n\t{len(not_allowed)} items not allowed")