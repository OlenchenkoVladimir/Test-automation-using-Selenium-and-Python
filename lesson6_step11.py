from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"
link13 = "http://suninjuly.github.io/find_link_text_redirect13.html"
link7  = "http://suninjuly.github.io/huge_form.html"
link8  = "http://suninjuly.github.io/find_xpath_form"
link10 = "http://suninjuly.github.io/registration1.html"
link11 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link11)

    input1 = browser.find_element(By.CLASS_NAME, "first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, "second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("ku@box.com")
    input4 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your phone:"]')
    input4.send_keys("+79995557788")
    input5 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your address:"]')
    input5.send_keys("СНТ Энергетик")
# Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()