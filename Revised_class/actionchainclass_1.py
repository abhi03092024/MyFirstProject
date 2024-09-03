import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://demoqa.com/resizable")

# resizable_ele = driver.find_element(By.XPATH,"//div[@id='resizable']")
arrow_ele = driver.find_element(By.XPATH,"(//span[contains(@class,'react-resizable')])[2]")
driver.execute_script("arguments[0].scrollIntoView()",arrow_ele)

action=ActionChains(driver)
#action.click_and_hold(arrow_ele).move_by_offset(400,200).release().perform()
action.click_and_hold(arrow_ele).move_by_offset(500,300).release().perform()
time.sleep(5)

##Action Chains Note
'''In python selenium actionchains are used to simulate complex useer interaction , like mose movements,drag & drop
right click, double click 
import-->from selenium.webdriver.common.action_chains import Actionchains
action = ActionChains(driver)
To mouse hover-->ActionChains(driver).move_to_element(element).perform()
To right click-->ActionChains(driver).context_click(element).perform().'''

