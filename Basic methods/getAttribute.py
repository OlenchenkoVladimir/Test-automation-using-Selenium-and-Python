from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link =         "http://suninjuly.github.io/math.html"
linkExercism = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, 
# как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", 
# точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

# Ваша программа должна:

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".
# Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

 

# Если все сделано правильно и достаточно быстро 
# (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
# Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
try:
    browser  = webdriver.Chrome()
    browser.get(linkExercism) #17
    
    imgTorba = browser.find_element(By.ID,"treasure")#18
    x        = imgTorba.get_attribute("valuex")#19x = x_element.text
    
    answer   = calc(x)
    fieldAns = browser.find_element(By.ID,"answer")#21
    fieldAns.send_keys(answer)
    
    robot    = browser.find_element(By.ID,"robotCheckbox")
    robot.click()
    rule     = browser.find_element(By.ID,"robotsRule")
    rule.click()
    submit   = browser.find_element(By.CLASS_NAME,"btn-default")
    submit.click()
    
    
    #browser.get(link)
    
    # people_radio = browser.find_element(By.ID, "peopleRule")
    # people_cheked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_cheked)
    # assert people_cheked is not None, "People radio is not selected by default"
    # robots_radio = browser.find_element(By.ID, "robotsRule")
    # robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None, "Robot radio is not selected by default"
finally:
    time.sleep(10)
    browser.quit()