# Women's Health
import time
from selenium.webdriver.common.by import By


class Tests:
    sitemap = "//a[normalize-space()='Sitemap']"
    Horizon_Advanced_Carrier_Screening = "//a[contains(text(),'Horizon – Advanced Carrier Screening')]"
    Panorama_Non_Invas = "//a[contains(text(),'Panorama – Non-Invasive Prenatal Testing (NIPT)')]"
    Empower_Hereditary_Cancer_Test = "(//a[contains(text(),'Empower – Hereditary Cancer Test')])[2]"
    Vistara_Single_Gene_NIPT = "//a[contains(text(),'Vistara – Single-Gene NIPT')]"
    Anora_Miscarriage_Test = "//a[contains(text(),'Anora – Miscarriage Test')]"
    Spectrum_Preimplantation_Genetics = "//a[contains(text(),'Spectrum – Preimplantation Genetics')]"
    Vasistera_Limited = "//a[contains(text(),'Vasistera – Limited noninvasive prenatal testing (')]"

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

    def Nav_Horizon_Advanced_Carrier_Screening(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'TESTS')])[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Horizon_Advanced_Carrier_Screening).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Genetic Carrier Screening | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Panorama_Non_Invas(self):
        self.driver.find_element(By.XPATH, self.Panorama_Non_Invas).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Panorama – Non-Invasive Prenatal Testing (NIPT) | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Empower_Hereditary_Cancer_Test(self):
        self.driver.find_element(By.XPATH, self.Empower_Hereditary_Cancer_Test).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Empower Overview | Empower Overview| Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Vistara_Single_Gene_NIPT(self):
        self.driver.find_element(By.XPATH, self.Vistara_Single_Gene_NIPT).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Vistara Overview | Vistara Single-Gene Disorders Testing | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Anora_Miscarriage_Test(self):
        self.driver.find_element(By.XPATH, self.Anora_Miscarriage_Test).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Anora Overview | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Spectrum_Preimplantation_Genetics(self):
        self.driver.find_element(By.XPATH, self.Spectrum_Preimplantation_Genetics).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Spectrum – Preimplantation Genetic Testing (PGT) | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Vasistera_Limited(self):
        self.driver.find_element(By.XPATH, self.Vasistera_Limited).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Vasistera | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
