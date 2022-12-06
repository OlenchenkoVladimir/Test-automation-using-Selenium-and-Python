from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    
    alert = browser.switch_to.alert
    alert.accept()

    getValue = browser.find_element(By.ID, "input_value")
    chrValue = getValue.text
    answer   = calc(chrValue)

    form = browser.find_element(By.ID, "answer")
    form.send_keys(answer)

    submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit.click()
    # alert = browser.switch_to.alert
    # alert_text = alert.text
    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()
finally:
    time.sleep(20)
    browser.quit()