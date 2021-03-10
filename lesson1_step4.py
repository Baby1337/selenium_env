import time
from math import log, sin
from selenium import webdriver


def calc(x):
	#Функция для подсчета всеми нами любмой функции(сори за тавтологию)
    return str(log(abs(12*sin(int(x)))))


try:

    driver = webdriver.Chrome()

    driver.get('http://suninjuly.github.io/math.html')
    time.sleep(5)

    x_element = driver.find_element_by_id("input_value")
    x_element = x_element.text
    answer_field = driver.find_element_by_id("answer")
    answer_field.send_keys(calc(int(x_element)))

    rob_check = driver.find_element_by_tag_name("[type='checkbox']")
    rob_check.click()

    rob_cool_check = driver.find_element_by_id("robotsRule")
    rob_cool_check.click()

    submit_button = driver.find_element_by_tag_name('[type="submit"]')
    submit_button.click()
finally:
    time.sleep(20)
    driver.quit()

