import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .locators import LoginLocators, OVERLAY_MODAL_WINDOW
import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def drag_and_drop(self, element_from, element_to):
        source = self.find_element_with_wait(element_from)
        target = self.find_element_with_wait(element_to)
        if data.DRIVER_TYPE == "chrome":
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        else:
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(OVERLAY_MODAL_WINDOW))
            self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);

                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);

                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);

                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);

                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, source, target)

    def move_to_element_and_click(self, locator):
        element = self.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        if data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(OVERLAY_MODAL_WINDOW))
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        if data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(OVERLAY_MODAL_WINDOW))
            self.driver.find_element(*locator).click()
        else:
            self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.find_element_with_wait(locator).send_keys(value)

    def get_text_from_element(self, locator):
        if data.DRIVER_TYPE == "firefox":
            WebDriverWait(self.driver, 15).until_not(
                expected_conditions.visibility_of_any_elements_located(OVERLAY_MODAL_WINDOW))
        return self.find_element_with_wait(locator).text

    def get_new_text_from_element(self, locator, standard_text):
        new_text_status = False
        while new_text_status is False:
            if self.find_element_with_wait(locator).text == standard_text:
                time.sleep(2)
            else:
                new_text_status = True
        return self.find_element_with_wait(locator).text

    def get_url(self, url):
        try:
            WebDriverWait(self.driver, 10).until(lambda d: d.current_url == url)
            url = self.driver.current_url
            return url
        except Exception as e:
            return f"Ошибка полученный URL не соответствует ожидаемому {str(e)}"

    def login(self, email, password):
        self.send_keys(LoginLocators.INPUT_EMAIL, email)
        self.send_keys(LoginLocators.INPUT_PASSWORD, password)
        self.click_to_element(LoginLocators.BUTTON_LOGIN)
