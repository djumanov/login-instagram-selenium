from dotenv import load_dotenv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
username = os.getenv('username')
password = os.getenv('password')

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/')
driver.implicitly_wait(5)

username_element = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
password_element = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

username_element.clear()
username_element.send_keys(username)

time.sleep(5)

password_element.clear()
password_element.send_keys(password)

time.sleep(5)

submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn.submit()

time.sleep(5)

driver.close()
driver.quit()
