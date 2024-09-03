import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://letcode.in/test")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//*[text()='Drop-Down']").click()
drp_down1 = Select(driver.find_element(By.ID,"fruits"))    ## To select by select class
print(drp_down1.is_multiple)
drp_down1.select_by_index(4)
drp_down1.select_by_visible_text("Mango")
drp_down1.select_by_value("3")
time.sleep(2)
drp_down2 = Select(driver.find_element(By.ID,"superheros"))
options = drp_down2.options
for opt in options:                                          ##To click drop down by using op[tion
    if opt.text == "Batman":
        opt.click()
for opt2 in options:                                          ##To capture all the element from drop down
    print(opt2.text)
time.sleep(2)
drp_down3 = Select(driver.find_element(By.ID,"lang"))   ##To select first selected option
print(drp_down3.first_selected_option.text)