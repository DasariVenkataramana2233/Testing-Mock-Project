from selenium.webdriver.common.by import By


class HomePage:

    input = (By.CSS_SELECTOR, '.search-keyword')
    elements = (By.XPATH, "//button[text()='ADD TO CART']")
    cart_go = (By.CLASS_NAME, 'cart-icon')
    checkOut = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):

        self.driver = driver

    def input_to_searcbox(self):

        return self.driver.find_element(*HomePage.input)

    def elements_in_home(self):

        return self.driver.find_elements(*HomePage.elements)

    def cart_clicking(self):

        return self.driver.find_element(*HomePage.cart_go)

    def clickon_checkOut(self):

        return self.driver.find_element(*HomePage.checkOut)

