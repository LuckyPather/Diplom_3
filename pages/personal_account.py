import allure

from .base_page import BasePage
from .locators import PersonalAccountLocators
from data import URL


class PersonalAccount(BasePage):
    def move_to_personal_account(self, email, password):
        with allure.step("Перехожу на главную страницу"):
            self.driver.get(URL.MAIN)
        with allure.step("Нажимаю на кнопку личного кабинета"):
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        with allure.step(f"Захожу в аккаунт Email:{email}, Password:{password}"):
            self.login(email, password)
        with allure.step("Нажимаю на кнопку личного кабинета"):
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        return self.get_url(f"{URL.MAIN}{URL.PERSONAL_ACCOUNT}")

    def move_to_order_history(self, email, password):
        with allure.step("Перехожу на страницу входа в аккаунт"):
            self.driver.get(f"{URL.MAIN}{URL.LOGIN}")
        with allure.step(f"Захожу в аккаунт Email:{email}, Password:{password}"):
            self.login(email, password)
        with allure.step("Нажимаю на кнопку личного кабинета"):
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        with allure.step("Нажимаю на кнопку 'История заказов'"):
            self.click_to_element(PersonalAccountLocators.BUTTON_HISTORY_ORDER)
        return self.get_url(f"{URL.MAIN}{URL.ORDER_HISTORY}")

    def logout(self, email, password):
        with allure.step("Перехожу на страницу входа в аккаунт"):
            self.driver.get(f"{URL.MAIN}{URL.LOGIN}")
        with allure.step(f"Захожу в аккаунт Email:{email}, Password:{password}"):
            self.login(email, password)
        with allure.step("Нажимаю на кнопку личного кабинета"):
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        with allure.step("Нажимаю на кнопку 'Выход'"):
            self.click_to_element(PersonalAccountLocators.BUTTON_EXIT)
        return self.get_url(f"{URL.MAIN}{URL.LOGIN}")
