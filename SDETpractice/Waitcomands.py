import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
# driver.implicitly_wait(10)
# search_box=driver.find_element(By.ID,"APjFqb")
# search_box.send_keys("Selenium")
# search_box.submit()
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
#Some times the application takes time to get the element in that case we use wait statements to avoid synchronization problem..
#Its a global wait & it works based on the time
#We can use implicit wait for all the element on the webpage
#It waits till the given time before throwing no such element exception
#If it unable to loacte the element then it will return no such exception
search_box=driver.find_element(By.ID,"APjFqb")
search_box.send_keys("Selenium")
search_box.submit()
search_link=driver.find_element(By.XPATH,"//h3[text()='Selenium']")
my_wait = WebDriverWait(driver,10)
my_wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search_link.click()
time.sleep(4)
#We use explicit wait for a signle webelement,Where the condition satisfying
#If the condition is satisfying then the code will execute
#If the element didn't find within given time then it will ignore that script & execute rest of element
driver.quit()