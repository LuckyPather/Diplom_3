from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .locators import LoginLocators, OVERLAY_MODAL_WINDOW
import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_element_by_javascript(self, locator):
        self.driver.execute_script("arguments[0].click();", self.find_element_with_wait(locator))

    def close_modal_window(self):
        self.driver.execute_script(f"document.querySelector('.Modal_modal__P3_V5').remove();")

    def move_to_element_and_click(self, locator):
        element = self.driver.find_element_with_wait(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

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
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

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
