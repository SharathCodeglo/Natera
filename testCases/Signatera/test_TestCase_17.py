import time

from pageObjects.SignateraFAQ import FAQ_OrderingAndLogistics
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_017_FaqOrderingAndLogistics:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_faqOrderAndLogist(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.faq = FAQ_OrderingAndLogistics(self.driver)
        self.faq.faq_OrderAndLogist()
        self.driver.close()

