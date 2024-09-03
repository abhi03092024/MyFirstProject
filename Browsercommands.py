import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
text=driver.find_element(By.XPATH,"//input[@placeholder='Username']")
text.send_keys("Admin")
time.sleep(3)
#driver.implicitly_wait(5)

