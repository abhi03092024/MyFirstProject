import time

from selenium import webdriver
from selenium.webdriver.common.by import By



driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/webtables')
table_first_data=driver.find_element(By.XPATH,"//div[text()='Cierra']").text
print(table_first_data)
table_first_row_data=driver.find_elements(By.XPATH,"//div[@class='rt-tbody']/div/div/div[1]")
#We cna use below XPATH as well..
#table_first_row_data=driver.find_elements(By.XPATH,"//div[@class='rt-table']/div[2]/div/div/div[1]")
# for element in table_first_row_data:
#     ele_Text=element.text
#     print(ele_Text)
# time.sleep(5)

#How to capture all the data from the table
rows = driver.find_elements(By.XPATH,"//div[contains(@class,'rt-table')]/div[2]/div")
cols = driver.find_elements(By.XPATH,"//div[contains(@class,'rt-table')]/div[2]/div[1]/div/div")

for r in range(1,len(rows)):
    for c in range(1,len(cols)):
        print(rows[r].text)
        print(cols[c].text)


