from pages.django_pages.base_pages import BasePage


def test_open_admin(browser):
    bs = BasePage(browser)
    bs.open_base_page()
