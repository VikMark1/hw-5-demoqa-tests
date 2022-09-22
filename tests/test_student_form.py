from hw_5_demoqa_tests.model import app
from hw_5_demoqa_tests.model.pages.registration_form import *
from hw_5_demoqa_tests.model.controls import checkbox, datepicker, file_attach, radiobutton

def test_student_registration_form():
    #GIVEN
    app.setup_ready()
    #WHEN
    fill_firstname('Vika')
    fill_lastname('Mark')
    fill_email('test@test.com')
    radiobutton.select_choice()
    fill_mobile('1234567899')
    datepicker.select_date('7 Oct 1991')
    #datepicker.select_date_2()
    fill_subjects(('English', 'Maths'))
    checkbox.select_checkbox()
    file_attach.add_pict('../resources/test.png')
    fill_address('Test address')
    scroll_to_state()
    set_state('NCR')
    set_city('Delhi')
    scroll_to_submit()
    submit_form()
    #THEN
    should_have_submitted(
        [
            ('Student Name', 'Vika Mark'),
            ('Student Email', 'test@test.com'),
            ('Gender', 'Female'),
            ('Mobile', '1234567899'),
            ('Date of Birth', '07 October,1991'),
            ('Subjects', 'English, Maths'),
            ('Hobbies', 'Reading'),
            ('Picture', 'test.png'),
            ('Address', 'Test address'),
            ('State and City', 'NCR Delhi')
        ]
    )


