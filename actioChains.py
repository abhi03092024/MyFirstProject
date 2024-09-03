import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/sortable")
driver.maximize_window()
act_title=driver.title
print(act_title)
ele = driver.find_element(By.XPATH,"(//div[text()='Six'])[1]")
driver.execute_script("arguments[0].scrollIntoView;",ele)
source_ele=driver.find_element(By.XPATH,"(//div[text()='Two'])[1]")
target_ele=driver.find_element(By.XPATH,"(//div[text()='One'])[1]")
action = ActionChains(driver)
action.drag_and_drop(source_ele,target_ele).perform()
time.sleep(6)