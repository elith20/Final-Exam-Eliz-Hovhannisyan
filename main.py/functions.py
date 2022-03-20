import time

from xpath import Xpath
from signup import user1, user2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.phptravels.net/signup')
parent_window = driver.current_window_handle


def click(locator):
    """ The function clicks on the given button. """
    button = driver.find_element(By.XPATH, locator)
    return button.click()


def send_keys(locator, value):
    """ The function input the given value the given area."""
    return driver.find_element(By.XPATH, locator).send_keys(value)


def signup():
    """The function Signs Up the page with given requisites"""
    send_keys(Xpath.first_name, user2.first_name)
    send_keys(Xpath.last_name, user2.last_name)
    send_keys(Xpath.phone, user2.phone)
    send_keys(Xpath.email, user2.email)
    send_keys(Xpath.password, user2.password)
    driver.find_element(By.XPATH, Xpath.password).send_keys(Keys.ENTER)


def login():
    """The function Logins an account."""
    send_keys(Xpath.login, user2.login())
    send_keys(Xpath.acc_password, user2.acc_password())
    driver.find_element(By.XPATH, Xpath.acc_password).send_keys(Keys.ENTER)


def choose_hotel():
    """The function choses 'Hotels' from menu. """
    return click(Xpath.hotels)


def search_from_hotels():
    """ The function searches hotel in 'Yerevan'"""
    driver.find_element(By.CLASS_NAME, 'select2-selection__rendered').click()
    send_keys(Xpath.city_name_to_input, 'Yerevan')
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, 'select2-results__option').click()
    click(Xpath.search_button)


def choose_details():
    """The function chooses hotel details."""
    click(Xpath.details)


def select_room():
    """The function selects rooms in hotel. """
    click(Xpath.select_room)


def reserve():
    """The function clicks on reserve button. """
    driver.find_element(By.CLASS_NAME, 'ChildRoomsList-bookButtonInput').click()


def fill_in_reservation():
    """The function fills in requisites for booking hotel room. """
    send_keys(Xpath.full_name, user2.first_name + ' ' + user2.last_name)
    send_keys(Xpath.reserve_email, user2.email)
    send_keys(Xpath.retype_email, user2.email)
    send_keys(Xpath.phone_number, user2.phone)
    click(Xpath.non_smoking)
    click(Xpath.large_bed)


def final_step():
    click(Xpath.next_final_step)


def actions():

    global parent_window
    signup()
    WebDriverWait(driver, 10).until(
        EC.url_changes('https://www.phptravels.net/signup')
    )
    login()

    driver.implicitly_wait(10)
    choose_hotel()
    driver.implicitly_wait(10)
    search_from_hotels()

    WebDriverWait(driver, 10).until(
        EC.title_is('Hotels in yerevan - PHPTRAVELS')
    )
    choose_details()
    child_window = driver.window_handles
    sec_win = child_window[1]
    driver.switch_to.window(parent_window)
    driver.switch_to.window(sec_win)

    parent_window = driver.current_window_handle

    select_room()
    driver.implicitly_wait(15)
    child_window = driver.window_handles
    third_win = child_window[2]
    driver.switch_to.window(third_win)
    reserve()
    driver.implicitly_wait(10)
    fill_in_reservation()
    driver.implicitly_wait(10)
    final_step()
    current_url = driver.current_url
    return current_url




