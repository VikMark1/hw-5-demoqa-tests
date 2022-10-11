from typing import Tuple
from selene import have, command, by
from selene.support.shared import browser
from hw_5_demoqa_tests.model.controls.datepicker import DatePicker
from hw_5_demoqa_tests.model.controls.dropdown import Dropdown
from hw_5_demoqa_tests.model.controls.file_attach import FileAttach
from hw_5_demoqa_tests.model.controls.radiobutton import RadioButton
from hw_5_demoqa_tests.model.data import user
import datetime
from hw_5_demoqa_tests.model.data.user import Subject, Hobby, student


class RegistrationForm:
    def __init__(self):
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))
    def setup_ready(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads][id$=container__]')
        if ads.wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self
    def fill_firstname(self, firstname: str):
        browser.element('#firstName').send_keys(firstname)
        return self
    def fill_lastname(self, lastname: str):
        browser.element('#lastName').send_keys(lastname)
        return self
    def fill_email(self, email: str):
        browser.element('#userEmail').send_keys(email)
        return self
    def fill_mobile(self, mobile: str):
        browser.element('#userNumber').send_keys(mobile)
        return self
    def fill_subjects(self, values: Tuple[Subject]):
        for subject in values:
            browser.element('#subjectsInput').send_keys(subject.value).press_enter()
        return self
    def fill_address(self, address):
        browser.element('#currentAddress').send_keys(address)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#submit').perform(command.js.scroll_into_view)
        return self
    def set_state(self, value: str):
        Dropdown.select(self, browser.element('#state'), value)
        return self
    def set_city(self, value: str):
        Dropdown.select(self, browser.element('#city'), value)
        return self
    def submit_form(self, ):
        browser.element('#submit').press_enter()
        return self
    def should_have_submitted(self, data):
        dialog = browser.element('.modal-content')
        rows = dialog.all('tbody tr')
        for row, value in data:
            rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
        return self
    def fill_gender(self, value: user.Gender):
        RadioButton.select_choice(self, value.value) #noqa
        return self
    def fill_birth_date(self, date: datetime.date):
        self.birthday.select_date(date)
        return self
    def fill_hobbies(self, values: Tuple[Hobby]):
        for hobby in values:
            path = "//label[contains(.,'" + str(hobby.value) + "')]"
            browser.element(by.xpath(path)).click()
        return self
    def select_picture(self, relative_path):
        FileAttach.add_pict(self, relative_path)
        return self


class SubmitForm:
    def __init__(self):
        self.registration_form = RegistrationForm()

    def submit(self):
        (
            self.registration_form.setup_ready()

            .fill_firstname(student.firstname)
            .fill_lastname(student.lastname)
            .fill_email(student.email)
            .fill_gender(student.gender)
            .fill_mobile(student.mobile)
            .fill_birth_date(student.birth_date)
            .fill_subjects(student.subjects)
            .fill_hobbies(student.hobbies)
            .select_picture(student.picture)
            .fill_address(student.address)
            .set_state(student.state)
            .set_city(student.city)
            .submit_form()

            .should_have_submitted(
                [
                    ('Student Name', f'{student.firstname} {student.lastname}'),
                    ('Student Email', student.email),
                    ('Gender', 'Female'),
                    ('Mobile', student.mobile),
                    ('Date of Birth', '07 October,2001'),
                    ('Subjects', 'English, Maths'),
                    ('Hobbies', 'Music, Reading'),
                    ('Picture', 'test.png'),
                    ('Address', student.address),
                    ('State and City', f'{student.state} {student.city}'),
                ],
            )
        )