import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
time.sleep(2)
drag_ele=driver.find_element(By.ID,"draggable")
drop_ele=driver.find_element(By.ID,"droppable")
action = ActionChains(driver)
action.drag_and_drop(drag_ele,drop_ele).perform()
time.sleep(3)
driver.find_element(By.ID,"droppableExample-tab-accept").click()
time.sleep(3)
