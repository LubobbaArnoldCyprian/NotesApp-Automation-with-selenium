from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage:
    textbox_username_id = "username"
    button_username_xpath = "//input[@value='Continue']"
    textbox_password_id = "password"
    button_login_id = "loginButton"
    button_loginDashboard_xpath = "//nav[@aria-label='Utility navigation']//a[normalize-space()='Log In']"
    button_addNote_xpath = "//*[name()='circle' and contains(@cx,'12')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):

        login_username_field = self.driver.find_element(By.ID, self.textbox_username_id)
        login_username_field.clear()
        login_username_field.send_keys(username)

    def btnContinue(self):
        self.driver.find_element(By.XPATH, self.button_username_xpath).click()

    def setPassword(self, password):

        login_password_field = self.driver.find_element(By.ID, self.textbox_password_id)
        login_password_field.clear()
        login_password_field.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def clickLoginDashboard(self):
        self.driver.find_element(By.XPATH, self.button_loginDashboard_xpath).click()

    def clickAddNote(self):
        self.driver.find_element(By.XPATH, self.button_addNote_xpath).click()
        #self.driver.find_element(By.XPATH, self.button_addNote_xpath).click()










