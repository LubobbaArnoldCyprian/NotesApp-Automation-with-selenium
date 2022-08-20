from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.keys import Keys


class CreateNote:

    textbox_title_xpath = "(//textarea[@placeholder='Title'])[1]"
    iframe_id = "qa-COMM_ENGINE_IFRAME"
    iframe_xpath = "//iframe[@id='qa-COMMON_EDITOR_IFRAME']"
    textbox_message_xpath = "//en-note[@aria-label='Note Content']"
    button_accountLogout_xpath = "//div[@id='qa-USER_PORTRAIT']"   #doubt
    button_logout_id = "qa-ACCOUNT_DROPDOWN_LOGOUT"
    button_confirmExit_iq = "qa-LOGOUT_CONFIRM_DIALOG_SUBMIT"
    #note_tabs_id = "react-tabs-15"

    def __init__(self, driver):
        self.driver = driver

    def setTitle(self,title):
        note_title_field = self.driver.find_element(By.XPATH, self.textbox_title_xpath)
        note_title_field.click()
        note_title_field.clear()
        note_title_field.send_keys(title)
        note_title_field.send_keys(Keys.RETURN)

    def setMessage(self, message):
        message_title_field = self.driver.find_element(By.XPATH, self.textbox_message_xpath)
        #message_title_field.click()
        message_title_field.clear()
        message_title_field.send_keys(message)

    def btnAccountLogout(self):
        self.driver.find_element(By.XPATH, self.button_accountLogout_xpath).click()

    def btnLogout(self):
        self.driver.find_element(By.ID, self.button_logout_id).click()

    def selectIframe(self):
        frame2 = self.driver.find_element(By.XPATH, self.iframe_xpath)
        self.driver.switch_to.frame(frame2)

    def btnExit(self):
        self.driver.find_element(By.ID, self.button_confirmExit_iq).click()













