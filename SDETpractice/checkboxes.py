import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
time.sleep(2)
#how to select specific checkbox ?
driver.find_element(By.ID,"isAgeSelected").click()
#How to select all checkboxes ?
ele = driver.find_element(By.XPATH,"//input[@type='button']")
driver.execute_script("arguments[0].scrollIntoView;",ele)
time.sleep(4)
checkboxes = driver.find_elements(By.XPATH,"//div[@class='checkbox']/label//input")
# for checkbox in checkboxes:
#      checkbox.click()
for i in checkboxes:
    options = i.get_attribute("value")
    if options == "Option 3" and options == "Option 4":
        i.click()
time.sleep(5)



# for checkbox in checkboxes:
#     checkbox.click()
#How to select multiple checkbox by choice
# for checkbox in checkboxes:
#     check_box = checkbox.get_attribute("value")
#     if check_box == 'Option 1' or check_box == 'Option 3':
#         checkbox.click()
#How to select last two checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()
#How to select first 2 checkboxes:
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()
# #How to select middle 2 checkboxes
# for i in range(len(checkboxes)-3,len(checkboxes)-1):
#     checkboxes[i].click()


time.sleep(5)