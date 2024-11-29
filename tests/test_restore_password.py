import allure

from pages.restore_password import RestorePassword
from data import URL


@allure.suite("Страница восстановления пароля")
@allure.sub_suite("Тесты")
class TestRestorePassword:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль")
    def test_redirect_from_button(self, driver):
        restore_password = RestorePassword(driver).redirect_from_button()
        assert restore_password == f"{URL.MAIN}{URL.FORGOT_PASSWORD}"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_reset_password(self, driver):
        restore_password = RestorePassword(driver).reset_password()
        assert restore_password == f"{URL.MAIN}{URL.RESET_PASSWORD}"

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_return_input_password_status(self, driver):
        restore_password = RestorePassword(driver).return_input_password_status()
        assert restore_password is True
