class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator("[data-test='inventory-item']")
        self.remove_button = page.locator(
            "[data-test='remove-sauce-labs-backpack']"
        )
        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping = page.locator(
            "[data-test='continue-shopping']"
        )

    def get_cart_item_count(self):
        return self.cart_items.count()

    def remove_item(self):
        self.remove_button.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()