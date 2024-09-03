from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//*[@class='card-footer-item']").click()
name_box = (driver.find_element(By.ID,"fullName"))
name_box.send_keys("Abhaya kumar")
print(name_box.is_displayed())
driver.find_element(By.ID,"join").send_keys("Millu")
text1 = driver.find_element(By.ID,"getMe")
print(text1.get_attribute("value"))
driver.find_element(By.ID,"clearMe").clear()
enable_ele = driver.find_element(By.ID,"noEdit")
print(enable_ele.is_enabled())
read_box=driver.find_element(By.ID,"dontwrite")
print(read_box.get_attribute("value"))
time.sleep(4)