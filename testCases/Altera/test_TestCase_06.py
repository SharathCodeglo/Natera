import time
from pageObjects.AlteraOverview import ReadInspirePublication_LearnMore
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_006_ReadPublication:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_downloadRIP(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(2)

        self.rip = ReadInspirePublication_LearnMore(self.driver)
        self.rip.learnmore()
        self.rip.clickRIP()
        self.rip.setFirstname("Munish")
        self.rip.setLastname("Kanth")
        self.rip.setEmail("qwerty@gmail.com")
        self.rip.setPostalcode("233980")
        self.rip.setCompanyName("Codeglo")
        self.rip.setCountry()
        self.rip.clickRadioButton("no")
        self.rip.download()
        self.driver.close()

