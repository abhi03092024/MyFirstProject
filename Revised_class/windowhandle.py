import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/browser-windows")

new_tab=driver.find_element(By.XPATH,"//button[@id='tabButton']")
driver.execute_script("arguments[0].scrollIntoView();",new_tab)
