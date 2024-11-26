import allure
from .base_page import BasePage
from .locators import RestorePasswordLocators, OVERLAY_MODAL_WINDOW_CLOSE
from data import URL


class RestorePassword(BasePage):
    def redirect_from_button(self):
        with allure.step("Открываю страницу входа в аккаунт"):
            self.driver.get(f"{URL.MAIN}{URL.LOGIN}")
        with allure.step("Закрываю модальное окно"):
            self.move_to_element_and_click(OVERLAY_MODAL_WINDOW_CLOSE)
        with allure.step("Нажимаю на кнопку восстановления пароля"):
            self.click_to_element(RestorePasswordLocators.LINK_RESTORE_PASSWORD)
        url = self.get_url(f"{URL.MAIN}{URL.FORGOT_PASSWORD}")
        return url

    def reset_password(self):
        with allure.step("Открываю страницу смены пароля"):
            self.driver.get(f"{URL.MAIN}{URL.RESET_PASSWORD}")
        with allure.step("Ввожу email в поле восстановления email"):
            self.send_keys(RestorePasswordLocators.INPUT_EMAIL, "test@mai.com")
        with allure.step("Закрываю модальное окно"):
            self.move_to_element_and_click(OVERLAY_MODAL_WINDOW_CLOSE)
        with allure.step("Нажимаю на кнопку 'Восстановить'"):
            self.click_to_element(RestorePasswordLocators.BUTTON_RESTORE_PASSWORD)
        url = self.get_url(f"{URL.MAIN}{URL.RESET_PASSWORD}")
        return url

    def return_input_password_status(self):
        with allure.step("Перехожу на страницу сброса пароля"):
            self.driver.get(f"{URL.MAIN}{URL.RESET_PASSWORD}")
            self.send_keys(RestorePasswordLocators.INPUT_EMAIL, "test@mai.com")
            with allure.step("Закрываю модальное окно"):
                self.move_to_element_and_click(OVERLAY_MODAL_WINDOW_CLOSE)
            self.click_to_element(RestorePasswordLocators.BUTTON_RESTORE_PASSWORD)
        with allure.step("Нажимаю на поле ввода пароля"):
            with allure.step("Закрываю модальное окно"):
                self.move_to_element_and_click(OVERLAY_MODAL_WINDOW_CLOSE)
            self.click_to_element(RestorePasswordLocators.INPUT_ICON)
        with allure.step("Проверяю, что поменялся класс поля и по нему можно найти элемент"):
            try:
                if self.find_element_with_wait(RestorePasswordLocators.INPUT_PASSWORD_STATUS_ACTIVE):
                    return True
            except Exception as e:
                allure.attach(f"Error: {str(e)}", name="Ошибка при поиске элемента")
                return False
