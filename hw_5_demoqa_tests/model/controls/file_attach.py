from selene.support.shared import browser
import os


def add_pict(relative_path):
    browser.element('#uploadPicture').send_keys(os.path.abspath(relative_path))