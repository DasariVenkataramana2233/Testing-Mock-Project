import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture(scope='class')
def test_invocation(request):

    serv_obj = Service()
    driver = webdriver.Chrome(service=serv_obj)
    driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.minimize_window()
    driver.close()

