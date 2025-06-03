from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_order_details(self, name: str, surname: str, address: str, city: str, region: str, postal_code: str, phone: str, date: str, comments: str):
        self.page.get_by_role("textbox", name="Имя *").fill(name)
        self.page.get_by_role("textbox", name="Фамилия *").fill(surname)
        self.page.get_by_role("textbox", name="Адрес *").fill(address)
        self.page.get_by_role("textbox", name="Город / Населенный пункт *").fill(city)
        self.page.get_by_role("textbox", name="Область *").fill(region)
        self.page.get_by_role("textbox", name="Почтовый индекс *").fill(postal_code)
        self.page.get_by_role("textbox", name="Телефон *").fill(phone)
        self.page.get_by_role("textbox", name="Дата заказа (дополнительно)").fill(date)
        self.page.get_by_role("textbox", name="Комментарии к заказу (дополнительно)").fill(comments)

    def select_payment_method(self, method: str):
        self.page.get_by_role("radio", name=method).check()

    def place_order(self):
        self.page.get_by_role("button", name="Оформить заказ").click()

    def apply_coupon(self, coupon_code: str):
        self.page.get_by_role("link", name="Нажмите для ввода купона").click()
        self.page.get_by_role("textbox", name="Введите код купона").fill(coupon_code)
        self.page.get_by_role("button", name="Применить купон").click()

    def agree_to_terms(self):
        self.page.get_by_role("checkbox", name="I have read and agree to the").check()