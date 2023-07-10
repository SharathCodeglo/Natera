# Women's Health
import time
from SitemapObjects.OurTests.Womens_Health.ForPatients import ForPatients
from Utilities.readProperties import read_config


class Test_ForPatients:
    url = read_config.get_url()

    def test_pat(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.patients = ForPatients(self.driver)
        self.patients.Nav_sitemap()
        self.patients.Nav_Pricing_and_Billing_Information()
        self.patients.Nav_Womens_Health_Portal()
        self.driver.quit()
