import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/html/html_tables.asp")
#time.sleep(5)
tbl_cont = driver.find_element(By.XPATH,"//div[@class='w3-white w3-padding notranslate w3-padding-16']")
#driver.execute_script("arguments[0].scrollIntoView();", tbl_cont)
#country_name = str(input("please provide country_name:".title()))
country_name='Canada'
time.sleep(2)
input_ele = driver.find_elements(By.XPATH,"//table[@class='ws-table-all']/tbody/tr/td[3]")
company_ele = driver.find_elements(By.XPATH,"//table[@class='ws-table-all']/tbody/tr/td[1]")
# company_name = input("Enter the country here: ")

# for company in range(1,len(company_ele)):
#     print(company_ele[company].text)
driver.close()
for i in range(2,len(input_ele)+1):
    exp_country_text = driver.find_element(By.XPATH,"//table[@class='ws-table-all']/tbody/tr[" + str(i) + "]/td[3]").text
    if exp_country_text == country_name:
        print("requested country is is :",exp_country_text)
        act_company_details = driver.find_element(By.XPATH,"//table[@class='ws-table-all']/tbody/tr[" + str(i) + "]/td[1]").text
        print("company details of requested country is :", act_company_details)