import time

from selenium import webdriver

from selenium.webdriver.common.by import By

url="https://www.facebook.com/"
title="Facebook – log in or sign up"
act_text="The email address or mobile number you entered isn't connected to an account. Find your account and log in."

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)


expected_url = driver.current_url
assert url == expected_url   #To check the URL


expected_title = driver.title
assert title == expected_title  #To check the title of the page

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("8397053491")
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("dusmatna12364")
driver.find_element(By.XPATH,"//button[contains(@id,'u_0_5')]").click()
time.sleep(4)
expected_text = driver.find_element(By.XPATH,"//div[@class='_9ay7']").text
print(expected_text)
assert act_text == expected_text  #To check the text

time.sleep(5)
#driver.close()
