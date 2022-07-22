from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '.basket-mini>span>a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    INPUT_EMAIL = (By.XPATH, "//*[@id='id_registration-email']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='id_registration-password1']")
    REPEAT_PASSWORD = (By.XPATH, "//*[@id='id_registration-password2']")
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')
    REGISTER_SUCCESS = (By.XPATH, '//*[@id="messages"]/div/div')

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    ALLERT_INNER = (By.XPATH, "//*[@id='messages']/div[1]/div")
    ALLERT_INNER_PRODUCT = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_COST = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_COST_IN_BASKET = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//*[@id='content_inner']/p")

