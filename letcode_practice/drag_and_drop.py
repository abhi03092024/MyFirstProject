import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[10]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(1)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[10]").click()

source_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
target_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")
action = ActionChains(driver)
action.drag_and_drop(source_ele,target_ele).perform()
time.sleep(5)