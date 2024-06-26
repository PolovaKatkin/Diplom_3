import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    @allure.step('Находим заголовок страницы "Лента заказов".')
    def show_orders_list_form(self):
        return self.find_and_wait_element(OrderListPageLocators.HEADER_ORDER_LIST).text

    @allure.step("Открываем страницу 'Лента заказов'")
    def open_order_list_page(self):
        self.open_page(Urls.URL_MAIN_PAGE + Urls.URL_ORDER_LIST_PAGE)

    @allure.step("Переходим на главную страницу")
    def go_to_main_page(self):
        self.click_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Кликаем на первый заказ в списке заказов")
    def click_in_first_order_in_list(self):
        self.click_element(OrderListPageLocators.FIRST_ORDER_LIST)

    @allure.step("Находим текст 'Состав' на модальном окне с деталями заказа")
    def get_text_from_modal_window(self):
        return self.find_and_wait_element(OrderListPageLocators.MODEL_ORDER_WINDOW).text

    @allure.step('Проверяем счётчик «Выполнено за всё время».')
    def show_all_time_done_orders(self):
        all_time_count = self.find_and_wait_element(OrderListPageLocators.ALL_TIME_COUNT).text
        return all_time_count

    @allure.step('Проверяем счётчик «Выполнено за сегодня».')
    def show_today_done_orders(self):
        today_count = self.find_and_wait_element(OrderListPageLocators.TODAY_COUNT).text
        return today_count

    @allure.step('Проверяем заказ в разделе «В работе».')
    def show_created_order_in_work(self, order_count):
        order_number_in_work_formatted = self.format_locator(OrderListPageLocators.ORDER_NUMBER_IN_WORK, order_count)
        return self.find_and_wait_element(order_number_in_work_formatted).text

    @allure.step('Находим все заказы в ленте заказов.')
    def collect_order_numbers(self):
        order_elements = self.find_elements(OrderListPageLocators.BLOCK_ORDERS_LIST)
        order_numbers = []
        for order_element in order_elements:
            order_number_element = order_element.find_element(*OrderListPageLocators.ALL_ORDERS)
            order_number = order_number_element.text
            order_numbers.append(order_number)
        return order_numbers
