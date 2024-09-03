import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()

def facebook(login_page):
    driver.maximize_window()
    act_title = driver.title
    print(act_title)
    exp_title = "Facebook – log in or sign up"
    assert act_title == exp_title
    print("Title check passed")
    driver.find_element(By.XPATH, "//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Abhaya")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Paikaraya")
    driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys("7606862957")
    driver.find_element(By.ID, "password_step_input").send_keys("erabhaya")
    driver.find_element(By.ID, "day").send_keys("18")
    driver.find_element(By.ID, "month").send_keys("mar")
    driver.find_element(By.ID, "year").send_keys("1999")
    driver.find_element(By.XPATH, "(//input[@name='sex'])[2]").click()
    driver.find_element(By.XPATH, "//button[@name='websubmit']").click()


time.sleep(6)
facebook("login_page")