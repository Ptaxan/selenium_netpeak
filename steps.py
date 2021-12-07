from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import random
import string


def random_text():
    letters_and_digits = string.ascii_letters + string.digits
    lenght = random.randint(0, 100)
    rand_string = ''.join(random.choice(letters_and_digits) for i in range(lenght))
    return rand_string


s = Service('f:\\Coding\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://netpeak.ua/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

aboutXpath = "//li[contains(text(),'нас')]"
teamXpath = "//nav//a[text()='Команда']"
beTeamXpath = "//a[contains(text(),'Стать')]"
lkXpath = "//nav//a[contains(text(),'Личный кабинет')]"

driver.find_element(By.XPATH, aboutXpath).click()
wait.until(EC.visibility_of_element_located((By.XPATH, teamXpath))).click()
wait.until(EC.presence_of_element_located((By.XPATH, beTeamXpath))).click()
driver.switch_to.window(driver.window_handles[1])

assert "Работа в Netpeak" in driver.page_source

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, lkXpath).click()

driver.switch_to.window(driver.window_handles[2])

loginXpath = '//*[@id="login"]'
passwordXpath = '//*[@id="password"]'

loginText = random_text()
passwordText = random_text()

login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, loginXpath)))
login.send_keys(loginText)

password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, passwordXpath)))
password.send_keys(passwordText)

checkBox = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]/div/md-checkbox').click()
pressLogin = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[5]/button').click()

loginElement = driver.find_element(By.XPATH, '//*[@id="login"]')

print(loginElement.value_of_css_property('border-bottom-color') == 'rgb(221, 44, 0)')
