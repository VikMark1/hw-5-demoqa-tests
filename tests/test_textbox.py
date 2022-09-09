import os
from selene import be, command, have
from selene.support.shared import browser
from hw_5_demoqa_tests.model import app


def test_student_registration_form():
    app.setup_ready()

    browser.element('#firstName').should(be.blank).type('Vika')
    browser.element('#lastName').should(be.blank).type('Mark')
    browser.element('#userEmail').should(be.blank).type('test@test.com')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').should(be.blank).type('1234567899')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('October')
    browser.element('.react-datepicker__year-select').type('1991')
    browser.element('[aria-label="Choose Monday, October 7th, 1991"]').click()
    browser.element('#subjectsInput').should(be.blank).type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/test.png'))
    browser.element('#currentAddress').type('Georgia Tbilisi')
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').press_enter()


    #Verification
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    browser.element("//td[preceding-sibling::td[contains(.,'Student Name')]]").should(have.text('Vika Mark'))
    browser.element("//td[preceding-sibling::td[contains(.,'Student Email')]]").should(have.text('test@test.com'))
    browser.element("//td[preceding-sibling::td[contains(.,'Gender')]]").should(have.text('Female'))
    browser.element("//td[preceding-sibling::td[contains(.,'Mobile')]]").should(have.text('1234567899'))
    browser.element("//td[preceding-sibling::td[contains(.,'Date of Birth')]]").should(have.text('07 October,1991'))
    browser.element("//td[preceding-sibling::td[contains(.,'Subjects')]]").should(have.text('English'))
    browser.element("//td[preceding-sibling::td[contains(.,'Hobbies')]]").should(have.text('Reading'))
    browser.element("//td[preceding-sibling::td[contains(.,'Picture')]]").should(have.text('test.png'))
    browser.element("//td[preceding-sibling::td[contains(.,'Address')]]").should(have.text('Georgia Tbilisi'))
    browser.element("//td[preceding-sibling::td[contains(.,'State and City')]]").should(have.text('Haryana Panipat'))