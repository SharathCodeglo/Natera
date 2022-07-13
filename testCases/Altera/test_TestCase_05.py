import time
from pageObjects.AlteraOverview import Flipbook_LearnMore
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_005_Flipbook:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_flipbook(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(2)

        self.flipbook = Flipbook_LearnMore(self.driver)
        self.flipbook.learnmore()
        self.flipbook.flipbooks()
        self.driver.close()

