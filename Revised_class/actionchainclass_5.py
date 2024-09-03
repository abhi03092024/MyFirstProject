import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


actual_text="Dragabble"
driver=webdriver.Chrome()
driver.get("https://demoqa.com/dragabble")
driver.maximize_window()
time.sleep(4)


# interaction_ele=driver.find_element(By.XPATH,"(//div[@class='card-body'])[5]")
# driver.execute_script("arguments[0].scrollIntoView();",interaction_ele)
# time.sleep(4)
# interaction_ele.click()

#driver.find_element(By.XPATH,"//li[@class='btn btn-light ']/*[name()='svg']/following-sibling::span[text()='Dragabble']").click()
selectable_txt = driver.find_element(By.XPATH,"//h1[@class='text-center']").text
print(selectable_txt)
assert selectable_txt == actual_text

drag_box = driver.find_element(By.ID,"dragBox")
driver.execute_script("arguments[0].scrollIntoView();",drag_box)
act = ActionChains(driver)
time.sleep(5)
act.drag_and_drop_by_offset(drag_box,400,0).perform()
time.sleep(5)
