# Organ Health
import time
from selenium.webdriver.common.by import By


class ForPatients:
    sitemap = "//a[normalize-space()='Sitemap']"
    Prospera_for_Kidney_Patients = "//a[@href='/organ-health/prospera-organ-transplantation-assessment/patients/']"
    Prospera_for_Heart_Patients = "//a[@href='/organ-health/prospera-heart-transplantation-assessment/patients/']"
    Prospera_for_Lung_Patients = "//a[@href='/organ-health/prospera-lung-transplantation-assessment/patients/']"
    Renasight_Patient_Information = "//a[@href='/organ-health/renasight-genetic-testing/patients/']"

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

    def Nav_Prospera_for_Kidney_Patients(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR PATIENTS')])[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Prospera_for_Kidney_Patients).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Prospera Patients | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Prospera_for_Heart_Patients(self):
        self.driver.find_element(By.XPATH, self.Prospera_for_Heart_Patients).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Prospera Heart Patient Information | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Prospera_for_Lung_Patients(self):
        self.driver.find_element(By.XPATH, self.Prospera_for_Lung_Patients).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Prospera Lung Patient Information | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Renasight_Patient_Information(self):
        self.driver.find_element(By.XPATH, self.Renasight_Patient_Information).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Renasight Patient | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
