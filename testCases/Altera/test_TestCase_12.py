import time
from pageObjects.AlteraFAQ import FAQ_Billing
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_012_FAQ_Billing:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_billing(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(3)

        self.faq = FAQ_Billing(self.driver)
        self.faq.clickFAQ()
        self.faq.faq_Billing()
        self.driver.close()

