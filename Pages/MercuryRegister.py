from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Register:
    def __init__(self, mercurydriver):
        self.driver = mercurydriver
        self.signon_link = (By.LINK_TEXT, "SIGN-ON")
        self.register_link = (By.LINK_TEXT, "REGISTER")
        self.firstname_box = (By.NAME, "firstName")
        self.address_box1 = (By.NAME, "address1")
        self.country_dropdown = (By.NAME, "country")
        self.username_box = (By.ID, "email")
        self.submit_button = (By.NAME, "register")

    def contact_info(self, firstname, lastname, phone, email):
        self.driver.find_element(*self.firstname_box)\
            .send_keys(firstname+Keys.TAB+lastname+Keys.TAB+phone+Keys.TAB+email)

    def mailing_info(self, address1, address2, city, state, postcode, country):
        self.driver.find_element(*self.address_box1)\
            .send_keys(address1+Keys.TAB+address2+Keys.TAB+city+Keys.TAB+state+Keys.TAB+postcode)
        Select(self.driver.find_element(*self.country_dropdown)).select_by_index(country)

    def user_info(self, username, password):
        self.driver.find_element(*self.username_box)\
            .send_keys(username+Keys.TAB+password+Keys.TAB+password)

    def go_submit(self):
        self.driver.find_element(*self.submit_button).click()
