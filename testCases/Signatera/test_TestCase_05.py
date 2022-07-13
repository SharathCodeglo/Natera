from pageObjects.SignateraOverview import Feedback
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_005_Feedbackform:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_feedback(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logger.info("****** Successfully Launched Signatera Page ******")

        self.feed = Feedback(self.driver)
        self.feed.setFirstname("Sharath")
        self.feed.setLastname("Kumar")
        self.feed.setEmail("abcdef@gmail.com")
        self.feed.setCompanyName("codeglo")
        self.feed.setPhone("4785485965")
        self.feed.setPostalcode("100211")
        self.feed.setCountry()
        self.feed.clickRadioButton("no")
        self.feed.setComments("Testing purpose.....")
        self.logger.info("****** Details are successfully filled ******")

