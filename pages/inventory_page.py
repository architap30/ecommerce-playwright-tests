class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button = page.locator(
            "[data-test='add-to-cart-sauce-labs-backpack']"
        )
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.cart_icon = page.locator("[data-test='shopping-cart-link']")

    def add_backpack_to_cart(self):
        self.add_to_cart_button.click()

    def get_cart_count(self):
        return self.cart_badge.text_content()

    def go_to_cart(self):
        self.cart_icon.click()