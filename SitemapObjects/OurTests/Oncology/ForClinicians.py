import time
from selenium.webdriver.common.by import By


class ForClinicians:
    sitemap = "//a[normalize-space()='Sitemap']"
    Signatera_for_Colorectal_Cancer = "//a[@href='/oncology/signatera-advanced-cancer-detection/clinicians/']"
    Signatera_for_Bladder_Cancer = "//*[@id='et-boc']/div/div/div[2]/div[2]/div[1]/div/div/ul/ul[3]/ul/li[2]/a"
    Signatera_for_Immunotherapy_Monitoring = "//a[@href='/oncology/signatera-advanced-cancer-detection/clinicians/" \
                                             "io-monitoring/']"
    Signatera_Research_Pipeline = "(//a[normalize-space()='Signatera Research Pipeline'])[3]"
    Oncology_Portal = "(//a[contains(@target,'_blank')][normalize-space()='Oncology Portal'])[4]"

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

    def Nav_Signatera_for_Colorectal_Cancer(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR CLINICIANS')])[1]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Signatera_for_Colorectal_Cancer).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera Clinicians | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Signatera_for_Bladder_Cancer(self):
        self.driver.find_element(By.XPATH, self.Signatera_for_Bladder_Cancer).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Bladder Cancer | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Signatera_for_Immunotherapy_Monitoring(self):
        self.driver.find_element(By.XPATH, self.Signatera_for_Immunotherapy_Monitoring).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "IO (HCP) | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Signatera_Research_Pipeline(self):
        self.driver.find_element(By.XPATH, self.Signatera_Research_Pipeline).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Signatera research pipeline | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Oncology_Portal(self):
        self.driver.find_element(By.XPATH, self.Oncology_Portal).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            time.sleep(2)
            if self.driver.title == "Oncology Portal":
                print("Title of Page:", self.driver.title)
                self.driver.close()


