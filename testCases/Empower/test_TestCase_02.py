import time
from pageObjects.EmpowerOverview import Scroll
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_002_Scroll:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_scroll(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(2)

        self.scroll = Scroll(self.driver)
        self.scroll.Scroll_ByElement()
        self.scroll.Scroll_toBottom()
        self.scroll.Scroll_toTop()
        self.driver.close()
