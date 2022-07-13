import time
from pageObjects.NavigateAltera import Nav_Altera
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_001_NavigateToAltera:
    url = read_config.get_url()
    logger = LogGen.loggen()

    def test_nav_altera(self, setup):
        self.logger.info("********** Verifying Navigation of the page to Altera **********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(10)
        self.sign = Nav_Altera(self.driver)
        self.sign.select_altera()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Altera | Natera":
            assert True
            self.driver.close()
            self.logger.info("********** Title of Altera page test is Passed **********")
        else:
            # self.driver.save_screenshot(".\\Screenshots\\", "test_HomePageTitle.png")
            self.logger.info("********** Title of Altera page test is Failed **********")
            self.driver.close()
            assert False

