from selenium import webdriver
import time
from auth_data import ya_username, ya_password


def ya_authorization(username, password):
    url = 'https://passport.yandex.ru/auth/'
    driver = webdriver.Chrome(executable_path=r'D:\Py3\netology\py_54\PY_ADVANCED\Task_6\chromedriver\chromedriver.exe')

    try:
        driver.get(url=url)
        time.sleep(2)

        id_input = driver.find_element_by_name('login')
        id_input.clear()
        id_input.send_keys(username)
        time.sleep(4)

        login_button = driver.find_element_by_id('passp:sign-in').click()
        time.sleep(3)

        password_input = driver.find_element_by_id('passp-field-passwd')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(3)

        login_button = driver.find_element_by_id('passp:sign-in').click()
        time.sleep(5)

        test_button =driver.find_element_by_class_name('PageNavigation-linkTitle').click()
        time.sleep(2)

        return f'Авторизация для {username} прошла успешно!'

    except Exception as ex:
        return 'Ошибка авторизации'

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    print(ya_authorization(ya_username, ya_password))