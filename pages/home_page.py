from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def add_pizza_to_cart(self, pizza_name: str):
        self.page.get_by_role("link", name=f"Add “{pizza_name}”").click()

    def go_to_cart(self):
        self.page.get_by_role("link", name="Подробнее").nth(1).click()