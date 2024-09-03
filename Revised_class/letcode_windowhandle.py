import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(2)
header=driver.find_element(By.XPATH,"(//header[@class='card-header'])[7]")
driver.execute_script("arguments[0].scrollIntoView();",header)
time.sleep(1)
ele_tab = driver.find_element(By.XPATH,"//a[text()='Tabs']")
ele_tab.click()
time.sleep(2)
print(driver.current_window_handle)
driver.find_element(By.XPATH,"//button[@id='home']").click()
time.sleep(4)
all_Windows=driver.window_handles      ##To capture all the windows we use-->driver.window_handles
print(all_Windows)
driver.switch_to.window(all_Windows[1])##T0 switch to specific window we use-->driver.switch_to.window(window id or index)
print(driver.title)
driver.switch_to.window(all_Windows[0])
print(driver.title)
for i in all_Windows:
    driver.switch_to.window(i)
    print(driver.title)
    time.sleep(1)

driver.close()  ## driver.close() method will cloase the current window
driver.quit()   ##driver.quit() method will close all windows,,,It will kill the process
time.sleep(2)