import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)

cookies = driver.get_cookies()
print(len(cookies))

#To Print all cookies
for cook in cookies:
    print(cook)
#To add cookies
driver.add_cookie({"name":"Abhaya","value":"123456"})
print(len(cookies))
driver.get_cookies()

#To delete cookies
# driver.delete_cookie("my cookie")
# print(len(cookies))
# driver.get_cookies()