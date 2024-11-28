import pytest
import allure

from pages.feed_order import FeedOrderPage


class TestFeedOrderPage:
    @pytest.mark.parametrize("number", [0, 1, 2, 3])
    def test_open_order_details(self, driver, number):
        result = FeedOrderPage(driver).open_order_details(1)
        assert result is True

    def test_check_user_orders_in_feed_orders(self, driver, create_user, delete_user):
        FeedOrderPage(driver).check_user_orders_in_feed_orders(create_user[0], create_user[1])
