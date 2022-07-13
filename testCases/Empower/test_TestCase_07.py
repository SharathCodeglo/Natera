import time
from pageObjects.EmpowerPatientInfo import KnowYourRisk
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_007_KnowYourRisk:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_innerlinks(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.links = KnowYourRisk(self.driver)
        self.links.patient_info()
        self.links.check_links()
        self.driver.quit()

