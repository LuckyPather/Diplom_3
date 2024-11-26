import allure

from pages.personal_account import PersonalAccount
from data import URL


class TestPersonalAccount:
    def test_move_to_personal_account(self, driver, create_user, delete_user):
        result = PersonalAccount(driver).move_to_personal_account(create_user[0], create_user[1])
        assert result == f"{URL.MAIN}{URL.PERSONAL_ACCOUNT}"
