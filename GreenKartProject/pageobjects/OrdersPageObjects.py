from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Orders:

    promocode = (By.CSS_SELECTOR, ".promoCode")
    promoInfo = (By.CLASS_NAME, 'promoInfo')
    placeorder = (By.XPATH, "//button[text()='Place Order']")
    dropdown = (By.TAG_NAME, "select")
    agree = (By.CSS_SELECTOR, ".chkAgree")
    procced = (By.XPATH, "//button[text()='Proceed']")

    def __init__(self, driver):

        self.driver = driver

    def applying_promo(self):

        return self.driver.find_element(*Orders.promocode).send_keys('rahulshettyacademy')

    def info_promo(self):

        return self.driver.find_element(Orders.promoInfo).text

    def order_placing(self):

        return self.driver.find_element(*Orders.placeorder)

    def click_dropdown(self):

        drop = Select(self.driver.find_element(*Orders.dropdown))
        return drop.select_by_value('india')

    def agreeing(self):

        return self.driver.find_element(*Orders.agree)

    def click_procced(self):

        return self.driver.find_element(*Orders.procced)


