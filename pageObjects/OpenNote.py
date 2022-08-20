from selenium.webdriver.common.by import By
from selenium import webdriver
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.keys import Keys


class OpenNote:
    button_AllNotes_xpath = "//a[@id='qa-NAV_ALL_NOTES']"
    clickNote_xpath = "//span[contains(text(),'This is an ever note test note')]"

    def __init__(self, driver):
        self.driver = driver

    def openNotes(self):
        self.driver.find_element(By.XPATH, self.button_AllNotes_xpath).click()

    def clickSpecificNote(self):
        self.driver.find_element(By.XPATH, self.clickNote_xpath).click()




