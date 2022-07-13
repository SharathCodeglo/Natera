import time
from pageObjects.SignateraFAQ import FAQ_ResultsAndReports
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_016_FaqResultsAndReports:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_faqResults(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.faq = FAQ_ResultsAndReports(self.driver)
        self.faq.faq_ResultsAndReports()
        self.driver.close()

