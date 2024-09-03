import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"alertButton").click()
time.sleep(4)
alert = driver.switch_to.alert
time.sleep(3)
alert.accept()
ele = driver.find_element(By.XPATH,"(//*[text()='Click me'])[2]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
ele.click()
WebDriverWait(driver,10).until(EC.alert_is_present())
alert2 = driver.switch_to.alert
alert2.accept()
driver.find_element(By.XPATH,"(//*[text()='Click me'])[3]").click()
alert3 = driver.switch_to.alert
alert3.dismiss()
driver.find_element(By.XPATH,"(//*[text()='Click me'])[4]").click()
alert4 = driver.switch_to.alert
alert4.send_keys("ABHAYA KUMAR")
alert4.accept()
time.sleep(5)
