import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Добавление пиццы в корзину")
@allure.story("Добавление пиццы '4 в 1' и 'Как у бабушки'")
def test_add_pizza_to_cart(driver):
    with allure.step("Открыть сайт пиццерии"):
        driver.get("https://pizzeria.skillbox.cc/")

    with allure.step("Авторизоваться"):
        driver.find_element(By.LINK_TEXT, "Войти").click()
        driver.find_element(By.NAME, "username").send_keys("igor")
        driver.find_element(By.NAME, "password").send_keys("igor123")
        driver.find_element(By.NAME, "login").click()

    with allure.step("Добавить пиццу '4 в 1' в корзину"):
        driver.find_element(By.LINK_TEXT, "Add “Пицца \"4 в 1\"” to your").click()

    with allure.step("Добавить пиццу 'Как у бабушки' в корзину"):
        driver.find_element(By.LINK_TEXT, "Add “Пицца \"Как у бабушки\"”").click()

    with allure.step("Перейти в корзину и проверить наличие пицц"):
        driver.find_element(By.LINK_TEXT, "Подробнее").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "cart-item")
        assert len(cart_items) == 2, "Не все пиццы добавлены в корзину"