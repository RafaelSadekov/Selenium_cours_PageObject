from .base_page import BasePage
from .locators import LoginPageLocators
import time
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login URL is not presented"
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_url.click()
        assert "/accounts/login/" in self.browser.current_url, "'/accounts/login/' not in current url"
        print("\nclicked on link to forms!")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"
        print("\nchecked exist login form!")

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration Form is not presented"
        print("\nchecked exist registration form!")

    def register_new_user(self):
        register_link = browser.find_element(*LoginPageLocators.LOGIN_URL)
        register_link.click()
        e-mail = str(time.time()) + "@fakemail.org"
        input_email = browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(e-mail)
        password = str(time.time()) + "qwertyu"
        input_password = browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        repeat_password = browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_password.send_keys(password)
        register_button = browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

