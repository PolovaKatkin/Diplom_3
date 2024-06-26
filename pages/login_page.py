import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Вводим емейл пользователя.')
    def set_user_email(self, email):
        self.set_value(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Вводим пароль пользователя.')
    def set_user_password(self, password):
        self.set_value(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('Авторизируем пользователя.')
    def confirm_user_authorization(self):
        self.click_element_with_wait(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Проверка отображение окна авторизации.')
    def show_authorization_form(self):
        return self.find_and_wait_element(LoginPageLocators.LOGIN_BUTTON).text
