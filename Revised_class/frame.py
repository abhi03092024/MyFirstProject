import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/frame")
time.sleep(4)
##How to perform with an element if the element inside a frame
##First we need to switch to frame by using-->driver.switcch_to.frame(frame id or frame ele or frame name)
# frame_ele=driver.find_element(By.XPATH,"//iframe[@id='firstFr']")
# driver.switch_to.frame(frame_ele)
# ##Now we can perform here..
# driver.find_element(By.XPATH,"//input[@name='fname']").send_keys('Admin')
# ##After performance inside the frame we need to get back from the frame to perform outside of the frame
# ##For this we will use-->driver.switch_to.default_content
# driver.switch_to.default_content()
frame1=driver.find_element(By.XPATH,"//iframe[@src='frameUI']")
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,"//input[@placeholder='Enter name']").send_keys("Abhaya kumar")
frame2 = driver.find_element(By.XPATH,"//iframe[@src='innerFrame']")
driver.switch_to.frame(frame2)
time.sleep(4)
driver.find_element(By.XPATH,"(//input[@name='email'])").send_keys("abhaya@12gmail.com")
driver.switch_to.default_content()
driver.back()
time.sleep(4)