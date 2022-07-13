import time
from pageObjects.AlteraOverview import InnerLink
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_003_InnerLinks:
    url = read_config.get_AlteraURL()
    logger = LogGen.loggen()

    def test_links(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.links = InnerLink(self.driver)
        self.links.clickListOfGenes()
        self.links.downloadListOfGenes()
        self.driver.close()

