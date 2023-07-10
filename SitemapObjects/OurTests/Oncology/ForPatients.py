import time
from selenium.webdriver.common.by import By


class ForPatients:
    sitemap = "//a[normalize-space()='Sitemap']"
    Signatera_Patient_Information = "//a[@href='/oncology/signatera-advanced-cancer-detection/patients/']"
    Signatera_for_Colorectal_Cancer_Patients = "//a[normalize-space()='Signatera for Colorectal Cancer Patients']"
    Signatera_for_Bladder_Cancer_Patients = "//a[normalize-space()='Signatera for Bladder Cancer Patients']"
    Signatera_for_Immunotherapy_Patients = "//a[normalize-space()='Signatera for Immunotherapy Patients']"

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

    def Nav_Signatera_Patient_Information(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR PATIENTS')])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Signatera_Patient_Information).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera for Patients | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Signatera_for_Colorectal_Cancer_Patients(self):
        self.driver.find_element(By.XPATH, self.Signatera_for_Colorectal_Cancer_Patients).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera Patient CRC & early stage cancers | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Signatera_for_Bladder_Cancer_Patients(self):
        self.driver.find_element(By.XPATH, self.Signatera_for_Bladder_Cancer_Patients).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Bladder Cancer | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Signatera_for_Immunotherapy_Patients(self):
        self.driver.find_element(By.XPATH, self.Signatera_for_Immunotherapy_Patients).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera Patient IO monitoring | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
