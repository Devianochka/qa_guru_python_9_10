import dataclasses


@dataclasses.dataclass
class DataUser:
    firstName: str
    lastName: str
    email: str
    gender: str
    phoneNumber: str
    dateBirth: str
    fileName: str
    subject: str
    state: str
    city: str
    hobbies: str
    address: str
    fileName: str


dataUser = DataUser(firstName='Diana', lastName='Sagaeva', email='d_sagaeva@mail.ru', gender='Female',
                    phoneNumber='8800555353', dateBirth='12 June,2001', fileName='tony.jpg', subject='English',
                    hobbies='Sports, Reading, Music', state='Haryana', city='Panipat', address='Leningradskoe shosse')