import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[7]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(1)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[7]").click()
driver.find_element(By.XPATH,"(//*[@id='home'])").click()
current_window = driver.current_window_handle            ##To capture current window
print(current_window)
all_windows = driver.window_handles
print(all_windows)                                      ##To capture all windows
for wind in all_windows:
    driver.switch_to.window(wind)                        ##To switch to windows
    print(driver.title)                                  ##To capture windows title..

parent_window = all_windows[0]
child_window = all_windows[1]
driver.switch_to.window(parent_window)
driver.switch_to.window(child_window)
time.sleep(4)