import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)
#Locators matching with single element
search_box = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
search_box.send_keys("Apple MacBook Pro 13-inch")
element=driver.find_elements(By.LINK_TEXT,"Sitemap")
print(len(element))
#Locators matching with multiple elements
elements = driver.find_elements(By.XPATH,"//div[@class='footer']/div/div/ul/li")
print(len(elements))
# for ele in range(len(elements)-3,len(elements)):
#     print(elements[ele].text)
for ele in range(len(elements)-5,len(elements)):
    print(elements[ele].text)





# elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# time.sleep(4)
# print(len(elements))
# print(elements[0].text)
# for ele in elements:
#     print(ele.text)
# # text vs getattributes
# search_box = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# search_box.clear()
# search_box.send_keys("Apple MacBook Pro 13-inch")
# print(search_box.text) # It returns always inner text of search box
# print(search_box.get_attribute('Value')) # It returns always attribute value of the webelement..
time.sleep(5)
