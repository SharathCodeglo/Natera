import time
from pageObjects.NavigateToEmpower import Nav_Empower
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_001_NavigateToEmpower:
    url = read_config.get_url()
    logger = LogGen.loggen()

    def test_nav_empower(self, setup):
        self.logger.info("********** Verifying Navigation of the page to Empower **********")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(10)

        self.sign = Nav_Empower(self.driver)
        self.sign.select_empower()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Empower Overview | Empower Overview| Natera":
            assert True
            self.driver.close()
            self.logger.info("********** Title of Empower page test is Passed **********")
        else:
            # self.driver.save_screenshot(".\\Screenshots\\", "test_HomePageTitle.png")
            self.logger.info("********** Title of Empower page test is Failed **********")
            self.driver.close()
            assert False

