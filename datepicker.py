import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.webdriver.support.expected_conditions import as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"firstName").send_keys("Abhaya")
driver.find_element(By.ID,"lastName").send_keys("Paikaraya")
driver.find_element(By.ID,"userEmail").send_keys("abhaya1888@gmail.com")
ele1=driver.find_element(By.XPATH,"//div[contains(@class,'custom-control custom-radio')][2]")
driver.execute_script("arguments[0].scrollintoView;",ele1)
time.sleep(1)
rd_button=driver.find_element(By.XPATH,"//label[@for='gender-radio-1']")
time.sleep(1)
rd_button.click()
time.sleep(2)
print(rd_button.is_selected())
if rd_button.is_selected():
    rd_button.click()
time.sleep(4)
driver.find_element(By.ID,"userNumber").send_keys("8397053491")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='react-datepicker__input-container']").click()
month = Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']"))
month.select_by_visible_text("March")
year = Select(driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']"))
year.select_by_visible_text("1999")
date = driver.find_element(By.XPATH,"//div[text()='18']")
date.click()
time.sleep(5)
