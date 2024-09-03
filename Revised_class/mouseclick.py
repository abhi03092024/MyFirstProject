import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//input[@name='q']").send_keys("iphone 15")
time.sleep(2)
search_box_all_item = driver.find_elements(By.XPATH,"//ul[@class='_1sFryS _2x2Mmc _3ofZy1']/li/div/a/div[2]")
for item in search_box_all_item:
    print(item)
    each_text=item.text
    print(each_text)
    if each_text == 'iphone 15 pro':
        item.click()
        time.sleep(4)
        print("you have successfully clicked the item")
        break
    print(each_text)

time.sleep(4)