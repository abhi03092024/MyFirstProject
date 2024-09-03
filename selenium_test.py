import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)


act_login_page_txt= driver.find_element(By.XPATH,"//div[text()='Swag Labs']").text
exp_login_page_txt = "Swag Labs"
assert act_login_page_txt == exp_login_page_txt
print("Login page check passed")

user_name = driver.find_element(By.XPATH,"//input[@id='user-name']")
user_name.send_keys("standard_user")
user_password = driver.find_element(By.XPATH,"//input[@id='password']")
user_password.send_keys("secret_sauce")
time.sleep(2)
act_title = 'Swag Labs'
exp_title = driver.title
assert act_title == exp_title
print("The title check passed")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
act_product_page = driver.find_element(By.XPATH,"//span[text()='Products']").text
exp_product_page = "Products"
assert act_product_page == exp_product_page
print("We are in right product page")

time.sleep(2)
dropdown = Select(driver.find_element(By.XPATH,"//select[@class='product_sort_container']"))
dropdown.select_by_visible_text("Price (high to low)")
time.sleep(1)
act_product_txt = driver.find_element(By.XPATH,"//div[text()='Sauce Labs Fleece Jacket']").text
driver.find_element(By.XPATH,"//button[text()='Add to cart']").click()
driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']").click()
exp_product_txt = "Sauce Labs Fleece Jacket"
assert act_product_txt == exp_product_txt
print("The product text matchimng")
act_product_price = driver.find_element(By.XPATH,"(//div[@class='inventory_item_price'])[1]").text
item_value = act_product_price.replace("$","")
act_cart_txt = driver.find_element(By.XPATH,"//span[text()='Your Cart']").text
exp_cart_txt = "Your Cart"
assert act_cart_txt == exp_cart_txt
print("We are in the add to cart page")
driver.find_element(By.XPATH,"//button[text()='Checkout']").click()
time.sleep(2)
act_information_page = driver.find_element(By.XPATH,"//span[text()='Checkout: Your Information']").text
exp_information_page = "Checkout: Your Information"
assert act_information_page == exp_information_page
print("We landed on the informatiion page")
driver.find_element(By.ID,"first-name").send_keys("Abhaya")
driver.find_element(By.ID,"last-name").send_keys("Kumar")
driver.find_element(By.ID,"postal-code").send_keys("12345")
driver.find_element(By.ID,"continue").click()
time.sleep(1)
act_view_page = driver.find_element(By.XPATH,"//span[text()='Checkout: Overview']")
exp_view_page = "Checkout: Overview"
print("We succesfully landed on view page")
tax_price = driver.find_element(By.XPATH,"//div[@class='summary_tax_label']").text
tax_value = tax_price.replace("Tax: $","")
print(tax_value)
item_price = driver.find_element(By.XPATH,"//div[@class='summary_subtotal_label']").text
item_value = item_price.replace("Item total: $","")
print(item_value)
total_product_price = driver.find_element(By.XPATH,"//div[@class='summary_total_label']").text
total_value_of_product = total_product_price.replace("Total: $","")
total_value = float(total_value_of_product)
exp_value = float(tax_value) + float(item_value)
print(exp_value)
assert total_value == exp_value
print("The value of product is matching")
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Finish']").click()
act_finish_page = driver.find_element(By.XPATH,"//h2[text()='Thank you for your order!']").text
exp_finish_page = "Thank you for your order!"
assert act_finish_page == exp_finish_page
print("The order is completed")
time.sleep(6)