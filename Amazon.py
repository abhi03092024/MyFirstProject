import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(2)
ele=driver.find_element(By.XPATH,"//a[@class='a-link-normal']//img[contains(@alt,'KLOSIA Women Printed Flared A-Line')]")
time.sleep(3)
driver.execute_script("arguments.scrollIntoView;",ele)
time.sleep(4)
ele.click()
driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']").click()
driver.find_element(By.XPATH,"//a[@data-csa-c-content-id='sw-gtc_CONTENT']").click()


time.sleep(6)