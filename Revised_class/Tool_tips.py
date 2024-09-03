import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(4)
interaction_ele=driver.find_element(By.XPATH,"(//div[@class='card-body'])[4]")
driver.execute_script("arguments[0].scrollIntoView();",interaction_ele)
time.sleep(4)
interaction_ele.click()
driver.find_element(By.XPATH,"//span[text()='Tool Tips']").click()
time.sleep(2)
hover_ele = driver.find_element(By.ID,"toolTipButton")
driver.execute_script("arguments[0].scrollIntoView();",hover_ele)
act=ActionChains(driver)
act.move_to_element(hover_ele).perform()
time.sleep(4)
tool_tip_ele=driver.find_element(By.XPATH,"//div[text()='You hovered over the Button']")
tool_tip_ele_text = tool_tip_ele.text
assert tool_tip_ele_text == "You hovered over the Button"
##Tool_tips-->
#--------------
#When we hover over the mouse to the button element some text appear beside ,We need to capture that text by using
#-->setTimeout(function(){debugger;},5000); #Capture the hover over text
#The above code we need to execute on the console tab
