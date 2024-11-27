import allure

from pages.personal_account import PersonalAccount
from data import URL


@allure.suite("Личный кабинет")
@allure.sub_suite("Тесты")
class TestPersonalAccount:
    @allure.title("Переход по клику на «Личный кабинет»")
    def test_move_to_personal_account(self, driver, create_user, delete_user):
        result = PersonalAccount(driver).move_to_personal_account(create_user[0], create_user[1])
        assert result == f"{URL.MAIN}{URL.PERSONAL_ACCOUNT}"

    @allure.title("Переход в раздел «История заказов")
    def test_move_to_order_history(self, driver, create_user, delete_user):
        result = PersonalAccount(driver).move_to_order_history(create_user[0], create_user[1])
        assert result == f"{URL.MAIN}{URL.ORDER_HISTORY}"

    @allure.title("Выход из аккаунта")
    def test_log_out(self, driver, create_user, delete_user):
        result = PersonalAccount(driver).logout(create_user[0], create_user[1])
        assert result == f"{URL.MAIN}{URL.LOGIN}"
