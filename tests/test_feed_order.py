import pytest
import allure

from pages.feed_order import FeedOrderPage


@allure.suite("Раздел «Лента заказов»")
@allure.sub_suite("Тесты")
class TestFeedOrderPage:
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    @pytest.mark.parametrize("number", [0, 1, 2, 3])
    def test_open_order_details(self, driver, number):
        result = FeedOrderPage(driver).open_order_details(1)
        assert result is True

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_check_user_orders_in_feed_orders(self, driver, create_user, delete_user):
        result = FeedOrderPage(driver).check_user_orders_in_feed_orders(create_user[0], create_user[1])
        assert result is True, "Не все заказы попали в общий список"

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_check_counter_all_time(self, driver, create_user, delete_user):
        result = FeedOrderPage(driver).check_counters(create_user[0], create_user[1])
        assert int(result[0][0]) < int(result[1][0]), "Счетчик заказов за все время работает неверно"

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_check_counter_today(self, driver, create_user, delete_user):
        result = FeedOrderPage(driver).check_counters(create_user[0], create_user[1])
        assert int(result[0][1]) < int(result[1][1]), "Счетчик заказов за сегодня работает неверно"

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_verify_order_in_progress(self, driver, create_user, delete_user):
        result = FeedOrderPage(driver).verify_order_in_progress(create_user[0], create_user[1])
        assert result[0] in result[1] or result[0] in result[
            2], "Заказ не находится ни в состоянии 'Готовится', ни в состоянии 'Готов'"
