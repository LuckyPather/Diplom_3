import time

import allure

from .base_page import BasePage
from .locators import PersonalAccountLocators, OVERLAY_MODAL_WINDOW_CLOSE
from data import URL


class PersonalAccount(BasePage):
    def move_to_personal_account(self, email, password):
        with allure.step("Перехожу на главную страницу"):
            self.driver.get(URL.MAIN)
        with allure.step("Нажимаю на кнопку личного кабинета"):
            time.sleep(2)
            #click_by_element_with_wait или опять таки ждем пока элемент виден
            #self.close_modal_window()
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        with allure.step(f"Захожу в аккаунт Email:{email}, Password:{password}"):
            self.login(email, password)
        with allure.step("Нажимаю на кнопку личного кабинета"):
            time.sleep(2)
            #self.close_modal_window()
            self.click_to_element(PersonalAccountLocators.BUTTON_PERSONAL_ACCOUNT)
        return self.get_url(f"{URL.MAIN}{URL.PERSONAL_ACCOUNT}")

