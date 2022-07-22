from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_cant_see_product_in_basket_opened_from_product_page(self):
        open_basket = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        open_basket.click()
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Basket is not empty!"
