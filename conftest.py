import pytest
import allure
import requests
from selenium import webdriver

import data
from data import URL
from helpers import Generators


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        with allure.step("Запускаю тест на браузере Chrome"):
            data.DRIVER_TYPE = "chrome"
            driver = webdriver.Chrome()
    else:
        with allure.step("Запускаю тест на браузере firefox"):
            data.DRIVER_TYPE = "firefox"
            driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
@allure.step("Создаю пользователя")
def create_user():
    generator = Generators()
    data_user = {
        "email": generator.email,
        "password": generator.password,
        "name": generator.name
    }
    with allure.step(
            f"Создаю пользователя с данными email: {generator.email}, password {generator.password}, name {generator.name}"):
        response = requests.post(f"{URL.MAIN}{URL.API_USER_CREATE}", json=data_user).json()
    assert response['accessToken'] is not None, "Ошибка создания пользователя"
    return generator.email, generator.password, generator.name, response


@pytest.fixture
@allure.title("Удаляю созданного пользователя")
def delete_user(create_user):
    access_token = create_user[3]['accessToken']
    yield
    with allure.step(
            f"Удаляю пользователя с данными email: {create_user[0]}, password {create_user[1]}, name {create_user[2]}"):
        requests.delete(f"{URL.MAIN}{URL.API_USER_DELETE}", headers={"Authorization": f"{access_token}"})
