import time

import allure

from .base_page import BasePage
from .locators import MainFunctionalLocators
from data import URL


class MainFunctional(BasePage):
    def move_to_lego(self):
        with allure.step("Перехожу на главную страницу"):
            self.driver.get(URL.MAIN)
        with allure.step("Нажимаю на кнопку 'Конструктор'"):
            self.click_to_element(MainFunctionalLocators.BUTTON_LEGO)
        with allure.step("Получаю текст заголовка h1"):
            return self.get_text_from_element(MainFunctionalLocators.HEADER_LEGO)

    def move_to_feed_order(self):
        with allure.step("Перехожу на главную страницу"):
            self.driver.get(URL.MAIN)
        with allure.step("Нажимаю на кнопку 'Лента Заказов'"):
            self.click_to_element(MainFunctionalLocators.BUTTON_FEED_ORDER)
        with allure.step("Получаю актуальный URL сайта"):
            return self.get_url(f"{URL.MAIN}{URL.FEED_ORDER}")

    def open_ingredient_details(self, ingredients, number):
        with allure.step("Перехожу на главную страницу"):
            self.driver.get(URL.MAIN)
        with allure.step("Нажимаю на кнопку 'Конструктор'"):
            self.click_to_element(MainFunctionalLocators.BUTTON_LEGO)
        with allure.step("Выбираю ингредиент"):
            self.find_elements_with_wait(ingredients)[number].click()
        with allure.step("Получаю статус окна с ингредиентами"):
            return self.find_element_with_wait(MainFunctionalLocators.INGREDIENT_DETAILS).is_displayed()

    def close_ingredient_details(self, ingredients, number):
        with allure.step("Открываю окно ингредиента"):
            self.open_ingredient_details(ingredients, number)
        with allure.step("Закрываю окно с ингредиентами"):
            self.move_to_element_and_click(MainFunctionalLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)
        with allure.step("Получаю статус окна с ингредиентами"):
            if self.driver.find_element(*MainFunctionalLocators.CLOSED_INGREDIENT_DETAILS):
                return True
            else:
                return False

    def counter_ingredients(self):
        with allure.step("Перехожу на главную страницу"):
            self.driver.get(URL.MAIN)
        with allure.step("Перетаскиваю ингредиент"):
            self.drag_and_drop(MainFunctionalLocators.LIST_INGREDIENT_BURGER_LOCATOR,
                               MainFunctionalLocators.CONSTRUCTOR)
            time.sleep(1)
        with allure.step("Проверяю счетчик элемента"):
            return int(self.find_elements_with_wait(MainFunctionalLocators.COUNTER)[0].text)

    def create_order(self, email, password):
        with allure.step("Перехожу на страницу входа"):
            self.driver.get(f"{URL.MAIN}{URL.LOGIN}")
        with allure.step(f"Захожу в аккаунт Email:{email}, Password:{password}"):
            self.login(email, password)
        with allure.step("Оформляю заказ"):
            self.drag_and_drop(MainFunctionalLocators.LIST_INGREDIENT_BURGER_LOCATOR,
                               MainFunctionalLocators.CONSTRUCTOR)
            time.sleep(1)
            self.click_to_element(MainFunctionalLocators.BUTTON_CREATE_ORDER)
        return self.get_new_text_from_element(MainFunctionalLocators.WINDOW_ORDER_NUMBER, "9999")


