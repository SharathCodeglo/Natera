import time
from pageObjects.SignateraClinicianInfo import ViewPresentation
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_009_PresentationForm:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_presentation(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.form = ViewPresentation(self.driver)
        self.form.click_ClinicianInfo()
        self.form.click_presentation()
        self.form.setFirstname("Sharath")
        self.form.setLastname("Kumar")
        self.form.setEmail("abcdef@gmail.com")
        self.form.setCompanyName("codeglo")
        self.form.setPostalcode("100211")
        self.form.setCountry()
        self.form.clickRadioButton("no")
        self.form.clickClose()
        self.logger.info("****** Details are successfully filled ******")
        time.sleep(2)
        self.driver.close()

