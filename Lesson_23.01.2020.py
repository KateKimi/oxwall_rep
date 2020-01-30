"""oxwall"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By #alt + enter автоматически добавляет By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from Try_try import presence_of_N_elements_located

def login(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".ow_signin_label.ow_signin_delimiter")
    element.click()
    return element

def name_field(driver):
    field_name = driver.find_element(By.NAME, "identity")
    field_name.click()
    field_name.clear()
    time.sleep(1)
    field_name.send_keys("demo")
    return field_name
def field_password(driver):
    password_field = driver.find_element(By.NAME, "password")
    password_field.click()
    password_field.clear()
    time.sleep(1)
    password_field.send_keys("demo")
    return password_field
def inside(driver):
    submit_field = driver.find_element(By.NAME, "submit")
    submit_field.click()
    return submit_field


def field_status(driver):
    time.sleep(1)
    status_field = driver.find_element(By.NAME, "status")
    status_field.click()
    status_field.send_keys("Hello!")
    return status_field

def qwtt(driver):
    status_elements = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    print(len(status_elements))
    return status_elements


def post_status(driver):
    post_click = driver.find_element(By.NAME, "save")
    post_click.click()
    return post_click

def log_out():
    el = driver.find_element(By.XPATH, '//*[@href="https://demo.oxwall.com/sign-out"]')
    (webdriver.ActionChains(driver)
        .move_to_element(driver.find_element(By.XPATH, '//*[@href="https://demo.oxwall.com/user/demo"]'))
        .pause(1)
        .click(el)
        .perform()
    )

driver = webdriver.Firefox()
base_url = "https://demo.oxwall.com/"
driver.get(base_url)
wait = WebDriverWait(driver, 5)

logg = wait.until(login, message="No login object")
name = wait.until(name_field, message="No name object")
password = wait.until(field_password, message="No password object")
submit = wait.until(inside, message="No submit object")
status = wait.until(field_status, message="No status object")
qwtt = wait.until(qwtt, message="No objects")
post_post = wait.until(post_status, message="No post object")


# log_out()

