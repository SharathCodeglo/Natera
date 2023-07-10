# Organ Health
import time
from selenium.webdriver.common.by import By


class Tests:
    sitemap = "//a[normalize-space()='Sitemap']"
    Prospera_Kidney_Transplant_Assessment = "//a[contains(text(),'Prospera Kidney – Transplant Assessment')]"
    Prospera_Heart_Transplant_Assessment = "//a[contains(text(),'Prospera Heart – Transplant Assessment')]"
    Prospera_Lung_Transplant_Assessment = "//a[contains(text(),'Prospera Lung – Transplant Assessment')]"
    Renasight_Kidney_Gene_Panel = "//a[contains(text(),'Renasight – Kidney Gene Panel')]"

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

    def Nav_Prospera_Kidney_Transplant_Assessment(self):
        self.driver.find_element(By.XPATH, self.Prospera_Kidney_Transplant_Assessment).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Prospera Overview | Cell-Free DNA Testing | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Prospera_Heart_Transplant_Assessment(self):
        self.driver.find_element(By.XPATH, self.Prospera_Heart_Transplant_Assessment).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Prospera Heart Overview | Cell-Free DNA Testing | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Prospera_Lung_Transplant_Assessment(self):
        self.driver.find_element(By.XPATH, self.Prospera_Lung_Transplant_Assessment).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Prospera Lung Overview | Cell-Free DNA Testing | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Renasight_Kidney_Gene_Panel(self):
        self.driver.find_element(By.XPATH, self.Renasight_Kidney_Gene_Panel).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Renasight Overview | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
