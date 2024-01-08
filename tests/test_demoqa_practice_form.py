from pages.registration_page import RegistrationPage


def test_fill_form(browser_config):
    registration_page = RegistrationPage()

    registration_page.open_url('/automation-practice-form')

    registration_page.fill_first_name('Diana')

    registration_page.fill_last_name('Sagaeva')

    registration_page.fill_email('d_sagaeva@mail.ru')

    registration_page.choice_gender()

    registration_page.fill_number_phone('88005553535')

    registration_page.choice_birthday()

    registration_page.fill_subject('English')

    registration_page.choice_hobbies()

    registration_page.upload_img('tony.jpg')

    registration_page.fill_address('Leningradskoe shosse')

    registration_page.state_city('Haryana', 'Panipat')

    registration_page.click_submit()

    registration_page.should_have_registered('Diana', 'Sagaeva', 'd_sagaeva@mail.ru', 'Female',  '8800555353',
                                             '12 June,2001', 'English', 'Sports, Reading, Music', 'tony.jpg',
                                             'Leningradskoe shosse', 'Haryana Panipat')