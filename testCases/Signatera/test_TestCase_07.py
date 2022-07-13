import time
from pageObjects.SignateraPatientInfo import Feedback
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_007_FeedbackForm:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_form(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        time.sleep(3)

        self.form = Feedback(self.driver)
        self.form.click_PatientInfo()
        self.form.setFirstname("Sharath")
        self.form.setLastname("Kumar")
        self.form.setEmail("abcdef@gmail.com")
        self.form.setPhone("4785485965")
        self.form.setPostalcode("100211")
        self.form.setCountry()
        self.form.clickRadioButton("no")
        self.form.setComments("Testing purpose.....")
        self.logger.info("****** Details are successfully filled ******")
        time.sleep(3)
        self.driver.close()

