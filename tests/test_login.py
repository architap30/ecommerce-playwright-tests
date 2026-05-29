import pytest
from pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_invalid_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("wrong_user", "wrong_pass")
    error = login.get_error_message()
    assert "Username and password do not match" in error


def test_empty_login(page):
    login = LoginPage(page)
    login.navigate()
    login.login("", "")
    error = login.get_error_message()
    assert "Username is required" in error


def test_locked_out_user(page):
    login = LoginPage(page)
    login.navigate()
    login.login("locked_out_user", "secret_sauce")
    error = login.get_error_message()
    assert "Sorry, this user has been locked out" in error