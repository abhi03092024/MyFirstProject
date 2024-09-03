import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://demoqa.com/resizable")

resizable_ele = driver.find_element(By.XPATH,"//div[@id='resizableBoxWithRestriction']")
arrow_ele = driver.find_element(By.XPATH,"//div[@id='resizableBoxWithRestriction']/span")
driver.execute_script("arguments[0].scrollIntoView()",resizable_ele)

action=ActionChains(driver)
action.click_and_hold(arrow_ele).move_by_offset(100,30).release().perform()
time.sleep(9)



