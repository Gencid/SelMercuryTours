from selenium.webdriver.common.by import By


class SignOn:
    def __init__(self, mercurydriver):
        self.driver = mercurydriver
        self.username_box = (By.NAME, "userName")
        self.password_box = (By.NAME, "password")
        self.submit_link = (By.NAME, "login")

    def signon_login(self, signon_user, signon_pass):
        self.driver.find_element(*self.username_box).send_keys(signon_user)
        self.driver.find_element(*self.password_box).send_keys(signon_pass)
        self.driver.find_element(*self.submit_link).click()
