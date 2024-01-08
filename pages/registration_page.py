from selene import browser, be, have
from controls import resource


class RegistrationPage:

    def open_url(self, url):
        browser.open(url)

    def fill_first_name(self, firstName):
        browser.element('#firstName').click().should(be.blank).type(firstName)

    def fill_last_name(self, lastName):
        browser.element('#lastName').click().should(be.blank).type(lastName)

    def fill_email(self, email):
        browser.element('#userEmail').click().should(be.blank).type(email)

    def choice_gender(self):
        browser.element('[for="gender-radio-2"]').click()

    def fill_number_phone(self, number):
        browser.element('#userNumber').click().should(be.blank).type(number)

    def choice_birthday(self):
        browser.element('[id="dateOfBirthInput"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="2001"]').click()
        browser.element('[class*=month-select]').click()
        browser.element('[class*=month-select] [value="5"]').click()
        browser.element('[class*=day--012]').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').click().type(value).press_tab()

    def choice_hobbies(self):
        browser.element('[for=hobbies-checkbox-1]').click()
        browser.element('[for=hobbies-checkbox-2]').click()
        browser.element('[for=hobbies-checkbox-3]').click()

    def upload_img(self, img_name):
        browser.element('[type=file]').send_keys(resource.path(img_name))

    def fill_address(self, address):
        browser.element('#currentAddress').click().should(be.blank).type(address)

    def state_city(self, state, city):
        browser.element('#react-select-3-input').type(state).press_enter()
        browser.element('#react-select-4-input').type(city).press_enter()

    def click_submit(self):
        browser.element('#submit').press_enter()

    def should_have_registered(self, firstName, lastName, email, gender, phoneNumber, dateBirth, subjects, hobbies,
                               imgName, address,
                               stateCity):
        browser.all('tbody tr td').should(
            have.texts('Student Name', f'{firstName} {lastName}', 'Student Email', email, 'Gender', gender, 'Mobile',
                       phoneNumber, 'Date of Birth', dateBirth, 'Subjects', subjects,
                       'Hobbies', hobbies, 'Picture', imgName, 'Address', address,
                       'State and City', stateCity))