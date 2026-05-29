import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.navigate()
    login.login("standard_user", "secret_sauce")
    return page


def test_add_item_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == "1"


def test_cart_badge_updates(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    cart_count = inventory.get_cart_count()
    assert cart_count == "1"


def test_item_appears_in_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    assert cart.get_cart_item_count() == 1


def test_remove_item_from_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    cart = CartPage(logged_in_page)
    cart.remove_item()
    assert cart.get_cart_item_count() == 0