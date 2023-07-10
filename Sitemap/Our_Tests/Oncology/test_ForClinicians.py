import time
from SitemapObjects.OurTests.Oncology.ForClinicians import ForClinicians
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
        self.clinicians.Nav_Signatera_for_Colorectal_Cancer()
        self.clinicians.Nav_Signatera_for_Bladder_Cancer()
        self.clinicians.Nav_Signatera_for_Immunotherapy_Monitoring()
        self.clinicians.Nav_Signatera_Research_Pipeline()
        self.clinicians.Nav_Oncology_Portal()
        self.driver.quit()
