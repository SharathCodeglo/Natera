import time
from pageObjects.NavigateSignatera import Nav_Signatera
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_002_NavigateToSignatera:
    url = read_config.get_url()
    logger = LogGen.loggen()

    def test_nav_signatera(self, setup):
        self.logger.info("********** Verifying Navigation of the page to Signatera **********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(10)
        self.sign = Nav_Signatera(self.driver)
        self.sign.select_signatera()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Signatera – Circulating Tumor DNA Blood Test | Natera":
            assert True
            self.driver.close()
            self.logger.info("********** Title of Signatera page test is Passed **********")
        else:
            # self.driver.save_screenshot(".\\Screenshots\\", "test_HomePageTitle.png")
            self.logger.info("********** Title of Signatera page test is Failed **********")
            self.driver.close()
            assert False

