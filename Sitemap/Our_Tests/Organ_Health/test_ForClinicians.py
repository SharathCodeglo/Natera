# Organ Health
import time
from SitemapObjects.OurTests.Organ_Health.ForClinicians import ForClinicians
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
        self.clinicians.Nav_Prospera_for_Kidney_Clinician()
        self.clinicians.Nav_Renasight_Clinician_Information()
        self.clinicians.Nav_Renasight_Gene_Conditions_List()
        self.clinicians.Nav_Organ_Health_Portal()
        self.driver.quit()
