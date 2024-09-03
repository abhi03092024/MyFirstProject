import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import  Select

actual_text="Dragabble"
driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(4)
interaction_ele=driver.find_element(By.XPATH,"(//div[@class='card-body'])[4]")
driver.execute_script("arguments[0].scrollIntoView();",interaction_ele)
time.sleep(4)
interaction_ele.click()
driver.find_element(By.XPATH,"//span[text()='Date Picker']").click()
driver.find_element(By.ID,"datePickerMonthYearInput").click()
time.sleep(4)
month_dropdown = driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']")
select_month = Select(month_dropdown)
select_month.select_by_visible_text("September")

year_dropdown = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
select_year = Select(year_dropdown)
select_year.select_by_visible_text("2028")

date = driver.find_element(By.XPATH,"//div[text()='24']")
driver.execute_script("arguments[0].scrollIntoView();",date)
date.click()
time.sleep(3)