import time

from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self, setup):
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
        time.sleep(5)

        #act_title = self.driver.title

        # if act_title == "Home - Evernote11":
        #     assert True
        #     #self.driver.close()
        # else:
        #     self.driver.save_screenshot(".//Screenshot/" + "evernote001_png")
        #     #self.driver.close()
        #     assert False

        // div[ @



