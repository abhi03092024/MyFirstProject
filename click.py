import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://letcode.in/test")

driver.maximize_window()
#exp_title=driver.find_element(By.XPATH,"")
act_title = driver.title
print(act_title)
exp_title = "LetCode - Testing Hub"
assert exp_title == act_title
print("The code testing passed")
driver.find_element(By.XPATH,"//a[text()='Edit']").click()
driver.find_element(By.ID,"fullName").send_keys("Abhaya")
driver.find_element(By.ID,"join").send_keys("HELLO")
text1=driver.find_element(By.ID,"getMe")
print(text1.get_attribute("value"))
driver.find_element(By.ID,"clearMe").clear()
enable1=driver.find_element(By.ID,"noEdit").is_enabled()
print(enable1)
driver.find_element(By.ID,"dontwrite")
driver.back()
driver.refresh()
driver.find_element(By.XPATH,"//a[text()='Click']").click()
driver.find_element(By.ID,"home").click()
driver.back()
loc=driver.find_element(By.XPATH,"//button[text()='Find Location']")
print(loc.location)
colour_ele=driver.find_element(By.XPATH,"//button[text()='What is my color?']")
print(colour_ele.get_property("background colour"))
#colour = colour_ele.get_property('background-color')
time.sleep(1)
tex2=driver.find_element(By.ID,"isDisabled").is_enabled()
print(tex2)
prop=driver.find_element(By.ID,"property")                   ######## Doubt
print(prop.get_property("text"))
driver.find_element(By.XPATH,"//h2[text()='Button Hold!']")
driver.back()
driver.find_element(By.XPATH,"//a[text()='Drop-Down']").click()
drp_select=Select(driver.find_element(By.XPATH,"//select[@id='fruits']"))
drp_select.select_by_index(2)
drp_select.select_by_value("4")
drp_select.select_by_visible_text("Apple")
time.sleep(1)
super_heroes = sup_heroes=Select(driver.find_element(By.XPATH,"//select[@id='superheros']"))
sup_heroes.select_by_index(5)
# sup_heroes.select_by_value("aq")
options=super_heroes.options
for option in options:
 print(option.text)
print("selected element")
first_option = sup_heroes.first_selected_option
print(first_option)
driver.back()
time.sleep(1)
# driver.find_element(By.XPATH,"//a[text()='Dialog']").click()
# driver.find_element(By.XPATH,"//button[@id='accept']")
# alert=driver.switch_to.alert
# print(alert.text)
driver.find_element(By.XPATH,"//a[text()='Inner HTML']").click()


time.sleep(4)