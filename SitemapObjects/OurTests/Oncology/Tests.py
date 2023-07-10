import time
from selenium.webdriver.common.by import By


class Tests:
    sitemap = "//a[normalize-space()='Sitemap']"
    signatera = "//a[contains(text(),'Signatera – Residual Disease Test (MRD)')]"
    altera = "//a[contains(text(),'Altera – Tumor Genomic profile')]"
    empower = "(//a[contains(text(),'Empower – Hereditary Cancer Test')])[1]"

    def __init__(self, driver):
        self.driver = driver

    def Nav_sitemap(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.sitemap).click()
        Actual_Title = self.driver.title
        print("Title_of_Page: ", Actual_Title)
        Expected_Title = "Sitemap | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)

    def Nav_signatera(self):
        self.driver.find_element(By.XPATH, self.signatera).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera – Circulating Tumor DNA Blood Test | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_altera(self):
        self.driver.find_element(By.XPATH, self.altera).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Altera | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_empower(self):
        self.driver.find_element(By.XPATH, self.empower).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Empower Overview | Empower Overview| Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
