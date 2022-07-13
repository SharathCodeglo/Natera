import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class KnowYourRisk:
    patient_info_XPATH = "(//a[normalize-space()='Patient Information'])[1]"
    download_patient_brochure_XPATH = "//a[normalize-space()='Download Our Patient Brochure']"
    download_patient_brochure_spanish_XPATH = "//a[normalize-space()='Descargue nuestro folleto para pacientes']"
    patients_with_cancer_diagnosis_XPATH = "//a[normalize-space()='For Patients with Cancer Diagnosis']"
    pricing_billing_XPATH = "//a[normalize-space()='View our Pricing and Billing Page']"

    def __init__(self, driver):
        self.driver = driver

    def patient_info(self):
        self.driver.find_element(By.XPATH, self.patient_info_XPATH).click()
        time.sleep(2)

    def check_links(self):
        link1 = self.driver.find_element(By.XPATH, self.download_patient_brochure_XPATH)
        link1.click()

        link2 = self.driver.find_element(By.XPATH, self.download_patient_brochure_spanish_XPATH)
        link2.click()

        link3 = self.driver.find_element(By.XPATH, self.patients_with_cancer_diagnosis_XPATH)
        link3.click()

        link4 = self.driver.find_element(By.XPATH, self.pricing_billing_XPATH)
        print("Link is Enabled:", link4.is_enabled())

        Windows_IDs = self.driver.window_handles

        for ID in Windows_IDs:
            self.driver.switch_to.window(ID)
            print(self.driver.title)
            if self.driver.title == "Empower Patient Brochure":
                time.sleep(2)
                self.driver.close()


class AnimeFrames:
    patient_info_XPATH = "(//a[normalize-space()='Patient Information'])[1]"
    frame1_XPATH = "(//header[@class='uf-tile-copy'])[1]"
    frame2_XPATH = "(//header[@class='uf-tile-copy'])[2]"
    frame3_XPATH = "(//header[@class='uf-tile-copy'])[3]"

    def __init__(self, driver):
        self.driver = driver

    def patient_info(self):
        self.driver.find_element(By.XPATH, self.patient_info_XPATH).click()
        time.sleep(3)

    def frame1(self):
        anime1 = self.driver.find_element(By.XPATH, self.frame1_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", anime1)
        ActionChains(self.driver).move_to_element(anime1).click().perform()
        time.sleep(3)
        self.driver.back()

    def frame2(self):
        anime2 = self.driver.find_element(By.XPATH, self.frame2_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", anime2)
        ActionChains(self.driver).move_to_element(anime2).click().perform()
        time.sleep(3)
        self.driver.back()

    def frame3(self):
        anime3 = self.driver.find_element(By.XPATH, self.frame3_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", anime3)
        ActionChains(self.driver).move_to_element(anime3).click().perform()
        time.sleep(3)
        self.driver.back()




