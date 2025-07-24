from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
web_url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_url)

articles_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a').text
print(f"English Articles Count in Wikipedia: {articles_count}")

driver.close()