import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .personal_account import PersonalAccount
from .base_page import BasePage
from .main_functional import MainFunctional
from .locators import FeedOrderLocator, MainFunctionalLocators, PersonalAccountLocators
from data import URL, USER_WITH_ORDERS


class FeedOrderPage(BasePage):
    def open_order_details(self, number):
        with allure.step("Перехожу на страницу с заказами"):
            self.driver.get(f"{URL.MAIN}{URL.FEED_ORDER}")
        with allure.step("Выбираю заказ из списка"):
            self.find_elements_with_wait(FeedOrderLocator.ORDERS_LIST)[number].click()
        with allure.step("Отправляю статус окна заказов"):
            return self.find_element_with_wait(FeedOrderLocator.ORDER_DETAILS).is_displayed()

    # TODO: Создать нужно заказы
    def check_user_orders_in_feed_orders(self, email, password):
        with allure.step("Захожу за пользователя создаю заказ"):
            order = MainFunctional(self.driver).create_order(email, password)
            self.move_to_element_and_click(MainFunctionalLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)
        with allure.step("Собираю список номеров заказов"):
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
            self.click_to_element(PersonalAccountLocators.BUTTON_HISTORY_ORDER)
            #list_personal_order = self.find_elements_with_wait(FeedOrderLocator.ORDERS_LIST_NUMBER)
            list_personal_order_text = [f"#0{order}"]
        with allure.step("Перехожу в ленту заказов, получаю список заказов"):
            self.click_to_element(MainFunctionalLocators.BUTTON_FEED_ORDER)
            time.sleep(10)
            list_feed_order = self.find_elements_with_wait(FeedOrderLocator.ORDERS_LIST_NUMBER)
            list_feed_order_text = [element.text for element in list_feed_order if element.text.startswith("#")]
            print(list_personal_order_text)
            print(list_feed_order_text)
            if all(item in list_feed_order_text for item in list_personal_order_text):
                print("jr")
