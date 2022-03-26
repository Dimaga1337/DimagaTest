import calc
from selenium import webdriver
import time
import math


from selenium.webdriver.common.by import By

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)

    options1 = browser.find_element(By.ID, 'robotCheckbox')
    options1.click()

    options2 = browser.find_element(By.ID, 'robotsRule')
    options2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
