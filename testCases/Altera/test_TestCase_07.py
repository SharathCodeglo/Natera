import time
from pageObjects.AlteraOverview import ReadMore_learnmore
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_007_Readmore_learnmore:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_readmore_learnmore(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(2)

        self.read = ReadMore_learnmore(self.driver)
        self.read.learnmore1()
        self.read.readmore()
        self.read.learnmore2()
        self.read.downloadstudy()
        self.driver.close()

