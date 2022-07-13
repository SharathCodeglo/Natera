from pageObjects.SignateraImageModule import SignateraForPatients
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_013_ForPatients:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_Links(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.patients = SignateraForPatients(self.driver)
        self.patients.clickForPatients()
        self.patients.clickPriceAndBill()
        self.patients.NewWindow()
        self.patients.setFirstname("Sharath")
        self.patients.setLastname("Kumar")
        self.patients.setEmail("abcdef@gmail.com")
        self.patients.setPhone("4785485965")
        self.patients.setPostalcode("100211")
        self.patients.setCountry()
        self.patients.clickRadioButton("no")
        self.patients.setComments("Testing purpose.....")
        self.logger.info("****** Details are successfully filled ******")

