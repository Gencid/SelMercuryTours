from selenium import webdriver
from Pages.MercuryWelcome import *
from Pages.MercuryRegister import *
from Pages.CreateAccountSuccess import *
from Pages.MercurySignOn import *
from Mer_Data import *

import unittest


class MerToursTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r"geckodriver.exe")
        self.driver.get("http://newtours.demoaut.com/mercurywelcome.php")
        self.welcome = Welcome(self.driver)
        self.register = Register(self.driver)
        self.success = Success(self.driver)
        self.signon = SignOn(self.driver)

    def test_index_login(self):
        self.welcome.welcome_login(d_username, d_password)
        self.driver.implicitly_wait(3)
        self.welcome.welcome_go_register()

    def test_register(self):
        self.welcome.welcome_go_register()
        self.register.contact_info(d_name, d_lastname, d_phone, d_email)
        self.register.mailing_info(d_dir1, d_dir2, d_city, d_state, d_postcode, d_country)
        self.register.user_info(d_username, d_password)
        self.register.go_submit()
        self.success.go_sign_in()
        self.signon.signon_login(d_username, d_password)

    def tearDown(self):
        self.driver.quit()
