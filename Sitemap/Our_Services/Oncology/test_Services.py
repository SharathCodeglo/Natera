import time
from SitemapObjects.OurServices.Oncology.Services import Services
from Utilities.readProperties import read_config


class Test_Services:
    url = read_config.get_url()

    def test_Services(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.service = Services(self.driver)
        self.service.Nav_sitemap()
        self.service.Nav_NateraCore_Services()
        self.service.Nav_Pharma_Partnership()
        self.driver.quit()
