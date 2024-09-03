import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
total_table_row=driver.find_elements(By.XPATH,"//div[@class='rt-tbody']/div/div")
total_table_col=driver.find_elements(By.XPATH,"//div[@class='rt-tbody']/div[1]/div/div")
email='alden@example.com'
for i in range(1,len(total_table_row)+1): #10
    for j in range(1, len(total_table_col)+1): #7
        table_each_data = driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div[ " +str( i )+"]/div/div[" +str( j )+"]")
        ele_Text=table_each_data.text
        #print(ele_Text)
        if len(ele_Text) == 1:
            break
        if ele_Text == email:
            driver.find_element(By.XPATH, "(//div[@class='rt-tbody']/div[" +str(i)+ "]/div/div/div/span)[1]/*").click()
            time.sleep(2)
            age_element=driver.find_element(By.XPATH,"//input[@id='age']")
            act_text=age_element.text
            age_text=age_element.get_attribute('value')
            age_element.clear()
            age_element.send_keys(str(int(age_text)+1))
            driver.find_element(By.XPATH, "//button[@id='submit']").click()
        print(ele_Text, end="     ")
    print()
    time.sleep(5)