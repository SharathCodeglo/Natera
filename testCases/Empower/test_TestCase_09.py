import time
from pageObjects.EmpowerClinicians import Empower_Gene_Table_Download
from Utilities.readProperties import read_config
from Utilities.customLogger import LogGen


class Test_009_Download_gene_table:
    url = read_config.get_EmpowerURL()
    logger = LogGen.loggen()

    def test_download_table(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.implicitly_wait(15)

        self.table = Empower_Gene_Table_Download(self.driver)
        self.table.clinician_info()
        self.table.empower_gene_table_download()
        self.driver.close()

