import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .personal_account import PersonalAccount
from .base_page import BasePage
from .main_functional import MainFunctional
from .locators import FeedOrderLocator, MainFunctionalLocators, PersonalAccountLocators
from data import URL, SUCCESS_STATUS_ORDER


class FeedOrderPage(BasePage):
    def open_order_details(self, number):
        with allure.step("Перехожу на страницу с заказами"):
            self.driver.get(f"{URL.MAIN}{URL.FEED_ORDER}")
        with allure.step("Выбираю заказ из списка"):
            self.find_elements_with_wait(FeedOrderLocator.ORDERS_LIST)[number].click()
        with allure.step("Отправляю статус окна заказов"):
            return self.find_element_with_wait(FeedOrderLocator.ORDER_DETAILS).is_displayed()

    def check_user_orders_in_feed_orders(self, email, password):
        with allure.step("Захожу за пользователя создаю заказ"):
            order = MainFunctional(self.driver).create_order(email, password)
            self.move_to_element_and_click(MainFunctionalLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)
        with allure.step("Собираю список номеров заказов"):
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
            self.click_to_element(PersonalAccountLocators.BUTTON_HISTORY_ORDER)
            list_personal_order_text = [f"#0{order}"]
        with allure.step("Перехожу в ленту заказов, получаю список заказов"):
            self.click_to_element(MainFunctionalLocators.BUTTON_FEED_ORDER)
            while self.get_text_from_element(FeedOrderLocator.ORDER_STATUS) != SUCCESS_STATUS_ORDER:
                time.sleep(1)
            list_feed_order = self.find_elements_with_wait(FeedOrderLocator.ORDERS_LIST_NUMBER)
            list_feed_order_text = [element.text for element in list_feed_order if element.text.startswith("#")]
        with allure.step("Проверяю что заказ из личного кабинета находится в общем списке"):
            if all(item in list_feed_order_text for item in list_personal_order_text):
                return True
            else:
                return False

    def check_counters(self, email, password):
        with allure.step("Перехожу на страницу заказов, запоминаю состояние счетчиков"):
            self.driver.get(f"{URL.MAIN}{URL.FEED_ORDER}")
            order_counter_list = self.find_elements_with_wait(FeedOrderLocator.ORDER_COUNTERS)
            order_counter_list_text = [order.text for order in order_counter_list]
        with allure.step("Создаю заказ"):
            MainFunctional(self.driver).create_order(email, password)
            self.move_to_element_and_click(MainFunctionalLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)
        with allure.step("Перехожу в ленту заказов, получаю новое состояние счетчиков"):
            self.click_to_element(MainFunctionalLocators.BUTTON_FEED_ORDER)
            time.sleep(2)
            while self.get_text_from_element(FeedOrderLocator.ORDER_STATUS) != SUCCESS_STATUS_ORDER:
                time.sleep(1)
            new_order_counter_list = self.find_elements_with_wait(FeedOrderLocator.ORDER_COUNTERS)
            new_order_counter_list_text = [order.text for order in new_order_counter_list]
        return order_counter_list_text, new_order_counter_list_text

    def verify_order_in_progress(self, email, password):
        with allure.step("Создаю заказ"):
            order = MainFunctional(self.driver).create_order(email, password)
            self.move_to_element_and_click(MainFunctionalLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)
        with allure.step("Перехожу в ленту заказов, получаю список заказов в работе"):
            self.click_to_element(MainFunctionalLocators.BUTTON_FEED_ORDER)
            order_status = self.get_text_from_element(FeedOrderLocator.ORDER_STATUS)
            order_status_list = self.get_text_from_element(FeedOrderLocator.ORDER_IN_STATUS_COMPLETE)
        return order, order_status, order_status_list.replace("\n", "")
