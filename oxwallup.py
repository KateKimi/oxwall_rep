from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from custom_wait_conditions import presence_of_N_elements_located


class Oxwall:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def login_as(self, username, password):
        sign_in_menu = self.driver.find_element_by_class_name('ow_signin_label')
        sign_in_menu.click()
        self.driver.find_element_by_name('identity').clear()
        self.driver.find_element_by_name('identity').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        self.wait.until(expected_conditions.presence_of_element_located((By.NAME, 'status')))


    def create_post(self, text):
        self.driver.find_element_by_name('status').click()
        self.driver.find_element_by_name('status').send_keys(text)
        self.driver.find_element_by_name('save').click()



    def get_posts(self):
        return self.driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")

    def wait_new_post(self, number_amount_of_posts_before):
        self.wait.until(presence_of_N_elements_located((By.CLASS_NAME, "ow_newsfeed_item"),
        number_amount_of_posts_before+1),
        message="Can't find correct count of elements")



    def logout(self):
        pass
