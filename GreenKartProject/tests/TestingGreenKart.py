import time
from lib2to3.pgen2 import driver

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.HomePageObjects import HomePage
from pageobjects.OrdersPageObjects import Orders
from utilities.BaseUtility import BaseClass


class Test_Greenkart(BaseClass):

    def test_home(self):

        self.driver.implicitly_wait(5)

        home = HomePage(self.driver)
        home.input_to_searcbox().send_keys('c')
        time.sleep(2)
        elements = home.elements_in_home()
        for element in elements:
            if element.find_element(By.XPATH, "//button[text()='ADD TO CART']").text == 'ADD TO CART':
                element.click()

        home.cart_clicking().click()
        home.clickon_checkOut().click()
        self.driver.execute_script('window.scrollBy(0,document.body.scrollHeight);')
        order = Orders(self.driver)
        order.applying_promo()
        self.driver.find_element(By.XPATH, "//button[text()='Apply']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(order.promoInfo))
        order.order_placing().click()
        # order.click_dropdown()
        # order.agreeing()
        # order.click_procced().click()








