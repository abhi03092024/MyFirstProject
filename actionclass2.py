import time

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# driver.get("https://demoqa.com/selectable")
# driver.maximize_window()
# print(driver.title)
# time.sleep(2)
# list=driver.find_element(By.XPATH,"//ul[@class='vertical-list-container mt-4 list-group']/li[1]")
# action = ActionChains(driver)
# action.move_to_element(list).perform()
# print(list.is_selected())  #Not getting selected
# time.sleep(5)
driver.get("https://demoqa.com/resizable")
driver.maximize_window()
time.sleep(2)
resizable=driver.find_element(By.XPATH,"//div[@id='resizable']")
driver.execute_script("arguments[0].scrollIntoView;",resizable)
ele=driver.find_element(By.XPATH,"//div[@id='resizableBoxWithRestriction']")
action = ActionChains(driver)
action.click_and_hold(ele).move_by_offset(100,30).release().perform()
time.sleep(8)