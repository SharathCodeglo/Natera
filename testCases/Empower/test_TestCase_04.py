import time
from pageObjects.EmpowerOverview import Feedback_learnmore
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_004_Feedback_learnmore:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_feedback(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.feed = Feedback_learnmore(self.driver)
        self.feed.clickOverview()
        self.feed.learnmore()
        self.feed.setFirstname("Ravi")
        self.feed.setLastname("Kumar")
        self.feed.setEmail("qwerty@gmail.com")
        self.feed.setPostalcode("900321")
        self.feed.setPhone("4578954521")
        self.feed.setCountry()
        self.feed.clickRadioButton("yes")
        time.sleep(2)
        self.driver.close()
