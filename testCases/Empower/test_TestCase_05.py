import time
from pageObjects.EmpowerOverview import AnimeFrame
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_005_Frames:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_feedback(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.frame = AnimeFrame(self.driver)
        self.frame.clickOverview()
        self.frame.frames()
        self.driver.close()
