from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

""" В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit" """
link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Claus")
    family = browser.find_element(By.NAME, "lastname")
    family.send_keys("Boss")
    postman = browser.find_element(By.NAME, "email")
    postman.send_keys("kuku@info.org")
    path_dir = os.path.abspath(os.path.dirname(__file__))
    path_file = os.path.join(path_dir, 'file.txt')
    button_file = browser.find_element(By.ID, "file")
    button_file.send_keys(path_file)

    submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()