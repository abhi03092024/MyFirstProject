import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(1)

ele = driver.find_element(By.XPATH,"(//*[@class='card-header-title is-size-3'])[8]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(1)
driver.find_element(By.XPATH,"(//a[@class='card-footer-item'])[8]").click()
time.sleep(2)
elements = driver.find_elements(By.XPATH,"(//div[@class='content'])[1]/ol/li")
for i in elements:
    print(i.text)                        ##To capture multipl;e element


act_text = driver.find_element(By.XPATH,"//li[text()='Type and Enter your Git username']").text
exp_text = "Type and Enter your Git username"
assert act_text == exp_text                 ##To check the text we use this two approach
if act_text == exp_text:
    print("Text check passed")


for ele in elements:
    if ele.text == act_text:
        print(ele.text)