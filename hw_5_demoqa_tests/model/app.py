from selene import have, command
from selene.support.shared import browser


def setup_ready():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id$=container__]')
    if ads.wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)

#browser.execute_script(document.querySelectorAll('[id^=google_ads][id$=container__]').forEach (element => element.remove())