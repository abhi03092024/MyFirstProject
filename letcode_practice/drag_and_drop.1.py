import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[11]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[11]").click()
source_ele1 = driver.find_element(By.XPATH,"(//div[@id='sample-box1'])[1]")
target_ele1 = driver.find_element(By.XPATH,"//div[text()=' Check e-mail']")
action = ActionChains(driver)
action.drag_and_drop(source_ele1,target_ele1).perform()
time.sleep(2)
source_ele2 = driver.find_element(By.XPATH,"//*[text()=' Pick up groceries']")
target_ele2 = driver.find_element(By.XPATH,"//*[text()=' Walk dog']")
action.drag_and_drop(source_ele2,target_ele2).perform()
time.sleep(3)