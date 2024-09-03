import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
# Select dropdown by using select class built_in method
drp_select=Select(driver.find_element(By.XPATH,"//select[@class='form-control']"))
# drp_select.select_by_value("Tuesday")
# drp_select.select_by_visible_text("Friday")
drp_select2 = Select(driver.find_element(By.XPATH,"//select[@id='multi-select']"))
drp_select2.select_by_value("New York")
drp_select2.select_by_visible_text("Washington")
#Capture all the optons and print them
#all_options = drp_select.options
# print(len(all_options))
# for opt in all_options:
#     print(opt.text)

#How to select options without using built-in methood
all_options = drp_select2.options
for opt in all_options:
    if opt.text == "New York" and opt == "Washington":
        opt.click()


time.sleep(4)