import time
from pageObjects.EmpowerPatientInfo import AnimeFrames
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_008_AnimmeFrame:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_animeframe(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.anime = AnimeFrames(self.driver)
        self.anime.patient_info()
        self.anime.frame1()
        self.anime.frame2()
        self.anime.frame3()
        self.driver.close()

