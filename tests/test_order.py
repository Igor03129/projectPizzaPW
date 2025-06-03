from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage


def test_order_pizza():
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

        # Checkout
        checkout_page = CheckoutPage(page)
        checkout_page.fill_order_details(
            name="igor",
            surname="igorc",
            address="asd",
            city="mos",
            region="mos",
            postal_code="123",
            phone="+1237654321",
            date="2025-06-03",
            comments="qwe asd"
        )
        checkout_page.select_payment_method("Оплата при доставке")
        checkout_page.apply_coupon("DC120")
        checkout_page.agree_to_terms()
        checkout_page.place_order()

        context.close()
        browser.close()