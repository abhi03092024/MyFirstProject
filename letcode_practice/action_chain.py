import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[12]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[12]").click()
ele1 = driver.find_element(By.XPATH,"(//div[@id='selectable'])[1]")
ele2 = driver.find_element(By.XPATH,"(//div[@id='selectable'])[2]")
ele3 = driver.find_element(By.XPATH,"(//div[@id='selectable'])[3]")
ele4 = driver.find_element(By.XPATH,"(//div[@id='selectable'])[4]")
action = ActionChains(driver)
action.click_and_hold(ele1).move_to_element(ele2).move_to_element(ele3).move_to_element(ele4).perform()
time.sleep(4)
