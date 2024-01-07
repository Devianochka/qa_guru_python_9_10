import os
from selene import browser, have, be
from resources.path import CURRENT_DIR


def test_fill_form(browser_config):
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().should(be.blank).type('Diana')
    browser.element('#lastName').click().should(be.blank).type('Sagaeva')
    browser.element('#userEmail').click().should(be.blank).type('d_sagaeva@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').click().should(be.blank).type('89005553535')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2001"]').click()
    browser.element('[class*=month-select]').click()
    browser.element('[class*=month-select] [value="5"]').click()
    browser.element('[class*=day--012]').click()
    browser.element('#subjectsInput').click().type('Eng').press_tab()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('[type=file]').send_keys(os.path.join(CURRENT_DIR, 'tony.jpg'))
    browser.element('#currentAddress').click().should(be.blank).type('Leningradskoe shosse')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()
    browser.all('tbody tr td')[1::2].should(
        have.texts('Diana Sagaeva', 'd_sagaeva@mail.ru', 'Female', '8900555353', '12 June,2001', 'English',
                   'Sports, Reading, Music', 'tony.jpg', 'Leningradskoe shosse', 'Haryana Panipat'))