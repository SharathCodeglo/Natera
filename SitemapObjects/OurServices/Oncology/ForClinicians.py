# Oncology_OurServices
import time
from selenium.webdriver.common.by import By


class ForClinicians:
    sitemap = "//a[normalize-space()='Sitemap']"
    Oncology_Portal = "(//a[normalize-space()='Oncology Portal'])[5]"
    Order_a_Test_Kit = "//a[contains(text(),'Order a Test Kit')]"
    Contact_Us = "(//a[normalize-space()='Contact Us'])[15]"

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

    def Nav_Oncology_Portal(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR CLINICIANS')])[4]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Oncology_Portal).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            time.sleep(2)
            if self.driver.title == "Oncology Portal":
                print("Title of Page:", self.driver.title)
                self.driver.close()
        self.driver.switch_to.window(Windows_ID[0])

    def Nav_Order_a_Test_Kit(self):
        self.driver.find_element(By.XPATH, self.Order_a_Test_Kit).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            time.sleep(2)
            if self.driver.title == "Oncology Portal":
                print("Title of Page:", self.driver.title)
                self.driver.close()
        self.driver.switch_to.window(Windows_ID[0])

    def Nav_Contact_Us(self):
        self.driver.find_element(By.XPATH, self.Contact_Us).click()
        Actual_Title = self.driver.title
        print("Title_of_Page: ", Actual_Title)
        Expected_Title = "Contact Us | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
