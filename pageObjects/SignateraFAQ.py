import time
from selenium.webdriver.common.by import By


class FAQ_Overview:
    FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    overview_XPATH = "//*[@id='et-boc']/div/div/div[5]/div/div/div[2]/div/ul/li[1]/span"
    Qn01_XPATH = "//h5[normalize-space()='What is Signatera and what does it test for?']"
    Qn02_XPATH = "//h5[contains(text(),'How is Signatera different from current biomarker ')]"

    def __init__(self, driver):
        self.driver = driver

    def faq_Overview(self):
        self.driver.find_element(By.XPATH, self.FAQ_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.overview_XPATH).click()
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)


class FAQ_ResultsAndReports:
    FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    res_rep_XPATH = "//span[normalize-space()='RESULTS & REPORTS']"
    Qn01_XPATH = "//h5[normalize-space()='How accurate is Signatera?']"
    Qn02_XPATH = "//h5[normalize-space()='WHAT INFORMATION DOES THE TEST REPORT PROVIDE?']"
    Qn03_XPATH = "//h5[normalize-space()='WHAT DOES A POSITIVE SIGNATERA RESULT MEAN?']"
    Qn04_XPATH = "//h5[normalize-space()='WHAT DOES A NEGATIVE SIGNATERA RESULT MEAN?']"

    def __init__(self, driver):
        self.driver = driver

    def faq_ResultsAndReports(self):
        self.driver.find_element(By.XPATH, self.FAQ_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.res_rep_XPATH).click()
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn03_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn04_XPATH).click()
        time.sleep(2)


class FAQ_OrderingAndLogistics:
    FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    order_logist_XPATH = "//span[normalize-space()='ORDERING & LOGISTICS']"
    Qn01_XPATH = "//h5[normalize-space()='HOW DO I GET SIGNATERA TESTING?']"
    Qn02_XPATH = "//h5[normalize-space()='WHAT TYPE OF SAMPLES ARE NEEDED FOR SIGNATERA?']"
    Qn03_XPATH = "//h5[contains(text(),'WHAT IS THE TURNAROUND TIME FOR MY SIGNATERA RESUL')]"

    def __init__(self, driver):
        self.driver = driver

    def faq_OrderAndLogist(self):
        self.driver.find_element(By.XPATH, self.FAQ_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.order_logist_XPATH).click()
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn03_XPATH).click()
        time.sleep(2)


class FAQ_Billing:
    FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    billing_XPATH = "//span[normalize-space()='BILLING']"
    Qn01_XPATH = "//h5[normalize-space()='IS SIGNATERA COVERED BY MEDICARE ?']"
    Qn02_XPATH = "//h5[contains(text(),'Who can I contact if I have questions about my Nat')]"

    def __init__(self, driver):
        self.driver = driver

    def faq_Billing(self):
        self.driver.find_element(By.XPATH, self.FAQ_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.billing_XPATH).click()
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)


class FAQ_CustomerExp:
    FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    customer_exp_XPATH = "//*[@id='et-boc']/div/div/div[5]/div/div/div[2]/div/ul/li[5]/span"
    Qn01_XPATH = "//h5[normalize-space()='Where can I get my blood drawn for Signatera?']"

    def __init__(self, driver):
        self.driver = driver

    def faq_CustomerExp(self):
        self.driver.find_element(By.XPATH, self.FAQ_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.customer_exp_XPATH).click()
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)

