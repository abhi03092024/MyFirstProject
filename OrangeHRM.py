import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
act_title = driver.title
print(act_title)
exp_title = "OrangeHRM"
assert act_title == exp_title
print("Code passed")
driver.find_element(By.XPATH,"//input[@placeholder='Username'][1]").send_keys("Admin")
driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[1]").send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(@class,'oxd-button')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]").click()
time.sleep(2)
count_all_rows=driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div")
print(len(count_all_rows))
# for ele in range(1,len(count_all_rows)):
#     if ele == driver.find_element(By.XPATH,"(//i[contains(@class,'oxd-icon bi-check')])[1]"):


time.sleep(4)