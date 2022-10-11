from selene.support.shared import browser

class RadioButton:
    def __init__(self):
        pass
    def select_choice(self, number: int):
        browser.element(f'[for=gender-radio-{number}]').double_click()