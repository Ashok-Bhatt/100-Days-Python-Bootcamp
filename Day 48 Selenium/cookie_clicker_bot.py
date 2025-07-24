from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
web_url = "https://ozh.github.io/cookieclicker/"
game_duration_in_seconds = 5*60

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_url)

time.sleep(5)

language_skip_button = driver.find_element(By.ID, value="promptClose")
driver.execute_script("arguments[0].click();", language_skip_button)

time.sleep(2)

start_time  = time.time()
last_upgrade_time = time.time()
cookie = driver.find_element(By.ID, value="bigCookie")
cookie_per_second = 0

while ((time.time() - start_time) < game_duration_in_seconds):
    cookie.click()

    if ((time.time() - last_upgrade_time) > 10):
        
        enabled_products = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
        if (len(enabled_products) > 0):
            try:
                enabled_products[len(enabled_products)-1].click()
            except Exception as e:
                print(e)
        last_upgrade_time = time.time()

    try:
        cookie_per_second = driver.find_element(By.CSS_SELECTOR, value="#cookies #cookiesPerSecond").text
    except Exception:
        continue

time.sleep(2)
print(f"cookies {cookie_per_second}")

driver.close()