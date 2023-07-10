# Oncology_OurServices
import time
from selenium.webdriver.common.by import By


class ForPatients:
    sitemap = "//a[normalize-space()='Sitemap']"
    Pricing_and_Billing_Information = "//*[@id='et-boc']/div/div/div[2]/div[4]/div[1]/div/div/ul/ul[2]/ul/li[1]/a"
    Contact_Us = "//*[@id='et-boc']/div/div/div[2]/div[4]/div[1]/div/div/ul/ul[2]/ul/li[3]/a"

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

    def Nav_Pricing_and_Billing_Information(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR PATIENTS')])[4]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Pricing_and_Billing_Information).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera Billing | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Contact_Us(self):
        self.driver.find_element(By.XPATH, self.Contact_Us).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Contact Us | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
