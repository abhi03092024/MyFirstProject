import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.back() #To back to the 1st window
time.sleep(3)
driver.forward() #To forward to the 2nd window
time.sleep(3)
driver.refresh() #To refresh the window
time.sleep(3)

