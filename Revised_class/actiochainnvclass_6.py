import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(4)
search_box=driver.find_element(By.XPATH,"//input[@name='q']")
search_box.send_keys("iphone")
time.sleep(2)
search_box.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
search_box.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
search_box.send_keys(Keys.ENTER)
time.sleep(3)
### Whenever we search for any element we can't find the Xpath or element from the web page...
#We can pause the screen to find the Xpath of that specific search element by using below statements
##--->setTimeout(function(){debugger;},5000);
