import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[14]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[14]").click()
time.sleep(2)
names = driver.find_elements(By.XPATH,"(//table[@class='table is-fullwidth is-bordered'])/tbody/tr/td[2]")
print(len(names))
time.sleep(2)
ele = driver.find_elements(By.XPATH,"(//table[@class='table is-fullwidth is-bordered'])")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(3)
#driver.find_element(By.XPATH,"(//table[@class='table is-fullwidth is-bordered'])/tbody/tr[2]/td[4]").click()

for i in range(1,len(names)+1):
    name_raj = driver.find_element(By.XPATH,"(//table[@class='table is-fullwidth is-bordered'])/tbody/tr["+ str(i) +"]/td[2]").text
    print(name_raj)
    if name_raj == "Raj":
        driver.find_element(By.XPATH,"(//table[@class='table is-fullwidth is-bordered'])/tbody/tr[2]/td[4]").click()

        time.sleep(5)




