import datetime
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//header[@class='card-header'])[7]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"//a[text()='Tabs']").click()
driver.find_element(By.XPATH,"//button[text()='Open Home Page']").click()
# current_window = driver.current_window_handle  #To capture current window
# print(current_window)
all_windows = driver.window_handles        #To capture all windows
print(all_windows)                         #It will return a list
# parentwindow_ID = all_windows[0]
# driver.switch_to.window(parentwindow_ID)    #To switch to parent window
#driver.close()
# time.sleep(5)
# childwindow_ID = all_windows[1]
# driver.switch_to.window(childwindow_ID)
# driver.close()                           ##To switch to child window
# time.sleep(3)
# for wind in all_windows:
#     driver.switch_to.window(wind)         #Switch to all windowsss
#     print(driver.title)                     #To capture the title of window
# time.sleep(3)
##How to close a specific window from multiple window
# for wind in all_windows:
#     driver.switch_to.window(wind)
#     if driver.title == "Window handling - LetCode":
#         driver.close()
#         time.sleep(4)

##How to close two specific window
for wind in all_windows:
    driver.switch_to.window(wind)
    if driver.title == "Window handling - LetCode" and driver.title == "LetCode - Testing Hub":
        driver.close()
        time.sleep(8)