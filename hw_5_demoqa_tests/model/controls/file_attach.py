from selene.support.shared import browser
import os

class FileAttach:
    def __init__(self):
        pass
    def add_pict(self, relative_path):
        browser.element('#uploadPicture').send_keys(os.path.abspath(relative_path))