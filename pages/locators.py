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


class MainFunctionalLocators:
    BUTTON_LEGO = By.XPATH, ".//p[text()='Конструктор']"
    HEADER_LEGO = By.XPATH, ".//h1[text()='Соберите бургер']"
    LIST_INGREDIENT_BURGER_LOCATOR = By.CLASS_NAME, "BurgerIngredient_ingredient__1TVf6"
    INGREDIENT_DETAILS = By.CLASS_NAME, "Modal_modal__contentBox__sCy8X"
    BUTTON_CLOSE_INGREDIENT_DETAILS = By.CLASS_NAME, "Modal_modal__close_modified__3V5XS"
    CLOSED_INGREDIENT_DETAILS = By.CLASS_NAME, "Modal_modal__P3_V5"
    BUTTON_FEED_ORDER = By.XPATH, ".//p[text()='Лента Заказов']"
    CONSTRUCTOR = By.CLASS_NAME, "constructor-element_pos_top"
    COUNTER = By.CLASS_NAME, 'counter_counter__num__3nue1'
    WINDOW_ORDER_NUMBER = By.CLASS_NAME, 'Modal_modal__title_shadow__3ikwq'
    BUTTON_CREATE_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"


class FeedOrderLocator:
    ORDERS_LIST = By.CLASS_NAME, 'OrderHistory_listItem__2x95r'
    ORDER_DETAILS = By.CLASS_NAME, 'Modal_modal_opened__3ISw4'
    ORDERS_LIST_NUMBER = By.CLASS_NAME, 'text_type_digits-default'
    ORDER_STATUS = By.CLASS_NAME, "OrderFeed_orderListReady__1YFem"
    ORDER_COUNTERS = By.CLASS_NAME, "OrderFeed_number__2MbrQ"
    ORDER_IN_STATUS_COMPLETE = By.CLASS_NAME, 'OrderFeed_orderList__cBvyi'
