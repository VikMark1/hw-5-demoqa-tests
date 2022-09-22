from selene.support.shared import browser


def select_checkbox():
    browser.element('[for="hobbies-checkbox-2"]').click()

