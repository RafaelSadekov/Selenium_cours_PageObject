import pytest

from .pages.product_page import ProductPage


# #def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_product_page()
#     page.should_be_add_product_in_basket()
#     page.should_be_compare_name_product


# @pytest.mark.xfail(reason="Fix")
# @pytest.mark.need_review
@pytest.mark.parametrize('promo_offer',
                         ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    print(f"opened link: {link}")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_be_add_product_in_basket()
    page.should_be_compare_name_product()
    page.should_be_compare_cost_product_in_basket()
    page.should_be_guest_cant_see_success_message()
