from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
web_url = "https://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_url)

first_name_field = driver.find_element(By.CSS_SELECTOR, value=".form-control.top")
first_name_field.send_keys("Ashok")

last_name_field = driver.find_element(By.CSS_SELECTOR, value=".form-control.middle")
last_name_field.send_keys("Bhatt")

email_field = driver.find_element(By.CSS_SELECTOR, value=".form-control.bottom")
email_field.send_keys("ashokbhatt2048@gmail.com")

button_field = driver.find_element(By.TAG_NAME, value="button")
button_field.send_keys(Keys.ENTER)

time.sleep(2)

driver.close()