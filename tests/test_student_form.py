import datetime
import allure
from selene import have, command
from selene.support.shared import browser

from hw_5_demoqa_tests.model import app
from hw_5_demoqa_tests.model.data import user
from hw_5_demoqa_tests.model.data.user import Gender
from hw_5_demoqa_tests.model.pages import registration_form



def test_student_registration_form():
    #GIVEN
    app.setup_ready()

    #WHEN
    registration_form.fill_firstname('Vika')
    registration_form.fill_lastname('Mark')
    registration_form.fill_email('test@test.com')
    registration_form.fill_gender(user.Gender.Female)
    registration_form.fill_mobile('1234567899')
    registration_form.fill_birthday(datetime.date(2001, 10, 7))
    #registration_form.assert_filled_birthday(datetime.date(1991, 10, 7))
    #registration_form.datepicker.select_date_2()
    registration_form.fill_subjects(('English', 'Maths'))
    registration_form.fill_hobbies(user.Hobby.Music, user.Hobby.Reading)
    registration_form.select_picture('../resources/test.png')
    registration_form.fill_address('Test address')
    registration_form.scroll_to_state()
    registration_form.set_state('NCR')
    registration_form.set_city('Delhi')
    registration_form.scroll_to_submit()
    registration_form.submit_form()

    #THEN
    registration_form.should_have_submitted(
        [
            ('Student Name', 'Vika Mark'),
            ('Student Email', 'test@test.com'),
            ('Gender', 'Female'),
            ('Mobile', '1234567899'),
            ('Date of Birth', '07 October,2001'),
            ('Subjects', 'English, Maths'),
            ('Hobbies', 'Music, Reading'),
            ('Picture', 'test.png'),
            ('Address', 'Test address'),
            ('State and City', 'NCR Delhi')
        ]
    )
