from pageObjects.SignateraImageModule import SignateraForClinicians
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_012_ForClinicians:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_Link(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.clinicians = SignateraForClinicians(self.driver)
        self.clinicians.clickForClinicians()
        self.clinicians.checkScheduleSession()
        self.clinicians.checkLoginOncology()

