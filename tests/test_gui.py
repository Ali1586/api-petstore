import pytest
from playwright.sync_api import expect

def test_login_success(login_page, page):
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.parametrize("user, pwd", [
    ("locked_out_user", "secret_sauce"),
    ("wrong_user", "wrong_pass")
])
def test_login_failure(login_page, user, pwd):
    login_page.navigate()
    login_page.login(user, pwd)
    # _error_msg måste vara definierad i din LoginPage-klass
    expect(login_page._error_msg).to_be_visible()