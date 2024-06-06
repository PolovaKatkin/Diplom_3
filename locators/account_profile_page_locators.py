from selenium.webdriver.common.by import By


class AccountProfilePageLocators:
    # Кнопка "Профиль"
    HEADER_PROFILE = (By.XPATH, "//a[text() = 'Профиль']")
    # Кнопка "Истроия заказов"
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[text() = 'История заказов']")
    # Кнопка "Выход"
    BUTTON_LOGOUT = (By.XPATH, "//button[text() = 'Выход']")
    # Номер заказа верхнего заказа в истории заказов
    NUMBER_ORDER_HISTORY = (By.XPATH, "//li/a/div/p[@class = 'text text_type_digits-default']")
