import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(1)
searchbox=driver.find_element(By.ID,"twotabsearchtextbox")
searchbox.click()
searchbox.send_keys("ipad")
searchbox.send_keys(Keys.ARROW_DOWN)
searchbox.send_keys(Keys.ARROW_DOWN)
searchbox.send_keys(Keys.ARROW_DOWN)
searchbox.send_keys(Keys.ARROW_DOWN)
searchbox.send_keys(Keys.CONTROL,"a")
searchbox.send_keys(Keys.CONTROL,"c")
searchbox.clear()
searchbox.send_keys(Keys.CONTROL,"v")
time.sleep(4)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)



# search_box = driver.find_element(By.ID,"twotabsearchtextbox")
# search_box.click()
# search_box.send_keys("Treding book")
# time.sleep(3)
# search_box.send_keys(Keys.ARROW_DOWN)
# search_box.send_keys(Keys.ARROW_DOWN)
# time.sleep(1)
# search_box.send_keys(Keys.ARROW_DOWN)
# time.sleep(2)
# search_box.send_keys(Keys.CONTROL,"a")
# search_box.send_keys(Keys.CONTROL,"c")
# search_box.clear()
# search_box.send_keys(Keys.CONTROL,"v")
# time.sleep(3)
# driver.find_element(By.XPATH,"(//input[@type='submit'])[1]").click()
# time.sleep(2)


#>>>>>>>>>>>>>>>Flipcart<<<<<<<<<<<<<<<
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# time.sleep(4)
# search_box=driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
# search_box.send_keys("iphone")
# time.sleep(2)
# search_box.send_keys(Keys.ARROW_DOWN)
# time.sleep(2)
# search_box.send_keys(Keys.ARROW_DOWN)
# time.sleep(1)
#
# search_box.send_keys(Keys.ARROW_DOWN)
# time.sleep(1)
#
# search_box.send_keys(Keys.ARROW_DOWN)
# time.sleep(1)
#
# search_box.send_keys(Keys.CONTROL,"a")
# time.sleep(2)
# search_box.send_keys(Keys.CONTROL,"c")
# search_box.clear()
# search_box.send_keys(Keys.CONTROL,"v")
# time.sleep(4)
# driver.find_element(By.XPATH,"//button[@type='submit']").click()









