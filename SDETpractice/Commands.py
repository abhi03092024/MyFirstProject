import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Ie()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
act_title=driver.title  # to check the title of the web page(Going under application commands)
exp_title = "OrangeHRM"
assert act_title == exp_title
if act_title == exp_title:
    print("title got tpassed")
print(act_title)
url = driver.current_url # to check the current url(Going under application commands)
print(url)
page_source = driver.page_source # to check the page source(Going under application commands)
print(page_source)
time.sleep(2)
search_box=driver.find_element(By.NAME,"username")
#Conditional commands
#is_displayed()
#is_enabled()
#is_selected()
print(search_box.is_displayed())  # To check the searchbox displayed or not
search_box.send_keys("Admin")
print(search_box.is_enabled())   # To check the serchbox enabled or not
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(@class,'oxd-button oxd-button--medium')]").click()
# rad_button=driver.find_element(By.XPATH,"//input[@value='1']")
# rad_button.is_selected()
time.sleep(3)
#Browsercommands
driver.close() #To close the current browser on the web page
driver.quit() #To close all the browser on the web page
time.sleep(6)
