import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://demoqa.com/selectable")

selectable_sub_menu = driver.find_element(By.XPATH,"//a[@id='demo-tab-list']")
driver.execute_script("arguments[0].scrollIntoView()",selectable_sub_menu)
# list_first_ele = driver.find_element(By.XPATH,"//ul[@id='verticalListContainer']/li[1]")
# list_second_ele = driver.find_element(By.XPATH,"//ul[@id='verticalListContainer']/li[2]")
all_ele = driver.find_elements(By.XPATH,"//ul[@id='verticalListContainer']/li")
action=ActionChains(driver)

##How to hover the mouse in multiple element by chaining system---Aproach--1
#action.move_to_element(list_first_ele).click().move_to_element(list_second_ele).click().perform()

##Aproach--2
for ele in all_ele:
    action.move_to_element(ele).click().perform()

time.sleep(6)
