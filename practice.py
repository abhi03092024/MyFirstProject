import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()

driver.get("https://omayo.blogspot.com/")

driver.maximize_window()
#driver.implicitly_wait(10)
act_title=driver.title
exp_title = "omayo (QAFox.com)"
#option 1 to check title..
if act_title == exp_title:
    print("title test passed")
else:
    print("Title test failed")
#Option 2 to check title..
assert exp_title == act_title
print("passed")
frame1=driver.find_element(By.ID,"navbar-iframe")
driver.switch_to.frame(frame1)
driver.find_element(By.NAME,"q").send_keys("abhaya")
driver.find_element(By.XPATH,"//a[@id='b-query-icon']").click()
time.sleep(1)
driver.switch_to.default_content()
frame2=driver.find_element(By.XPATH,"//iframe[@id='navbar-iframe']")
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH,"//a[@tabindex='4']").click()
window_before = driver.window_handles[0]
print(window_before)
driver.switch_to.default_content()
time.sleep(3)
frame3=driver.find_element(By.XPATH,"//iframe[@id='more-iframe']")
driver.switch_to.frame(frame3)
driver.find_element(By.XPATH,"//div[@id='container']/ul/li[1]").click()
window_after = driver.window_handles[1]
time.sleep(1)
print(window_after)
driver.switch_to.window(window_before)
home=driver.find_element(By.ID,"home")
action = ActionChains(driver)
action.move_to_element(home).perform()
time.sleep(1)
blogs=driver.find_element(By.CLASS_NAME,"has-sub")
action.move_to_element(blogs).move_to_element(home).perform()
blogs.click()
driver.find_element(By.XPATH,"//a[@href='http://www.seleniumone-by-arun.blogspot.com']").click()
driver.back()
driver.find_element(By.XPATH,"//a[text()='http://www.Selenium143.blogspot.com']").click()
time.sleep(1)
driver.switch_to.window(window_before)
driver.find_element(By.XPATH,"//option[@value='volvox']").click()
driver.find_element(By.ID,"drop1").click()
time.sleep(1)
driver.find_element(By.XPATH,"//select[@id='drop1']//option[@value='ghi']").click()

time.sleep(2)

