import time
from pageObjects.SignateraOverview import AnimatedBlogs
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_004_AnimeBlogs:
    url = read_config.get_signURL()
    logger = LogGen.loggen()

    def test_blogs(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.implicitly_wait(10)
        self.logger.info("****** Successfully Launched Signatera Page ******")

        self.AB = AnimatedBlogs(self.driver)
        self.AB.clickAnimeBlog_1()
        time.sleep(3)
        self.AB.clickAnimeBlog_2()
        time.sleep(3)
        self.AB.clickAnimeBlog_3()
        time.sleep(3)
        self.driver.close()

