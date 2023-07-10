# Organ Health
import time
from selenium.webdriver.common.by import By


class ForClinicians:
    sitemap = "//a[normalize-space()='Sitemap']"
    Prospera_for_Kidney_Clinician = "//a[@href='/organ-health/prospera-organ-transplantation-assessment/clinicians/']"
    Renasight_Clinician_Information = "//*[@id='et-boc']/div/div/div[2]/div[2]/div[2]/div/div/ul/ul[3]/ul/li[2]/a"
    Renasight_Gene_Conditions_List = "//a[@href='/organ-health/renasight-genetic-testing/gene-conditions-list/']"
    Organ_Health_Portal = "//*[@id='et-boc']/div/div/div[2]/div[2]/div[2]/div/div/ul/ul[3]/ul/li[4]/a"

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

    def Nav_Prospera_for_Kidney_Clinician(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR CLINICIANS')])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Prospera_for_Kidney_Clinician).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Transplant Rejection Assessment | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Renasight_Clinician_Information(self):
        self.driver.find_element(By.XPATH, self.Renasight_Clinician_Information).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            if self.driver.title == "Renasight Clinicians | Natera":
                print(self.driver.title)
                self.driver.close()
                time.sleep(2)
        self.driver.switch_to.window(Windows_ID[0])

    def Nav_Renasight_Gene_Conditions_List(self):
        self.driver.find_element(By.XPATH, self.Renasight_Gene_Conditions_List).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Renasight Gene Conditions List | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Organ_Health_Portal(self):
        self.driver.find_element(By.XPATH, self.Organ_Health_Portal).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            time.sleep(2)
            if self.driver.title == "Organ Health Portal":
                print("Title of Page:", self.driver.title)
                self.driver.close()
