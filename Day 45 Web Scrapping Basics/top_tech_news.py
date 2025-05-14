
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_content_text = response.text

soup = BeautifulSoup(web_content_text, "html.parser")

data = soup.select(selector="span.titleline>a")
upvotes = soup.findAll(name="span", class_="score")

news_title = [title.getText() for title in data]
news_link = [link.get("href") for link in data]
upvotes_list = [int(upvote.getText().split()[0]) for upvote in upvotes]

index = 1
for title, link, upvote in zip(news_title, news_link, upvotes_list):
    print(f"{index}. News Headline: {title}")
    print(f"News Link: {link}")
    print(f"News Upvotes: {upvote}\n")
    index = index + 1

most_upvotes_index = upvotes_list.index(max(upvotes_list))
print(f"Most Upvoted Website: {news_title[most_upvotes_index]}")
print(f"Link: {news_link[most_upvotes_index]}")
print(f"Upvotes: {upvotes_list[most_upvotes_index]}")
print(f"Total amount of upvotes: {sum(upvotes_list)}")