from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    #What is ln(abs(12*sin(x))), where x = 531?
try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()
    
    radiobutton_robot = browser.find_element(By.ID, "robotsRule")
    radiobutton_robot.click()
    
    sub = browser.find_element(By.CLASS_NAME, "btn-default")
    sub.click()
finally:
    time.sleep(10)
    browser.quit()