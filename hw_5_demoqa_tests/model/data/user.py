import datetime
from enum import Enum
from dataclasses import dataclass
from typing import Tuple
import hw_5_demoqa_tests


class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3

class Hobby(Enum):
    Music: str = 'Music'
    Reading: str = 'Reading'

class Subject(Enum):
    English: str = 'English'
    Maths: str = 'Maths'

def format_input_date(value: datetime.date):
    return value.strftime(hw_5_demoqa_tests.config.datetime_input_format)

@dataclass
class User:
    gender: Gender
    firstname: str
    birth_date: datetime.date(2001, 10, 7)
    hobbies: Tuple[Hobby] = (Hobby.Music, Hobby.Reading)
    subjects: Tuple[Subject] = (Subject.English, Subject.Maths)
    lastname: str = 'Mark'
    picture: str = '../resources/test.png'
    address: str = 'Test address'
    state: str = 'NCR'
    city: str = 'Delhi'
    email: str = 'test@test.com'
    mobile: str = '1234567899'

student = User(firstname='Vika', gender=Gender.Female, birth_date=datetime.date(2001, 10, 7))
