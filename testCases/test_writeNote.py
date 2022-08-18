import time

from pageObjects.LoginPage import LoginPage
from pageObjects.WriteNote import CreateNote
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# logout = lgo
# LoginPage = lp


class Test_001_writeNote:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    title = ReadConfig.getTitle()
    message = ReadConfig.getMessage()

    def test_writeNote(self, setup):
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
        act_title = self.driver.title
        assert act_title == "Home - Evernote"
        if act_title == "Home - Evernote":
            time.sleep(10)
            self.lp.clickAddNote()
        else:
            self.driver.close()
        self.wn = CreateNote(self.driver)
        time.sleep(20)
        self.wn.selectIframe()
        #time.sleep(10)

        self.wn.setTitle()
        self.wn.setMessage(self.message)
        self.driver.switch_to.default_content()
        self.lgo = CreateNote(self.driver)
        self.lgo.btnAccountLogout()
        self.lgo.btnLogout()
        time.sleep(5)
        self.lgo.btnExit()











