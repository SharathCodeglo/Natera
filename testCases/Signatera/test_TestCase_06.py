import time
from pageObjects.SignateraPatientInfo import AnimeFrames
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_006_AnimeFrames:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_Frames(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        time.sleep(3)

        self.frames = AnimeFrames(self.driver)
        self.frames.click_PatientInfo()
        self.frames.clickAnimeBlog_1()
        self.frames.clickAnimeBlog_2()
        self.frames.clickAnimeBlog_3()
        self.frames.clickAnimeBlog_4()
        self.frames.clickAnimeBlog_5()
        self.frames.clickAnimeBlog_6()
        time.sleep(2)
        self.driver.close()


