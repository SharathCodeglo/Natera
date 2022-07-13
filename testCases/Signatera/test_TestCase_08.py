import time
from pageObjects.SignateraClinicianInfo import AnimeFrames
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_008_AnimeFrame:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_Frame(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.frame = AnimeFrames(self.driver)
        self.frame.click_ClinicianInfo()
        self.frame.clickAnimeBlog_1()
        self.frame.clickAnimeBlog_2()
        self.frame.clickAnimeBlog_3()
        time.sleep(2)
        self.driver.close()

