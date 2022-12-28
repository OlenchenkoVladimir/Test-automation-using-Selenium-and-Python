from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    exercism = "http://suninjuly.github.io/explicit_wait2.html"
    #browser.get("http://suninjuly.github.io/wait2.html")
    browser.get(exercism)

    # говорим Selenium проверять в течении 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"),"100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    solve = browser.find_element(By.ID, "solve")
    solve.click()
finally:
    time.sleep(20)
    browser.quit()