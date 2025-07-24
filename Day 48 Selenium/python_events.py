from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
web_url = "https://www.python.org/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_url)

events = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last ul li")
events_dictionary = {}

for index, event in enumerate(events):
    event_name = event.find_element(By.CSS_SELECTOR, value="a").text
    event_date = event.find_element(By.CSS_SELECTOR, value="time").text
    events_dictionary[index] = {"event_date" : event_date, "event_name" : event_name}

print(events_dictionary)

driver.close()