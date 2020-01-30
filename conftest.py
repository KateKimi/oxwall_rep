import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from oxwallup import Oxwall


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    base_url = 'https://demo.oxwall.com/'
    driver.get(base_url)
    yield driver
    driver.quit()



@pytest.fixture()
def app(driver):
    return Oxwall(driver)

@pytest.fixture()
def logged_user(app):
    username = "demo"
    # app = Oxwall(driver)
    app.login_as(username, "demo")
    # username = 'demo'
    # sign_in_menu = driver.find_element_by_class_name('ow_signin_label')
    # sign_in_menu.click()
    # driver.find_element_by_name('identity').clear()
    # driver.find_element_by_name('identity').send_keys(username)
    # driver.find_element_by_name('password').clear()
    # password_field = driver.find_element_by_name('password')
    # password_field.send_keys('demo')
    # password_field.send_keys(Keys.ENTER)
    yield username
    app.logout()