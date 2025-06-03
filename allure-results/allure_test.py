import pytest
import allure

@allure.feature("Оформление заказа")
@allure.story("Добавление пиццы в корзину и оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_order_pizza():
    with allure.step("Открыть сайт пиццерии"):
        # Открытие сайта
        pass

    with allure.step("Авторизоваться"):
        # Авторизация
        pass

    with allure.step("Добавить пиццу в корзину"):
        # Добавление пиццы
        pass

    with allure.step("Оформить заказ"):
        # Оформление заказа
        pass