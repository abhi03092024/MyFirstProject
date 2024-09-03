import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
# time.sleep(3)
# driver.find_element(By.ID,"name").send_keys("Abhaya kumar")
# driver.find_element(By.ID,"email").send_keys("abhaya1888@gmail.com")
# driver.find_element(By.ID,"phone").send_keys("7606862957")
# driver.find_element(By.ID,"textarea").send_keys("Odisha,Khodha,barabati")
# time.sleep(2)
# driver.find_element(By.ID,"male").click()
# checkboxes=driver.find_elements(By.XPATH,"(//div[@class='form-group'])[4]/div")
# print(len(checkboxes))
# for checkbox in checkboxes:
#     checkbox.click()
#Select by choice
#-------------------
#ele=driver.find_element(By.ID,"country")
#driver.execute_script("arguments[0].scrollIntoView();",ele)
# time.sleep(4)
# for checkbox in checkboxes:
#     if checkbox.text == "Sunday" or checkbox.text == "Monday":
#         checkbox.click()
# # time.sleep(4)
# # drp_down=Select(driver.find_element(By.XPATH,"(//select[@class='form-control'])[1]"))
# drp_down.select_by_visible_text("France")
# drp_down.select_by_value("uk")
#all_options = drp_down.options
#Without using in_built method
# for opt in all_options:
#     if opt.text == "Australia":
#         opt.click()
# time.sleep(5)
# drp2_option = Select(driver.find_element(By.XPATH,"(//select[@class='form-control'])[2]"))
# drp_down2 = drp2_option.options
# for opt2 in drp_down2:
#     if opt2.text == "Red":
#         opt2.click()
#drp2_option.select_by_visible_text("White")
# time.sleep(3)
# ele2=driver.find_element(By.XPATH,"//input[@class='hasDatepicker']")
#driver.execute_script("arguments[0].scrollIntoView();",ele2)
# time.sleep(2)
# ele2.click()
#Date picker
# month = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
# year = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
# while True:
#     if month == "March" and year == "1999":
#         break
#     else:
#         driver.find_element(By.XPATH," //a[@title='Prev']").click()
# time.sleep(10)
#Alert
# alert_accept = driver.find_element(By.XPATH,"//button[text()='Alert']")
# alert_accept.click()
# alert = driver.switch_to.alert
# time.sleep(4)
# print(alert.text)
# alert.accept()
# time.sleep(3)
# alert_dismiss=driver.find_element(By.XPATH,"//button[text()='Confirm Box']")
# alert_dismiss.click()
# alert.dismiss()
# time.sleep(4)
# alert_prompt = driver.find_element(By.XPATH,"//button[text()='Prompt']")
# alert_prompt.click()
# alert.send_keys("Wellcome")
# alert_text=alert.text
# print(alert_text)
# time.sleep(6)
# doubleClick=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
# action = ActionChains(driver)
# action.double_click(doubleClick).perform()
# time.sleep(5)
# source_ele = driver.find_element(By.XPATH,"//div[@id='draggable']")
# target_ele = driver.find_element(By.XPATH,"//div[@id='droppable']")
# action.drag_and_drop(source_ele,target_ele).perform()
# time.sleep(5)
# slider_ele=driver.find_element(By.XPATH,"//div[@id='slider']/span")
# action.click_and_hold(slider_ele).move_by_offset(100,20).release().perform()
# time.sleep(5)
# frame_id = driver.find_element(By.XPATH,"//iframe[@id='frame-one796456169']")
# driver.switch_to.frame(frame_id)
# driver.find_element(By.XPATH,"//input[@id='RESULT_TextField-0']").send_keys("Abhaya")
# #driver.switch_to.default_content()
# driver.find_element(By.XPATH,"//label[@for='RESULT_RadioButton-1_0']").click()
# time.sleep(5)
ele=driver.find_element(By.XPATH,"//span[@class='icon_calendar']")
driver.execute_script("arguments[0].scrollIntoView();",ele)
WebDriverWait(driver,10).until(EC.ele_is_present())
ele.click()
time.sleep(5)
mon_picker = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
year_picker = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']").text
while True:
    if mon_picker == "March" and year_picker == "1999":
        break
    else:
        driver.find_element(By.XPATH," //span[@class='ui-icon ui-icon-circle-triangle-w']").click()
time.sleep(4)
# resizable_ele = driver.find_element(By.XPATH,"//div[contains(@class,'ui-resizable-handle ui-resizable-se ui-icon')]")
# driver.execute_script("arguments[0].scrollIntoView;",resizable_ele)
# action.click_and_hold(resizable_ele).move_by_offset(90,50).release().perform()
# table=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/td")
# print(len(table))
# for i in table:
#     print(i.text, end =" ")
time.sleep(5)






