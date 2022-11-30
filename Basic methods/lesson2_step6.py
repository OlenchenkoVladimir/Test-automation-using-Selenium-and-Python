""" Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов 
и справиться с ужасным и огромным футером, который дизайнер всё 
никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Если все сделано правильно и достаточно быстро 
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script, 
чтобы сделать прокрутку в область видимости элементов, перекрытых футером. """


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link1    = "http://SunInJuly.github.io/execute_script.html"

def calc(x1 : str) -> str:
    return str(math.log(abs(12*math.sin(int(x1)))))

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    x1_element = browser.find_element(By.ID, "input_value")
    x1         = x1_element.text
    answer : str = calc(x1)

    input1 = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(answer)

    check_robot = browser.find_element(By.ID, "robotCheckbox")
    check_robot.click()
    
    radiobutton_robot = browser.find_element(By.ID, "robotsRule")
    radiobutton_robot.click()
    
    submit = browser.find_element(By.CLASS_NAME, "btn-primary" )
    submit.click()
finally:
    time.sleep(10)
    browser.quit()