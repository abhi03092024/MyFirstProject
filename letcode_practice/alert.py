import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//*[text()='Dialog']").click()
driver.find_element(By.XPATH,"//*[text()='Simple Alert']").click()
time.sleep(1)
my_alert1 = driver.switch_to.alert
time.sleep(1)
my_alert1.accept()                                                          ##To accept the alert
driver.find_element(By.XPATH,"//*[@id='confirm']").click()
my_alert2 = driver.switch_to.alert
my_alert2.dismiss()                                                         ##To dismiss the alert
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='prompt']").click()
my_alert3 = driver.switch_to.alert
my_alert3.send_keys("Welcome Abhaya")                                       ##To send kyes alert
time.sleep(2)
print(my_alert3.text)
my_alert3.accept()
time.sleep(3)