from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
from settings import login_url, valid_phone_number, valid_password, valid_email, valid_account_number, invalid_password, \
    invalid_email, empty_email, empty_password, name, surname, new_email, lesser_password, bigger_password, \
    cyrillic_password, no_caps_password, no_numbers_password, empty_phone_number, valid_login
import time

'''1.Авторизация клиента по номеру телефона'''


def test_phone_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email


'''2.Авторизация клиента по email'''


def test_email_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email


'''3.Авторизация клиента по логину'''


def test_login_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-login"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_login)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email


'''4.Авторизация клиента по лицевому счету'''


def test_account_number_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-ls"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(
        valid_account_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email


'''5.Авторизация через почту с валидным email и невалидным паролем'''


def test_valid_email_invalid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(invalid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


'''6.Авторизация через почту с невалидным email и валидным паролем'''


def test_invalid_email_valid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


'''7.Авторизация через почту с невалидной email и невалидным паролем'''


def test_invalid_email_invalid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(invalid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


'''8.Авторизация через email с пустыми полями почта и пароль'''


def test_empty_email_empty_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(empty_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


'''9.Регистрация нового пользователя с паролем меньше 8 символов (7 символов)'''


def test_lesser_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(lesser_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        lesser_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов'


'''10.Регистрация нового пользователя с паролем больше 20 символов (21 символов)'''


def test_bigger_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(bigger_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        bigger_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не более 20 символов'


'''11.Регистрация нового пользователя с паролем из кириллических символов'''


def test_cyrillic_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(cyrillic_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        cyrillic_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать только латинские буквы'


'''12.Регистрация нового пользователя с паролем без единой заглавной буквы '''


def test_no_caps_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_caps_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        no_caps_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы одну заглавную букву'


'''13.Регистрация нового пользователя с паролем без единой цифры или спецсимвола'''


def test_no_numbers_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_numbers_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        no_numbers_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'


'''14.  Авторизация клиента по номеру телефона, раздел "Телефон" с пустым полем Мобильный телефон'''


def test_empty_phone_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите номер телефона'


'''15.  Авторизация клиента по почте, раздел "Почта" с пустым полем Электронная почта'''


def test_empty_email_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите адрес, указанный при регистрации'
    
driver.close()
