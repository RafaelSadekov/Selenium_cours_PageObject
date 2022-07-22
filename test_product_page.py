import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.xfail(reason="Fix")
@pytest.mark.parametrize('promo_offer',
                         [i for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(f"opened link: {link}")
    page = ProductPage(browser, link)
    page.open()
    #page.should_be_product_page()
    page.should_be_check_avaliable_basket()
    page.should_be_add_product_in_basket()
    page.should_be_compare_name_product()
    page.should_be_compare_cost_product_in_basket()
    page.should_be_guest_cant_see_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # 1. Гость открывает страницу товара
    page = BasketPage(browser, link)
    page.open()
        # 2. Переходит в корзину по кнопке в шапке сайта
    page.should_be_cant_see_product_in_basket_opened_from_product_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = email
        page.register_new_user(str(password))
