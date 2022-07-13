from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_001_ValidateHomepage:
    url = read_config.get_url()
    logger = LogGen.loggen()

    def test_HomePageTitle(self, setup):
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying HomePage Title **********")
        self.driver = setup
        self.driver.get(self.url)
        setup.implicitly_wait(10)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Natera: A global leader in cfDNA testing":
            self.logger.info("********** HomePage Title test is Passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_HomePageTitle.png")
            self.logger.info("********** HomePage Title test is Failed **********")
            self.driver.close()
            assert False

