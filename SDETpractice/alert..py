import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Dialog']").click()
time.sleep(2)
#alert1-->Too accept the alert
# driver.find_element(By.XPATH,"//button[text()='Simple Alert']").click()
# my_alert = driver.switch_to.alert
# alert_txt = my_alert.text
# print(alert_txt)
# my_alert.accept()
# time.sleep(4)
#alert2-->To dismiss the alert & print the alert text
# driver.find_element(By.XPATH,"//button[text()='Confirm Alert']").click()
# my_alert2 = driver.switch_to.alert
# alert_txt = my_alert2.text
# print(alert_txt)
# my_alert2.dismiss()
# time.sleep(3)

# #promptalert3-->To send the text to the alert
# driver.find_element(By.XPATH,"//button[text()='Prompt Alert']").click()
# my_alert3 = driver.switch_to.alert
# my_alert3.send_keys("Well come to abhaya world")
# my_alert3.accept()
# time.sleep(4)
#
# # #sweetalert4-->
driver.find_element(By.XPATH,"//button[text()='Modern Alert']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='modal-close is-large']").click()
time.sleep(2)