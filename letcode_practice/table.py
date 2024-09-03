import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(2)

ele1 = driver.find_element(By.XPATH,"(//p[@class='card-header-title is-size-3'])[14]")
driver.execute_script("arguments[0].scrollIntoView();",ele1)
driver.find_element(By.XPATH,"//a[text()='Simple table']").click()
time.sleep(3)
cols = driver.find_elements(By.XPATH,"//table[@id='shopping']/tbody/tr/td[2]")
sum = 0
for i in range(1,len(cols)+1):
    values = driver.find_element(By.XPATH,"//table[@id='shopping']/tbody/tr[" + str(i) + "]/td[2]").text
    print(values)

    v = int(values)
    sum= sum + v
    #v = v + 1
print(sum)


