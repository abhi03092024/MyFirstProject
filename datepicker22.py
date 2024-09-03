import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

actual_text="Dragabble"
driver=webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
driver.find_element(By.XPATH,"(//span[@class='lbl_input appendBottom10'])[3]").click()
act_month_year = "June 2025"
time.sleep(5)
while True:
    exp_month_year = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption'])[1]/div").text
    if act_month_year == exp_month_year:
        driver.find_element(By.XPATH,"(//div[@class='dateInnerCell']//p[text()='6'])[1]").click()
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='DayPicker-NavButton DayPicker-NavButton--next']").click()

time.sleep(5)




# driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
# time.sleep(1)
# dropdown_ele=driver.find_element(By.XPATH,"(//span[@class='lbl_input appendBottom10'])[3]")
# dropdown_ele.click()
# time.sleep(5)
# actual_month_year="July 2025"
#
# while True:
#      expected_month_year = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption']/div)[1]").text
#      if expected_month_year == actual_month_year:
#         driver.find_element(By.XPATH, "(//div[@class ='dateInnerCell']/p[text()='10'])[1]").click()
#         break
#      else:
#         driver.find_element(By.XPATH, "//span[@class='DayPicker-NavButton DayPicker-NavButton--next']").click()
#
time.sleep(2)