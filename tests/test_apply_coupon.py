from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage


def test_apply_coupon_discount():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("igor@mail.com", "igor123")

        # Add pizzas to cart
        home_page = HomePage(page)
        home_page.add_pizza_to_cart("Пицца \"4 в 1\"")
        home_page.add_pizza_to_cart("Пицца \"Как у бабушки\"")
        home_page.go_to_cart()

        # Apply coupon and verify discount
        checkout_page = CheckoutPage(page)
        initial_price = checkout_page.get_total_price()
        checkout_page.apply_coupon("GIVEMEHALYAVA")
        discounted_price = checkout_page.get_total_price()

        assert discounted_price == initial_price * 0.9, "Discount not applied correctly"

        context.close()
        browser.close()