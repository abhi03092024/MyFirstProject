import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/")
driver.maximize_window()
sliders=driver.find_elements(By.CLASS_NAME,"carousel-inner")
print(len(sliders))
time.sleep(1)
for ele in sliders:                                     #We uss class name & Tag name for find multiple element
    print(ele.text)
all_elements=driver.find_elements(By.CLASS_NAME,"features_items")
print(len(all_elements))
time.sleep(1)
for all_ele in all_elements:
    print(all_ele.text,end="")
links=driver.find_elements(By.LINK_TEXT,"a")
print(len(links))
driver.find_element(By.ID,"susbscribe_email").send_keys("abhaya1888@gmail.com")
driver.find_element(By.ID,"subscribe").click()

time.sleep(2)


