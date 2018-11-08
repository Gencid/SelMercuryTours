from selenium import webdriver
from Pages.MercuryWelcome import *
from Pages.MercuryRegister import *
from Pages.CreateAccountSuccess import *
from Pages.MercurySignOn import *

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
        self.welcome.welcome_login("Usuario", "contraseña")
        self.welcome.welcome_go_register()

    def test_register(self):
        self.welcome.welcome_go_register()
        self.register.contact_info("Fulanito", "de Tal", "555 55 55", "prueba@testing.com")
        self.register.mailing_info("251 Something Street", "Apartment T, Second Floor",
                                   "Testville", "Testington", "73575", 23)
        self.register.user_info("Usuario", "contraseña")
        self.register.go_submit()
        self.success.go_sign_in()
        self.signon.signon_login("Usuario", "contraseña")

    def tearDown(self):
        self.driver.quit()
