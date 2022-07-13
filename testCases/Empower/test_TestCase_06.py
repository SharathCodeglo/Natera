import time
from pageObjects.EmpowerOverview import Feedback_Empower
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_006_Feedback_empower:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_feedback(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.feed = Feedback_Empower(self.driver)
        self.feed.clickOverview()
        self.feed.setFirstname("Ravi")
        self.feed.setLastname("Kumar")
        self.feed.setEmail("qwerty@gmail.com")
        self.feed.setPostalcode("900321")
        self.feed.setPhone("4578954521")
        self.feed.setCountry()
        self.feed.clickRadioButton("yes")
        self.feed.clickComments("Testing Purpose.........")
        self.feed.contact_us()
        time.sleep(2)
        self.driver.close()

