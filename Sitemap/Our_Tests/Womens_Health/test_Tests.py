# Women's Health
import time
from SitemapObjects.OurTests.Womens_Health.Tests import Tests
from Utilities.readProperties import read_config


class Test_Tests:
    url = read_config.get_url()

    def test_Tests(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.tests = Tests(self.driver)
        self.tests.Nav_sitemap()
        self.tests.Nav_Horizon_Advanced_Carrier_Screening()
        self.tests.Nav_Panorama_Non_Invas()
        self.tests.Nav_Empower_Hereditary_Cancer_Test()
        self.tests.Nav_Vistara_Single_Gene_NIPT()
        self.tests.Nav_Anora_Miscarriage_Test()
        self.tests.Nav_Spectrum_Preimplantation_Genetics()
        self.tests.Nav_Vasistera_Limited()
        self.driver.quit()
