import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()
#tagname & value of id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abhaya1888@gmail.com") #1st Tagname#value of id

#tagname & value of class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext _55r1 _6luy").send_keys("abc@gmail.com")

#tagname & attribute
#driver.find_element(By.CSS_SELECTOR,"input[placeholder='Email or phone number']").send_keys("abc@gmail.com")

#tagname,valueofclassname & [attribute=value]
#driver.find_element(By.CSS_SELECTOR,"input.inputtext _55r1 _6luy[placeholder='Email or phone number']")
#last 3 css selectors are not working
time.sleep(5)