from selenium.webdriver.common.by import By


class Welcome:
    def __init__(self, mercurydriver):  # Define mydriver and find all important links and boxes
        self.driver = mercurydriver
        self.signon_link = (By.LINK_TEXT, "SIGN-ON")
        self.register_link = (By.LINK_TEXT, "REGISTER")
        self.username_box = (By.NAME, "userName")
        self.password_box = (By.NAME, "password")
        self.signin_button = (By.NAME, "login")

    def welcome_login(self, wel_log_user, wel_log_pass):
        self.driver.find_element(*self.username_box).send_keys(wel_log_user)
        self.driver.find_element(*self.password_box).send_keys(wel_log_pass)
        self.driver.find_element(*self.signin_button).click()

    def welcome_go_register(self):
        self.driver.find_element(*self.register_link).click()
