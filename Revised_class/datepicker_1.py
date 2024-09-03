import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

actual_text="Dragabble"
driver=webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()
time.sleep(1)
dropdown_ele=driver.find_element(By.XPATH,"(//span[@class='lbl_input appendBottom10'])[3]")
dropdown_ele.click()
actual_month_year="July 2025"

while True:
    expected_month_year = driver.find_element(By.XPATH, "(//div[@class='DayPicker-Caption']/div)[1]").text
    if expected_month_year == actual_month_year :
        driver.find_element(By.XPATH, "(//div[@class ='dateInnerCell']/p[text()='2'])[1]").click()
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='DayPicker-NavButton DayPicker-NavButton--next']").click()
