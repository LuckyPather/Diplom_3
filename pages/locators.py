from selenium.webdriver.common.by import By


class RestorePassword:
    LINK_RESTORE_PASSWORD = (By.CLASS_NAME, "Auth_link__1fOlj")
    INPUT_EMAIL = (By.NAME, "name")
    BUTTON_RESTORE_PASSWORD = By.XPATH, ".//button[text()='Восстановить']"


