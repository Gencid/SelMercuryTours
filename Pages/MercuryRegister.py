from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Register:
    def __init__(self, mercurydriver):
        self.driver = mercurydriver
        self.signon_link = (By.LINK_TEXT, "SIGN-ON")
        self.register_link = (By.LINK_TEXT, "REGISTER")
        self.lastname_box = (By.NAME, "lastName")
        self.firstname_box = (By.NAME, "firstName")
        self.phone_box = (By.NAME, "phone")
        self.email_box = (By.ID, "userName")
        self.address_box1 = (By.NAME, "address1")
        self.address_box2 = (By.NAME, "address2")
        self.city_box = (By.NAME, "city")
        self.state_box = (By.NAME, "state")
        self.postcode_box = (By.NAME, "postalCode")
        self.country_dropdown = (By.NAME, "country")
        self.username_box = (By.ID, "email")
        self.password_box = (By.NAME, "password")
        self.confirmpass_box = (By.NAME, "confirmPassword")
        self.submit_button = (By.NAME, "register")

    def contact_info(self, firstname, lastname, phone, email):
        self.driver.find_element(*self.lastname_box).send_keys(lastname)
        self.driver.find_element(*self.firstname_box).send_keys(firstname)
        self.driver.find_element(*self.phone_box).send_keys(phone)
        self.driver.find_element(*self.email_box).send_keys(email)

    def mailing_info(self, address1, address2, city, state, postcode, country):
        self.driver.find_element(*self.address_box1).send_keys(address1)
        self.driver.find_element(*self.address_box2).send_keys(address2)
        self.driver.find_element(*self.city_box).send_keys(city)
        self.driver.find_element(*self.state_box).send_keys(state)
        self.driver.find_element(*self.postcode_box).send_keys(postcode)
        Select(self.driver.find_element(*self.country_dropdown)).select_by_index(country)

    def user_info(self, username, password):
        self.driver.find_element(*self.username_box).send_keys(username)
        self.driver.find_element(*self.password_box).send_keys(password)
        self.driver.find_element(*self.confirmpass_box).send_keys(password)

    def go_submit(self):
        self.driver.find_element(*self.submit_button).click()
