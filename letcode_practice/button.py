import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//*[text()='Click']").click()
driver.find_element(By.ID,"home").click()
driver.back()
loc = driver.find_element(By.ID,"position")
print(loc.location)
col=driver.find_element(By.ID,"color")
print(col.get_attribute("value"))
property=driver.find_element(By.ID,"property")
print(property.get_property("value"))
disable_ele = driver.find_element(By.ID,"isDisabled")
print(disable_ele.is_enabled())
click_hold_button = driver.find_element(By.XPATH,"//*[@id='isDisabled']")
action = ActionChains(driver)
action.click_and_hold(click_hold_button).perform()

time.sleep(4)