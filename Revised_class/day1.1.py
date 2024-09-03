import time
from selenium import webdriver
#from selenium.webdriver.support.select import  Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.facebook.com/')
driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()
time.sleep(6)

day_dropdown1 = Select(driver.find_element(By.XPATH,"//select[@id='day']"))

#
# day_dropdown1.select_by_visible_text("1")
# day_dropdown1.select_by_value("7")
# day_dropdown1.select_by_index(19)
# time.sleep(2)
#
all_options=day_dropdown1.options  #For capture all the option from select class..
for i in all_options:
    print(i.text)
time.sleep(3)

# first_value=day_dropdown1.first_selected_option
#print(first_value.text)
# all_value=day_dropdown1.all_selected_options
# for i in all_value:mg
#     print(i.text)
# time.sleep(3)
mon_dd1 = Select(driver.find_element(By.XPATH,"//select[@name='birthday_month']"))
#mon_dd1.select_by_value("5")
#mon_dd1.select_by_visible_text("Jun")
mon_dd1.select_by_index(5)
time.sleep(3)

# select_by_visible_text()
# select_by_value()
# select_by_index()
#
