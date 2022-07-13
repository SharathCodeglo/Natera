import time
from pageObjects.AlteraFAQ import FAQ_OrderingAndLogistics
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_010_FAQ_OrderAndLogistics:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_order(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(3)

        self.faq = FAQ_OrderingAndLogistics(self.driver)
        self.faq.clickFAQ()
        self.faq.faq_OrderAndLogist()
        self.driver.close()

