import allure
import pytest

from pages.main_functional import MainFunctional
from pages.locators import MainFunctionalLocators
from data import URL, STANDART_VALUE_ORDER


@allure.suite("Основной функционал")
@allure.sub_suite("Тесты")
class TestMainFunctional:
    @allure.title("Переход по клику на «Конструктор»")
    def test_move_to_lego(self, driver):
        result = MainFunctional(driver).move_to_lego()
        assert result == "Соберите бургер", "Заголовок страницы конструктора не найден"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_move_to_feed_order(self, driver):
        result = MainFunctional(driver).move_to_feed_order()
        assert result == f"{URL.MAIN}{URL.FEED_ORDER}"

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    @pytest.mark.parametrize('ingredients, number', [
        (MainFunctionalLocators.LIST_INGREDIENT_BURGER_LOCATOR, 0),
        (MainFunctionalLocators.LIST_INGREDIENT_BURGER_LOCATOR, 1)
    ])
    def test_open_ingredient_details(self, driver, ingredients, number):
        result = MainFunctional(driver).open_ingredient_details(ingredients, number)
        assert result is True

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @pytest.mark.parametrize('ingredients, number', [
        (MainFunctionalLocators.LIST_INGREDIENT_BURGER_LOCATOR, 0),
        (MainFunctionalLocators.LIST_INGREDIENT_BURGER_LOCATOR, 1)
    ])
    def test_open_ingredient_details(self, driver, ingredients, number):
        result = MainFunctional(driver).close_ingredient_details(ingredients, number)
        assert result is True

    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter_ingredients(self, driver):
        result = MainFunctional(driver).counter_ingredients()
        assert result == 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, driver, create_user, delete_user):
        result = MainFunctional(driver).create_order(create_user[0], create_user[1])
        assert result != STANDART_VALUE_ORDER
