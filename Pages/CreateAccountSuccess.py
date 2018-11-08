from selenium.webdriver.common.by import By


class Success:
    def __init__(self, mercurydriver):
        self.driver = mercurydriver
        self.signin_link = (By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/"
                                      "tr/td[2]/table/tbody/tr[3]/td/p[2]/font/a[1]")

    def go_sign_in(self):
        self.driver.find_element(*self.signin_link).click()