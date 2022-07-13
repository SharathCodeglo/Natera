import time
from selenium.webdriver.common.by import By


class FAQ_Overview:
    click_FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    click_Overview_XPATH = "//span[@class='nat-accordion__filter-list-item nat-accordion__filter-list-item_active']"
    Qn01_XPATH = "//h5[normalize-space()='What is Altera and what does it test for?']"
    Qn02_XPATH = "//h5[contains(text(),'How is the Altera test different from my Signatera')]"

    def __init__(self, driver):
        self.driver = driver

    def clickFAQ(self):
        self.driver.find_element(By.XPATH, self.click_FAQ_XPATH).click()
        time.sleep(2)

    def faq_Overview(self):
        self.driver.find_element(By.XPATH, self.click_Overview_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)


class FAQ_OrderingAndLogistics:
    click_FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    order_logist_XPATH = "//span[normalize-space()='ORDERING & LOGISTICS']"
    Qn01_XPATH = "//h5[contains(text(),'Can the Altera test be done on all types of cancer')]"
    Qn02_XPATH = "//h5[contains(text(),'I already had Signatera testing, can my doctor now')]"
    Qn03_XPATH = "//h5[contains(text(),'I already had Altera testing, can my doctor now or')]"
    Qn04_XPATH = "//h5[contains(text(),'Can my doctor order Signatera and Altera at the sa')]"
    Qn05_XPATH = "//h5[contains(text(),'Can I have Signatera and or Altera testing if I am')]"
    Qn06_XPATH = "//h5[contains(text(),'Does getting a COVID-19 vaccine affect my eligibil')]"
    Qn07_XPATH = "//h5[contains(text(),'How long does it take to receive Altera results/Wh')]"
    Qn08_XPATH = "//h5[normalize-space()='What samples are required for the initial test?']"
    Qn09_XPATH = "//h5[normalize-space()='Why do you need both a tissue and blood sample?']"

    def __init__(self, driver):
        self.driver = driver

    def clickFAQ(self):
        self.driver.find_element(By.XPATH, self.click_FAQ_XPATH).click()
        time.sleep(2)

    def faq_OrderAndLogist(self):
        self.driver.find_element(By.XPATH, self.order_logist_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn03_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn04_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn05_XPATH).click()
        time.sleep(2)
        scroll = self.driver.find_element(By.XPATH, self.Qn05_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Qn06_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn07_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn08_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn09_XPATH).click()
        time.sleep(2)


class FAQ_ResultsAndReports:
    click_FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    result_report_XPATH = "//span[normalize-space()='RESULTS & REPORTS']"
    Qn01_XPATH = "//h5[contains(text(),'Will the Altera report also identify what clinical')]"
    Qn02_XPATH = "//h5[normalize-space()='How do I obtain my test results?']"

    def __init__(self, driver):
        self.driver = driver

    def clickFAQ(self):
        self.driver.find_element(By.XPATH, self.click_FAQ_XPATH).click()
        time.sleep(2)

    def faq_ResultAndReports(self):
        self.driver.find_element(By.XPATH, self.result_report_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)


class FAQ_Billing:
    click_FAQ_XPATH = "(//a[normalize-space()='FAQ'])[1]"
    billing_XPATH = "//span[normalize-space()='BILLING']"
    Qn01_XPATH = "//h5[normalize-space()='Is Altera testing covered by Medicare?']"
    Qn02_XPATH = "//h5[normalize-space()='How much will it cost patients?']"
    Qn03_XPATH = "//h5[normalize-space()='Can a patient cancel an order?']"
    Qn04_XPATH = "//h5[contains(text(),'What happens if coverage is denied? How does the a')]"
    Qn05_XPATH = "//h5[contains(text(),'Does Natera reach out to patients to explain their')]"
    Qn06_XPATH = "//h5[contains(text(),'Who can I contact if I have any additional billing')]"

    def __init__(self, driver):
        self.driver = driver

    def clickFAQ(self):
        self.driver.find_element(By.XPATH, self.click_FAQ_XPATH).click()
        time.sleep(2)

    def faq_Billing(self):
        self.driver.find_element(By.XPATH, self.billing_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn01_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn02_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn03_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn04_XPATH).click()
        time.sleep(2)
        scroll = self.driver.find_element(By.XPATH, self.Qn04_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.Qn05_XPATH).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Qn06_XPATH).click()
        time.sleep(2)

