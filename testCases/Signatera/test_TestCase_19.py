import time
from pageObjects.SignateraFAQ import FAQ_CustomerExp
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_019_FaqCustomerExp:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_faqCustomerExp(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.faq = FAQ_CustomerExp(self.driver)
        self.faq.faq_CustomerExp()
        self.driver.close()

