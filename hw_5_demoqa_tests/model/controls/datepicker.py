from selenium.webdriver.common.keys import Keys
from selene.support.shared import browser


def select_date(date: str):
    browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND + 'a').type(date).press_enter()


def select_date_2():
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1991')
    browser.element('[aria-label="Choose Monday, October 7th, 1991"]').click()