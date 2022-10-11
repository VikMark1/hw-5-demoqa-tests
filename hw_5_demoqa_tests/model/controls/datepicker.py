import datetime
import sys
import selene
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys
from hw_5_demoqa_tests.model.data import user


class DatePicker:
    def __init__(self, element: selene.Element):
        self.element = element
    def select_date(self, date: datetime.date):
        modifier_key = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        self.element.send_keys(
            modifier_key + 'a' + Keys.NULL,
            user.format_input_date(date),
        ).press_enter()
        return self



class DatePicker2:
    def __init__(self, element: selene.Element):
        self.element = element
    def select_date_2(self, ):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('October')
        browser.element('.react-datepicker__year-select').type('1991')
        browser.element('[aria-label="Choose Monday, October 7th, 1991"]').click()
        return self

