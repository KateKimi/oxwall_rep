from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from custom_wait_conditions import presence_of_N_elements_located # ,wait
import time
import pytest


def test_status_create(driver, logged_user, app):
    # wait = WebDriverWait(driver, 5)
    # Wait until login finished
    # x = wait.until(expected_conditions.presence_of_element_located((By.NAME, 'status')))
    old_posts = app.get_posts()
    app.create_post('Cool day!!!!!')
    app.wait_new_post(len(old_posts))

    # status_elements = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    # Input text in Status field
    # driver.find_element_by_name('status').click()
    # driver.find_element_by_name('status').send_keys('How are you?!!!!!')
    # # Post status
    # # TODO wait clickable
    # driver.find_element_by_name('save').click()


    # status_elements = wait.until(presence_of_N_elements_located(
    #     (By.CLASS_NAME, "ow_newsfeed_item"),
    #     len(status_elements)+1),
    #     message="Can't find correct count of elements"
    # )

    # driver.find_element_by_xpath('//a[contains(@id, "nfa-feed")]/input').send_keys(r'E:\workspace\untitled10_selenium\geoline.png')
    # wait.until(expected_conditions.presence_of_element_located
    #                                ((By.CSS_SELECTOR, f'div.ow_console_right [href="{base_url}/user/{username}"]')))
    #

    # TODO: fix Sign out
    # wait.until(
    #     expected_conditions.presence_of_element_located((By.CSS_SELECTOR, f'div.ow_console_right a[href="{base_url}/user/{username}"]')),
    #     message="Can't find User menu"
    # )
    # menu = driver.find_element_by_css_selector('div.ow_console_right a')
    # sign_out = driver.find_element_by_css_selector(f'div.ow_console_right [href="{base_url}/sign-out"]')
    # action = ActionChains(driver)
    # action.move_to_element(menu)
    # action.click(sign_out)
    # action.perform()