from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Личный кабинет"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    # Главная страница сайта.
    MAIN_PAGE = (By.CLASS_NAME, "App_App__aOmNj")
    # Заголовок главной старницы "Соберите бургер"
    HEADER_MAIN_PAGE = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    # Кнопка "Лента заказов"
    BUTTON_ORDER_LIST = (By.XPATH, "//p[text() = 'Лента Заказов']")
    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//li/a[@href = '/']")
    # Булка, первая в списке
    BUN_FIRST_IN_LIST = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    # Заголовок окна с деталями ингредиента
    HEADER_MODAL_INGREDIENT = (By.XPATH, "//h2[text() = 'Детали ингредиента']")
    INGR_MODAL = (
        By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]")
    # Кнопка крестика в модальном окне ингредиента
    BUTTON_CROSS_IN_MODAL_INGREDIENT = (
        By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # Верхняя булка в конструкторе
    BUN_IN_CONSTRUCTOR = (By.XPATH, '//section/ul/li[1]')
    # Кнопка "Оформить заказ"
    BUTTON_CONFIRM_ORDER = (By.XPATH, "//button[text() = 'Оформить заказ']")
    # Кнопка крестика в модальном окне оформленного заказа
    BUTTON_CROSS_IN_MODAL = (By.XPATH,
                             "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    # Текст "Ваш заказ начали готовить" в модальном окне оформленного заказа
    TEXT_IN_ORDER_MODAL = (By.XPATH, "//p[text() = 'Ваш заказ начали готовить']")
    # Cчетчик ингредиента
    COUNTER_INGREDIENT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
