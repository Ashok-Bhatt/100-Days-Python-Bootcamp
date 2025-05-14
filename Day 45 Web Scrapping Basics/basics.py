from bs4 import BeautifulSoup

with open("index.html") as file:
    content = file.read()

# sometimes you may need to import lxml package and pass it to BeautifulSoup object instead of html.parser
soup = BeautifulSoup(content, "html.parser")

print(soup, end="\n\n")
print(soup.prettify(), end="\n\n")      # cointains appropriate spaces and tabs

print(soup.title)
print(soup.title.name)
print(soup.title.string)

# to get first paragraph of soup object
print(soup.p)

# to get all paragraph of soup object
all_paragraphs = soup.find_all(name="p")
print(all_paragraphs, "\n")

# to get only text
for tag in all_paragraphs:
    print(tag.getText(), "\n\n\n")

# to get links
all_links = soup.find_all(name="a")
print(all_links, "\n")

# to get actual links
for link in all_links:
    print(link.get("href"))


# to search using id
paragraph1 = soup.find(name="p", id="p1")
print(paragraph1)

# to search using class
paragraph2 = soup.find(name="p", class_="ud")
print(paragraph2)
print(paragraph2.get("id"))

# Using CSS Selectors
print(soup.select_one(selector="p a"))
print(soup.select(selector="p a"))
print(soup.select(selector="#p4"))