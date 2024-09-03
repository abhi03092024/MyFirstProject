import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.agoda.com/en-in/?site_id=&ds=yvTdpJ%2FkV9bxtcPm")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"(//i[@data-selenium='ficon-icon-box'])[2]").click()
act_mon_year = "November 2024"
time.sleep(3)
# exp_mon_year = driver.find_element(By.XPATH,"(//div[@role='heading'])[1]").text

while True:
    exp_mon_year = driver.find_element(By.XPATH, "(//div[@role='heading'])[1]").text
    if act_mon_year == exp_mon_year:
        driver.find_element(By.XPATH,"//span[@data-selenium-date='2024-11-20']").click()
        break
    else:
        driver.find_element(By.XPATH,"//button[@aria-label='Next Month']").click()
        time.sleep(5)