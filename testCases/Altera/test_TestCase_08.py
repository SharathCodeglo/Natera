import time
from pageObjects.AlteraOverview import Feedback
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_008_Feedback:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_feedback(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(2)

        self.feed = Feedback(self.driver)
        self.feed.clickOverview()
        self.feed.setFirstname("Ravi")
        self.feed.setLastname("Kumar")
        self.feed.setEmail("asdf@gmail.com")
        self.feed.setPostalcode("100321")
        self.feed.setCompanyName("Codeglo")
        self.feed.setPhone("9876545678")
        self.feed.setCountry()
        self.feed.clickRadioButton("yes")
        self.feed.setComments("Testing Purpose........")
        self.driver.close()
