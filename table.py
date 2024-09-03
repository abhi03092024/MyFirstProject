import time
import random
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH,"(//a[@class='oxd-main-menu-item'])[1]").click()
time.sleep(3)
ele = driver.find_element(By.XPATH,"(//button[@type='button'])[1]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(5)
cols=driver.find_elements(By.XPATH,"//div[@class='oxd-table-body']/div/div/div[3]")
r_values=len(cols)
for i in range(1,r_values+1):
    user_admin = driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div["+ str(i) +"]/div/div[3]").text
    if user_admin == "ESS":
        driver.find_element(By.XPATH,"(//i[@class='oxd-icon bi-pencil-fill'])[1]").click()
        time.sleep(1)
        emp_name=driver.find_element(By.XPATH,"//input[@autocomplete='off']")
        emp_name.clear()
        emp_name.send_keys("Abhaya123456")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        print(emp_name)
        time.sleep(10)