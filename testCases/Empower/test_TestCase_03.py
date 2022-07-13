import time
from pageObjects.EmpowerOverview import Learnmore
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_003_Learnmore:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_learnmore(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.learn = Learnmore(self.driver)
        self.learn.clickOverview()
        self.learn.learnmore()
        self.driver.close()
