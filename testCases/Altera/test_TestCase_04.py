import time
from pageObjects.AlteraOverview import LearnMore
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_004_LearnMore:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_learnmore(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(2)

        self.learn = LearnMore(self.driver)
        self.learn.learnmore()
        self.driver.close()

