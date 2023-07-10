import time
from SitemapObjects.OurServices.Oncology.ForClinicians import ForClinicians
from Utilities.readProperties import read_config


class Test_ForPatients:
    url = read_config.get_url()

    def test_pat(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(2)

        self.clinicians = ForClinicians(self.driver)
        self.clinicians.Nav_sitemap()
        self.clinicians.Nav_Oncology_Portal()
        self.clinicians.Nav_Order_a_Test_Kit()
        self.clinicians.Nav_Contact_Us()
        self.driver.quit()
