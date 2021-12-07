import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import string


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def random_text():
    letters_and_digits = string.ascii_letters + string.digits
    lenght = random.randint(0, 100)
    rand_string = ''.join(random.choice(letters_and_digits) for i in range(lenght))
    return rand_string


def test_work_in_netpeak_page(browser):
    """Убедится, что в новой вкладке открылась страница Работа в Нетпик"""
    URL = "https://netpeak.ua/"
    PHRASE = "Работа в Нетпик"
    aboutXpath = "//li[contains(text(),'нас')]"
    teamXpath = "//nav//a[text()='Команда']"
    beTeamXpath = "//a[contains(text(),'Стать')]"

    browser.get(URL)
    browser.maximize_window()

    browser.find_element(By.XPATH, aboutXpath).click()
    browser.find_element(By.XPATH, teamXpath).click()
    browser.find_element(By.XPATH, beTeamXpath).click()
    browser.switch_to.window(browser.window_handles[1])

    assert PHRASE in browser.page_source


def test_i_want_work_clickable(browser):
    """Убедится, что на странице есть кнопка "Я хочу работать в Netpeak" и на нее можно кликнуть"""
    URL = "https://netpeak.ua/"
    PHRASE = "Я хочу работать в Netpeak"
    aboutXpath = "//li[contains(text(),'нас')]"
    teamXpath = "//nav//a[text()='Команда']"
    beTeamXpath = "//a[contains(text(),'Стать')]"
    wantTeamXpath = "/html/body/div[5]/div/div/div[2]/div/a"

    browser.get(URL)
    browser.maximize_window()

    browser.find_element(By.XPATH, aboutXpath).click()
    browser.find_element(By.XPATH, teamXpath).click()
    browser.find_element(By.XPATH, beTeamXpath).click()
    browser.switch_to.window(browser.window_handles[1])

    button = browser.find_element(By.XPATH, wantTeamXpath)
    href_data = button.get_attribute('href')

    assert PHRASE in browser.page_source and href_data is not None


def test_login_not_available(browser):
    """Проверить, что кнопка "Войти" не доступна"""
    URL = "https://netpeak.ua/"
    aboutXpath = "//li[contains(text(),'нас')]"
    teamXpath = "//nav//a[text()='Команда']"
    beTeamXpath = "//a[contains(text(),'Стать')]"
    lkXpath = "//nav//a[contains(text(),'Личный кабинет')]"
    loginXpath = '//*[@id="login"]'
    passwordXpath = '//*[@id="password"]'
    buttonXpath = '//*[@id="loginForm"]/div[5]/button'
    loginText = random_text()
    passwordText = random_text()

    browser.get(URL)
    browser.maximize_window()

    browser.find_element(By.XPATH, aboutXpath).click()
    browser.find_element(By.XPATH, teamXpath).click()
    browser.find_element(By.XPATH, beTeamXpath).click()
    browser.switch_to.window(browser.window_handles[1])

    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.XPATH, lkXpath).click()

    browser.switch_to.window(browser.window_handles[2])

    login = browser.find_element(By.XPATH, loginXpath)
    login.send_keys(loginText)

    password = browser.find_element(By.XPATH, passwordXpath)
    password.send_keys(passwordText)

    button = browser.find_element(By.XPATH, buttonXpath)
    disable = button.get_attribute('disabled')

    assert disable


def test_notification_invalid_login_password(browser):
    """Наличие нотификации о неправильном логине или пароле"""
    URL = "https://netpeak.ua/"
    aboutXpath = "//li[contains(text(),'нас')]"
    teamXpath = "//nav//a[text()='Команда']"
    beTeamXpath = "//a[contains(text(),'Стать')]"
    lkXpath = "//nav//a[contains(text(),'Личный кабинет')]"
    loginXpath = '//*[@id="login"]'
    passwordXpath = '//*[@id="password"]'
    buttonXpath = '//*[@id="loginForm"]/div[5]/button'
    loginText = random_text()
    passwordText = random_text()
    checkboxXpath = '//*[@id="loginForm"]/div[4]/div/md-checkbox'

    browser.get(URL)
    browser.maximize_window()

    browser.find_element(By.XPATH, aboutXpath).click()
    browser.find_element(By.XPATH, teamXpath).click()
    browser.find_element(By.XPATH, beTeamXpath).click()
    browser.switch_to.window(browser.window_handles[1])

    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.XPATH, lkXpath).click()

    browser.switch_to.window(browser.window_handles[2])

    login = browser.find_element(By.XPATH, loginXpath)
    login.send_keys(loginText)

    password = browser.find_element(By.XPATH, passwordXpath)
    password.send_keys(passwordText)

    browser.find_element(By.XPATH, checkboxXpath).click()
    browser.find_element(By.XPATH, buttonXpath).click()

    message = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body'), 'Неправильный логин или пароль'))

    assert message


def test_red_login_password(browser):
    """Проверить что Логин и Пароль подсветились красным цветом"""
    URL = "https://netpeak.ua/"
    aboutXpath = "//li[contains(text(),'нас')]"
    teamXpath = "//nav//a[text()='Команда']"
    beTeamXpath = "//a[contains(text(),'Стать')]"
    lkXpath = "//nav//a[contains(text(),'Личный кабинет')]"
    loginXpath = '//*[@id="login"]'
    passwordXpath = '//*[@id="password"]'
    buttonXpath = '//*[@id="loginForm"]/div[5]/button'
    loginText = random_text()
    passwordText = random_text()
    checkboxXpath = '//*[@id="loginForm"]/div[4]/div/md-checkbox'

    browser.get(URL)
    browser.maximize_window()

    browser.find_element(By.XPATH, aboutXpath).click()
    browser.find_element(By.XPATH, teamXpath).click()
    browser.find_element(By.XPATH, beTeamXpath).click()
    browser.switch_to.window(browser.window_handles[1])

    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.XPATH, lkXpath).click()

    browser.switch_to.window(browser.window_handles[2])

    login = browser.find_element(By.XPATH, loginXpath)
    login.send_keys(loginText)

    password = browser.find_element(By.XPATH, passwordXpath)
    password.send_keys(passwordText)

    browser.find_element(By.XPATH, checkboxXpath).click()
    browser.find_element(By.XPATH, buttonXpath).click()

    loginFrame = browser.find_element(By.XPATH, loginXpath)
    passwordFrame = browser.find_element(By.XPATH, passwordXpath)

    loginFrameColor = loginFrame.value_of_css_property('border-bottom-color')
    passwordFrameColor = passwordFrame.value_of_css_property('border-bottom-color')

    assert loginFrameColor == passwordFrameColor == 'rgba(221, 44, 0, 1)'
