import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[9]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(1)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[9]").click()

drag_ele = driver.find_element(By.XPATH,"//h3[@id='header']")
action = ActionChains(driver)
action.click_and_hold(drag_ele).move_by_offset(118,30).perform()
time.sleep(5)