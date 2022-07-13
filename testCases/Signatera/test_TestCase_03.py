import time
from pageObjects.SignateraOverview import Scroll
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_003_Scroll:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_scroll(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(4)

        self.scrolling = Scroll(self.driver)
        self.scrolling.Scroll_ByElement()
        time.sleep(2)
        self.scrolling.Scroll_toBottom()
        time.sleep(2)
        self.scrolling.Scroll_toTop()
        time.sleep(2)
        self.driver.close()

