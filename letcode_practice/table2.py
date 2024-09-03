import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(2)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[14]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[14]").click()
time.sleep(1)
table_cols = driver.find_elements(By.XPATH,"//table[@id='shopping']/tbody/tr/td[2]")
print(len(table_cols))


sum=0

for i in range(1,len(table_cols)+1):
    values = driver.find_element(By.XPATH,"(//table[@id='shopping'])/tbody/tr["+ str(i) +"]/td[2]").text
    v=int(values)
    # print(v)
    sum=sum+v
    print(sum)




