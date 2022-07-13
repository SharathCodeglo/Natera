from pageObjects.SignateraImageModule import SignateraForPatients
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_011_ForPatients:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_Links(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.patients = SignateraForPatients(self.driver)
        self.patients.clickForPatients()
        self.patients.checkScheduleSession()
        self.patients.checkScheduleBloodDraw()
