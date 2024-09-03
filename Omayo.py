import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
act_title = driver.title
print(act_title)
exp_title = "omayo (QAFox.com)"
assert act_title == exp_title
print("Title check passed")
frame1=driver.find_element(By.NAME,"navbar-iframe")
driver.switch_to.frame(frame1)
driver.find_element(By.ID,"b-query").send_keys("Abhaya")
driver.switch_to.default_content()
frame2=driver.find_element(By.NAME,"navbar-iframe")
driver.switch_to.frame(frame2)
driver.find_element(By.ID,"b-more").click()
window_before=driver.window_handles[0]
driver.switch_to.default_content()
time.sleep(2)
frame3 = driver.find_element(By.XPATH,"//iframe[contains(@style,'margin: 0px; position: absolute; z-index: 1; border-style: none;')]")
driver.switch_to.frame(frame3)
driver.find_element(By.XPATH,"//a[@id='bm-facebook']").click()
time.sleep(2)
driver.switch_to.default_content()
driver.back()
time.sleep(2)
# driver.implicitly_wait(10)
# ele1=driver.find_element(By.XPATH,"//span[@id='home']")
# time.sleep(5)
# ele2=driver.find_element(By.XPATH,"//span[@id='blogsmenu']")
# action = ActionChains(driver)
# action.move_to_element(ele1).move_to_element(ele2).click().perform()
driver.refresh()
options=driver.find_elements(By.XPATH,"//select[@id='multiselect1']/option")
time.sleep(2)
options.select_by_visible_text("Swift")
options.select_by_value("Hyundaix")
time.sleep(5)
