from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


link1    = "http://suninjuly.github.io/selects1.html"
link2    = "http://suninjuly.github.io/selects2.html"

def calc(x1 : str, x2 : str) -> str:
    return str(int(x1) + int(x2))

try:
    browser = webdriver.Chrome()
    #browser.get(link1)
    browser.get(link2)
    x1_element = browser.find_element(By.ID, "num1")
    x1         = x1_element.text
    x2_element = browser.find_element(By.ID, "num2")
    x2         = x2_element.text
    answer : str = calc(x1, x2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(answer) # ищем элемент с текстом "Python"
    submit = browser.find_element(By.CLASS_NAME, "btn-default" )
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
#Второй способ ищет элемент по его индексу или порядковому номеру. 
#Индексация начинается с нуля. Для того чтобы найти элемент с текстом "Python",
#нужно использовать
#select.select_by_index(1)