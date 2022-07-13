import time

from pageObjects.AlteraFAQ import FAQ_Overview
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_009_FAQ_Overview:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_overview(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(3)

        self.faq = FAQ_Overview(self.driver)
        self.faq.clickFAQ()
        self.faq.faq_Overview()
        self.driver.close()

