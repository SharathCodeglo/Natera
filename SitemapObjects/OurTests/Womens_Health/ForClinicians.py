# Women's Health
import time
from selenium.webdriver.common.by import By


class ForClinicians:
    sitemap = "//a[normalize-space()='Sitemap']"
    NateraConnect_Provider_Portal = "//a[contains(text(),'NateraConnect Provider Portal')]"
    Horizon_Conditions_List = "//a[@href='/womens-health/horizon-advanced-carrier-screening/what-it-screens/']"
    NEVA_for_Empower = "//*[@id='et-boc']/div/div/div[2]/div[2]/div[3]/div/div/ul/ul[3]/ul/li[3]/a"

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

    def Nav_NateraConnect_Provider_Portal(self):
        scroll = self.driver.find_element(By.XPATH, "(//li[contains(text(),'FOR CLINICIANS')])[3]")
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.NateraConnect_Provider_Portal).click()
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            time.sleep(2)
            if self.driver.title == "Natera Connect":
                print("Title of Page:", self.driver.title)
                self.driver.close()
        self.driver.switch_to.window(Windows_ID[0])

    def Nav_Horizon_Conditions_List(self):
        self.driver.find_element(By.XPATH, self.Horizon_Conditions_List).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Comprehensive Screening Options from Horizon | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
        self.driver.back()

    def Nav_NEVA_for_Empower(self):
        self.driver.find_element(By.XPATH, self.NEVA_for_Empower).click()
        Actual_Title = self.driver.title
        print("Title of Page: " + Actual_Title)
        Expected_Title = "Women's Health NEVA | Virtual Assistant | Natera"
        assert Expected_Title == Actual_Title, "Title is not Matched"
        time.sleep(2)
