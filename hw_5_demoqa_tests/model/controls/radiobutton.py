from selene.support.shared import browser


def select_choice():
    browser.element('[for=gender-radio-2]').double_click()