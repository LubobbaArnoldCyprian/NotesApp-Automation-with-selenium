import time

from pageObjects.LoginPage import LoginPage
from pageObjects.OpenNote import OpenNote
from pageObjects.WriteNote import CreateNote
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# LoginPage = lp
class Test_003_openNote:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    title = ReadConfig.getTitle()
    message = ReadConfig.getMessage()

    def test_openNote(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginDashboard()
        self.lp.setUserName(self.username)
        self.lp.btnContinue()
        time.sleep(5)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(30)
        self.driver = setup
        self.op = OpenNote(self.driver)
        time.sleep(5)
        self.op.openNotes()
        time.sleep(5)
        self.op.clickSpecificNote()
        time.sleep(5)































