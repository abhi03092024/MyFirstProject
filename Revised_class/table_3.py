import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')

driver.find_element(By.XPATH,"//button[@type='submit']").click()
#WE an use also this Xpath->(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]
time.sleep(3)
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
time.sleep(2)
count_of_rows=driver.find_elements(By.XPATH,"//div[@class='oxd-table']/div[2]/div")
#//div[@class='oxd-table-body']/div/div/div[3]
print(len(count_of_rows))  #8

time.sleep(8)
for i in range(1,len(count_of_rows)+1):#range(1,9)
    user_admin = driver.find_element(By.XPATH,"//div[@class='oxd-table-body']/div[" + str(i) + "]/div/div[3]").text
    print(user_admin)

    if user_admin == "Admin":
        driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[" + str(i) + "]/div/div[1]").click()
        time.sleep(4)