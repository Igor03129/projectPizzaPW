from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://pizzeria.skillbox.cc/")

    def login(self, username: str, password: str):
        self.page.get_by_role("link", name="Войти").click()
        self.page.get_by_role("textbox", name="Имя пользователя или почта *").fill(username)
        self.page.get_by_role("textbox", name="Пароль *").fill(password)
        self.page.get_by_role("button", name="Войти").click()