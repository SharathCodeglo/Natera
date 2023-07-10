# Women's Health
import time
from selenium.webdriver.common.by import By


class ForPatients:
    sitemap = "//a[normalize-space()='Sitemap']"
    Pricing_and_Billing_Information = "//*[@id='et-boc']/div/div/div[2]/div[2]/div[3]/div/div/ul/ul[2]/ul/li[1]/a"
    Womens_Health_Portal = "//*[@id='et-boc']/div/div/div[2]/div[2]/div[3]/div/div/ul/ul[2]/ul/li[2]/a"

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
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR PATIENTS')])[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Pricing_and_Billing_Information).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Women's Health Pricing & Billing | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_Womens_Health_Portal(self):
        self.driver.find_element(By.XPATH, self.Womens_Health_Portal).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            if self.driver.title == "My Natera - Patient Portal":
                print(self.driver.title)
            else:
                print("Title is not matched")
                time.sleep(2)
