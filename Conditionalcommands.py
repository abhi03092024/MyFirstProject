import time

from selenium import webdriver

from selenium.webdriver.chrome.service import service

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.implicitly_wait(5)
search_box = driver.find_element(By.XPATH,"//input[@name='q']")
print("Display status",search_box.is_displayed())
print("Display status",search_box.is_enabled())
x = driver.find_element(By.XPATH,"//label[@for='gender']")
#y = driver.find_element(By.XPATH,"//span[@class='female']")
# print(x.is_selected())
# print(y.is_selected()) #Why its showing error
# time.sleep(5)


