from pages.registration_page import RegistrationPage
from data.user import dataUser


def test_fill_form(browser_config):
    registration_page = RegistrationPage()
    registration_page.open_url()
    registration_page.register(dataUser)
    registration_page.should_have_registered(dataUser)