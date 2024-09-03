import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[5]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"//*[text()='Inner HTML']").click()
time.sleep(2)
##How to switch to frame & switch to innerr frame
frame1 = driver.find_element(By.XPATH,"(//*[@id='firstFr'])")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"(//*[@name='fname'])").send_keys("Abhaya kumar")
driver.find_element(By.XPATH,"(//*[@name='lname'])").send_keys("abhaya123@gmail.com")
time.sleep(3)
frame2 = driver.find_element(By.XPATH,"(//iframe[@src='innerFrame'])")
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH,"(//*[@name='email'])").send_keys("milu123@gmail.com")
driver.switch_to.default_content()                                ##To get back from the frame
time.sleep(2)
## if a frame contain multiple frame then we dont need to use default content to get back from the frame..
## If there are multiple frame then we have to get back from the frame to perform in another frame
##By using driver.switch_to.defualt_content()