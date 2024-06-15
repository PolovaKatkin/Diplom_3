from selenium.webdriver.common.by import By


class OrderListPageLocators:
    # Заголовок "Лента заказов"
    HEADER_ORDER_LIST = (By.XPATH, "//h1[text() = 'Лента заказов']")
    # Первый заказ в ленте заказов
    FIRST_ORDER_LIST = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6'][position() = (1)]")
    # Окно с деталями заказа
    MODEL_ORDER_WINDOW = (By.XPATH, "//p[@class = 'text text_type_main-medium mb-8']")
    # Блок "Лента заказов"
    BLOCK_ORDERS_LIST = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li")
    # Заказы в ленте заказов
    ALL_ORDERS = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # Счетчик заказов выполненных за все время
    ALL_TIME_COUNT = (By.XPATH,
                      "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (1)]")
    # Счетчик созданных заказов за все сегодня.
    TODAY_COUNT = (By.XPATH,
                   "/descendant::p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'][position() = (2)]")
    # Поле отображения заказов в работе.
    ORDER_NUMBER_IN_WORK = (By.XPATH, "//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
