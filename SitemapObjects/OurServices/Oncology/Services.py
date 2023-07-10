# Oncology_OurServices
import time
from selenium.webdriver.common.by import By


class Services:
    sitemap = "//a[normalize-space()='Sitemap']"
    NateraCore_Services = "//*[@id='et-boc']/div/div/div[2]/div[4]/div[1]/div/div/ul/ul[1]/ul/li[1]/a"
    Pharma_Partnership = "//a[contains(text(),'Pharma Partnership')]"

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

    def Nav_NateraCore_Services(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'SERVICES')])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.NateraCore_Services).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Oncology Core Services | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Pharma_Partnership(self):
        self.driver.find_element(By.XPATH, self.Pharma_Partnership).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera research pipeline | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
