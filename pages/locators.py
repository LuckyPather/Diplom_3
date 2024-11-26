from selenium.webdriver.common.by import By

OVERLAY_MODAL_WINDOW_CLOSE = By.CLASS_NAME, 'Modal_modal__close_modified__3V5XS'
OVERLAY_MODAL_WINDOW = By.CLASS_NAME, 'Modal_modal_overlay__x2ZCr'


class RestorePasswordLocators:
    LINK_RESTORE_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    INPUT_EMAIL = By.NAME, "name"
    BUTTON_RESTORE_PASSWORD = By.XPATH, ".//button[text()='Восстановить']"
    INPUT_ICON = By.CLASS_NAME, "input__icon"
    INPUT_PASSWORD_STATUS_ACTIVE = By.CLASS_NAME, "input_status_active"


class PersonalAccountLocators:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"
    BUTTON_HISTORY_ORDER = By.XPATH, ".//a[text()='История заказов']"
    BUTTON_EXIT = By.XPATH, ".//button[text()='Выход']"


class LoginLocators:
    INPUT_EMAIL = By.NAME, "name"
    INPUT_PASSWORD = By.NAME, "Пароль"
    BUTTON_LOGIN = By.XPATH, ".//button[text()='Войти']"
