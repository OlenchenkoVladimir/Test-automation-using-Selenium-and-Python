from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд (Implicit Waits)
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")
    #browser.get("http://suninjuly.github.io/cats.html")

    #time.sleep(1)

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    #button = browser.find_element(By.ID, "button")
finally:
    time.sleep(5)
    browser.quit()