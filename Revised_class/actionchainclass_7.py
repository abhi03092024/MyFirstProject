import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(4)
interaction_ele=driver.find_element(By.XPATH,"(//div[@class='card-body'])[6]")
driver.execute_script("arguments[0].scrollIntoView();",interaction_ele)
time.sleep(4)
interaction_ele.click()
time.sleep(4)
actual_text = "Glenn Block et al."
driver.refresh()
time.sleep(5)
table_ele = driver.find_element(By.XPATH,"//div[@class='rt-table']")
driver.execute_script("arguments[0].scrollIntoView();",table_ele)
time.sleep(4)
list_of_auther_name = driver.find_elements(By.XPATH,"//div[@class='rt-table']/div[2]/div/div/div[3]")

for i in range(1,len(list_of_auther_name)+1):
    expected_text=driver.find_element(By.XPATH, "//div[@class='rt-table']/div[2]/div["+str(i)+"]/div/div[3]").text
    if expected_text == actual_text:
        title_text=driver.find_element(By.XPATH,"//div[@class='rt-table']/div[2]/div["+str(i)+"]/div/div[3]/preceding-sibling::div[1]/div/span/a").text
        print(f"{actual_text } title is {title_text}")