import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/alerts")

driver.implicitly_wait(10)
##We use implictly wait in our script for all the element,,Its a global wait
##It works based on time
time.sleep(2)
driver.find_element(By.XPATH,"(//button[text()='Click me'])[1]").click()
time.sleep(1)
my_alert = driver.switch_to.alert
my_alert.accept()
time.sleep(6)


alert2=driver.find_element(By.ID,"timerAlertButton")
driver.execute_script("arguments[0].scrollIntoView();",alert2)
alert2.click()
time.sleep(6)
# my_alert2 = driver.switch_to.alert
# my_alert2.accept()
WebDriverWait(driver,10).until(EC.alert_is_present())
##We use explicit wait for a single element where the condition is satisfying
##It works based on Condition
my_alert2 = driver.switch_to.alert
my_alert2.accept()
time.sleep(6)



# alert=Alert(driver) # to handle alert in web page we have to use Alert class and inside that we need to pass driver instance
# alert.accept()# to click on ok button
# alert.dismiss()# to click on cancel button
# alert.send_keys()# to send data to the alert
# alert_text=alert.text  #   to fetch data from alert
#
#
# alert3=driver.find_element(By.ID,"confirmButton")
# driver.execute_script("arguments[0].scrollIntoView();",alert3)
# alert3.click()
# time.sleep(4)
# #WebDriverWait(driver,10).until(EC.alert_is_present())
# my_alert3 = driver.switch_to.alert
# my_alert3.dismiss()
# time.sleep(8)

##Alert 4
alert4=driver.find_element(By.ID,"promtButton")
driver.execute_script("arguments[0].scrollIntoView();",alert4)
alert4.click()
time.sleep(4)
my_alert4=driver.switch_to.alert
print(my_alert4.text)              ##To print the text of alert
my_alert4.send_keys("abhya kumar") ##We can send some text to the alert input box by-->driver.switch_to.alert.send_keys()
my_alert4.accept()
time.sleep(4)
print(alert4.text)
time.sleep(6)
alert4.send_keys("Abhaya kumar")



#alert.dismiss()
#print(alert4_1.text)

