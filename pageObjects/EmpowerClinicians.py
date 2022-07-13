import time
from selenium.webdriver.common.by import By


class Empower_Gene_Table_Download:
    clinicianinfo_XPATH = "(//a[normalize-space()='Clinician Information'])[1]"
    empower_gene_table_XPATH = "//a[normalize-space()='Empower gene table with cancer risks']"
    download_table_XPATH = "//a[normalize-space()='Download Table']"

    def __init__(self, driver):
        self.driver = driver

    def clinician_info(self):
        self.driver.find_element(By.XPATH, self.clinicianinfo_XPATH).click()
        time.sleep(2)

    def empower_gene_table_download(self):
        self.driver.find_element(By.XPATH, self.empower_gene_table_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.download_table_XPATH).click()
        time.sleep(2)
        self.driver.back()

# class FilterAndSearch_table:
