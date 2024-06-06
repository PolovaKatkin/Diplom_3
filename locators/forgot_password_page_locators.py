from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # Cсылка на страницу восстановления пароля
    LINK_FORGOT_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    # Поле Email
    FIELD_EMAIL = (By.XPATH, '//input[@name="name"]')
    # Кнопка "Восстановить"
    BUTTON_RECOVER = (By.XPATH, "//button[text() = 'Восстановить']")
    # Поле Пароль
    FIELD_PASSWORD = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' "
                                "and @name = 'Введите новый пароль']")
    # Кнопка видимости пароля не активна
    BUTTON_VISIBILITY_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    # Поле Пароль в статусе "активно" (символы пароля видны)
    FIELD_PASSWORD_ACTIVE = \
        (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    # Заголовок страницы "Восстановление пароля"
    HEADING_TEXT = (By.XPATH, "//h2[text() = 'Восстановление пароля']")
