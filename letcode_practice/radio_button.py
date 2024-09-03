import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[6]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[6]").click()
driver.find_element(By.XPATH,"//input[@id='no']").click()
rd_1=(driver.find_element(By.XPATH,"//input[@id='one']"))
rd_1.click()
print(rd_1.is_selected())
rd_2=driver.find_element(By.XPATH,"//input[@id='nobug']")
rd_2.click()
print(rd_2.is_selected())
enable_button = driver.find_element(By.XPATH,"//input[@id='maybe']")
print(enable_button.is_enabled())
time.sleep(2)
