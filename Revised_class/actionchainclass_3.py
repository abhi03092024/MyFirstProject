import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://demoqa.com/droppable")

source_ele = driver.find_element(By.XPATH,"(//div[@id='draggable'])[1]")
target_ele = driver.find_element(By.XPATH,"(//div[@id='droppable'])[1]")
driver.execute_script("arguments[0].scrollIntoView()",source_ele)
action=ActionChains(driver)
#action.click_and_hold(source_ele).move_to_element(target_ele).release().perform() ##Aproach-1
action.drag_and_drop(source_ele,target_ele).perform() ##Aproach-2
time.sleep(6)

##Drag_and_drop
