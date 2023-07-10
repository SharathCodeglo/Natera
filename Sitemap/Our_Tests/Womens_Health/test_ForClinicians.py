# Women's Health
import time
from SitemapObjects.OurTests.Womens_Health.ForClinicians import ForClinicians
from Utilities.readProperties import read_config


class Test_ForClinicians:
    url = read_config.get_url()

    def test_cli(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.clinicians = ForClinicians(self.driver)
        self.clinicians.Nav_sitemap()
        self.clinicians.Nav_NateraConnect_Provider_Portal()
        self.clinicians.Nav_Horizon_Conditions_List()
        self.clinicians.Nav_NEVA_for_Empower()
        self.driver.quit()
