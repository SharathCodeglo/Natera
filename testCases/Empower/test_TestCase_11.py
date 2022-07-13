import time
from pageObjects.EmpowerClinicians import Sliders
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_008_Sliders:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_sliders(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)