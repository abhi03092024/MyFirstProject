import time
from selenium import webdriver
from selenium.webdriver.support.select import  Select
from selenium.webdriver.common.by import By



driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.functionize.com/free-trial')
time.sleep(4)
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("pintu")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("samal")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("samaldusmantafj@gmail.com")
driver.find_element(By.XPATH,"//input[@name='phone']").send_keys('7854656789')
driver.find_element(By.XPATH,"//input[@name='company']").send_keys('hp.com')
job_role_dropdown=Select(driver.find_element(By.XPATH,"//select[@name='job_role']"))
job_role_dropdown.select_by_visible_text("Quality Engineer / SDET")
# How to select ele from Dropdown
# To select data by using select class     #First we need to import Select class
total_size_dropdown=Select(driver.find_element(By.XPATH,"//select[@name='total_size_of_test_suite']"))
total_size_dropdown.select_by_visible_text("501-1000")

upcoming_projects_dropdown=Select(driver.find_element(By.XPATH,"//select[@name='any_upcoming_projects_that_require_test_automation_']"))
upcoming_projects_dropdown.select_by_value("Upgrades")

# ##To click checkboxes individually
# driver.find_element(By.XPATH,"//input[@id='i_m_interested_in_learning_more_about0-46e27199-313a-4a78-bd72-b85b29dd0158']").click()
# driver.find_element(By.XPATH,"//input[@id='i_m_interested_in_learning_more_about1-46e27199-313a-4a78-bd72-b85b29dd0158']").click()
# #Click on radio button
# driver.find_element(By.XPATH,"(//input[@name='do_you_have_any_hands_on_experience_with_selenium_or_other_scripted_automation_'])[1]").click()
###How to select multiple check boxes..
##driver.find_elements return a collection of list
checkboxes=driver.find_elements(By.XPATH,"(//li[@class='hs-form-checkbox']/label/input)")
# print(len(checkboxes))
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
# ###To select ceck boxes by choice
# for i in range(len(checkboxes)):
#     if i % 2 != 0:
#         checkboxes[i].click()
####To check first two check boxes...
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()


time.sleep(8)
