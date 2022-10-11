from hw_5_demoqa_tests.model import app
from hw_5_demoqa_tests.model.data.user import student

def test_student_registration_form():
    (
        app.registration_form.setup_ready()

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

#High-level business step ->
def test_submit_user():
    app.submit_form.submit()