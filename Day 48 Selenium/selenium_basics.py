from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
web_url = "https://www.geeksforgeeks.org/user/ashokbhacjou/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_url)

username = driver.find_element(By.CLASS_NAME, value="profilePicSection_head_userHandle__oOfFy").text
problems_solved = driver.find_element(By.CSS_SELECTOR, ".scoreCard_head__nxXR8 .scoreCard_head_left--score__oSi_x").text
problems_count = driver.find_elements(By.CLASS_NAME, value="problemNavbar_head_nav--text__UaGCx")

print(f"Username : {username}")
print(f"Problems Solved: {problems_solved}")

for itr in problems_count:
    print(itr.text)

driver.close()