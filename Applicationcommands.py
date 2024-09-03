import time

from selenium import webdriver

from selenium.webdriver.chrome.service import service


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")#Driver.get("URL")its a method to opening the URl..

driver.maximize_window()
print(driver.title)# To capture the title of the current web page
print(driver.current_url)# to capture the current URL of the web page
print(driver.page_source)#to capture the source code of the web page
time.sleep(2)




