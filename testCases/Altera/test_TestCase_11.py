import time
from pageObjects.AlteraFAQ import FAQ_ResultsAndReports
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_011_FAQ_ResultsAndReports:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_resultsandreports(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(3)

        self.faq = FAQ_ResultsAndReports(self.driver)
        self.faq.clickFAQ()
        self.faq.faq_ResultAndReports()
        self.driver.close()

