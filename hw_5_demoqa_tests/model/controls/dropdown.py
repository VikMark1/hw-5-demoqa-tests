from selene import have
from selene.support.shared import browser


class Dropdown:
    def __init__(self):
        pass
    def select(self, element, option):
        element.click()
        browser.all('[id^=react-select][id*=-option-]').by(
            have.exact_text(option)
        ).first.click()