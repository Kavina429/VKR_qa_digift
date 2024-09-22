from playwright.sync_api import Page
from step import *

@pytest.mark.smoke_market  # проверка загрузки страницы
def test_login_successful(page: Page, login):
    """Проверка входа"""
    username = "HR"  # Подставьте ваше значение
    password = "test"  # Подставьте ваше значение
    login(username, password)

@pytest.mark.smoke_market  # проверка загрузки страницы
def test_end_to_end_1_successful(page: Page, login, end_to_end_1):
    """Проверка входа"""
    username = "HR"  # Подставьте ваше значение
    password = "test"  # Подставьте ваше значение
    login(username, password)
    page.wait_for_timeout(1000)
    """Проверка загрузки собственного изображения для карты"""
    end_to_end_1()

@pytest.mark.smoke_market  # проверка загрузки страницы
def test_end_to_end_2_successful(page: Page, login, end_to_end_2):
    """Проверка входа"""
    username = "HR"  # Подставьте ваше значение
    password = "test"  # Подставьте ваше значение
    login(username, password)
    page.wait_for_timeout(1000)
    """Проверка загрузки собственного изображения для карты"""
    end_to_end_2()

@pytest.mark.smoke_market  # проверка загрузки страницы
def test_end_to_end_3_successful(page: Page, login, end_to_end_3):
    """Проверка входа"""
    username = "HR"  # Подставьте ваше значение
    password = "test"  # Подставьте ваше значение
    login(username, password)
    page.wait_for_timeout(1000)
    """Проверка загрузки собственного изображения для карты"""
    end_to_end_3()

