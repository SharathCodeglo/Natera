import time
from SitemapObjects.OurTests.Oncology.Tests import Tests
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
        self.tests.Nav_signatera()
        self.tests.Nav_altera()
        self.tests.Nav_empower()
        self.driver.close()
