from selene import browser, be, have


from controls import resource
from datetime import datetime


class RegistrationPage:
    def fill_first_name(self, dataUser):
        browser.element('#firstName').click().should(be.blank).type(dataUser.firstName)

    def fill_last_name(self, dataUser):
        browser.element('#lastName').click().should(be.blank).type(dataUser.lastName)

    def fill_email(self, dataUser):
        browser.element('#userEmail').click().should(be.blank).type(dataUser.email)

    def choice_gender(self, dataUser):
        gender_dict = {
            'Male': 1,
            'Female': 2,
            'Other': 3
        }
        browser.element(f'[for="gender-radio-{gender_dict[dataUser.gender]}"]').click()

    def fill_number_phone(self, dataUser):
        browser.element('#userNumber').click().should(be.blank).type(dataUser.phoneNumber)

    def choice_birthday(self, dataUser):
        date_text = dataUser.dateBirth
        date_format = '%d %B,%Y'
        date_formated = str(datetime.strptime(date_text, date_format).date()).split('-')
        date_formated = [int(i) for i in date_formated]
        date_formated[2] = str(date_formated[2]).rjust(3, '0')

        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(f'[value="{date_formated[0]}"]').click()
        browser.element('[class*=month-select]').click()
        browser.element(f'[class*=month-select] [value="{int(date_formated[1]) - 1}"]').click()
        browser.element(f'[class*=day--{date_formated[2]}]').click()

    def fill_subject(self, dataUser):
        browser.element('#subjectsInput').click().type(dataUser.subject).press_tab()

    def choice_hobbies(self, dataUser):
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()
        browser.element('[for=hobbies-checkbox-3]').click()

    def upload_img(self, dataUser):
        browser.element('[type=file]').send_keys(resource.path(dataUser.fileName))

    def fill_address(self, dataUser):
        browser.element('#currentAddress').click().should(be.blank).type(dataUser.address)

    def state_city(self, dataUser):
        browser.element('#react-select-3-input').type(dataUser.state).press_enter()
        browser.element('#react-select-4-input').type(dataUser.city).press_enter()

    def open_url(self):
        browser.open('/automation-practice-form')

    def click_submit(self):
        browser.element('#submit').press_enter()

    def register(self, dataUser):
        self.fill_first_name(dataUser)
        self.fill_last_name(dataUser)
        self.fill_email(dataUser)
        self.choice_gender(dataUser)
        self.fill_number_phone(dataUser)
        self.choice_birthday(dataUser)
        self.fill_subject(dataUser)
        self.choice_hobbies(dataUser)
        self.upload_img(dataUser)
        self.fill_address(dataUser)
        self.state_city(dataUser)
        self.click_submit()

    def should_have_registered(self, dataUser):
        browser.all('tbody tr td').should(
            have.texts('Student Name', f'{dataUser.firstName} {dataUser.lastName}', 'Student Email', dataUser.email,
                       'Gender',
                       dataUser.gender, 'Mobile',
                       dataUser.phoneNumber, 'Date of Birth', dataUser.dateBirth, 'Subjects', dataUser.subject,
                       'Hobbies', dataUser.hobbies, 'Picture', dataUser.fileName, 'Address', dataUser.address,
                       'State and City', f'{dataUser.state} {dataUser.city}'))