import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class InterLinks:
    click_PatientInfo_XPATH = "(//a[normalize-space()='Patient Information'])[1]"
    click_CancerPatient_XPATH = "//a[normalize-space()='Colorectal cancer patient']"
    click_ImmunoPatient_XPATH = "//a[normalize-space()='Immunotherapy patient']"
    click_LearnMore_XPATH = "//a[normalize-space()='Learn More']"

    def __init__(self, driver):
        self.driver = driver

    def click_PatientInfo(self):
        self.driver.find_element(By.XPATH, self.click_PatientInfo_XPATH).click()
        time.sleep(3)


class AnimeFrames:
    click_PatientInfo_XPATH = "//a[normalize-space()='Patient Information']"
    click_AnimeFrame1_XPATH = "(//header[@class='uf-tile-copy'])[1]"
    click_AnimeFrame2_XPATH = "(//header[@class='uf-tile-copy'])[2]"
    click_AnimeFrame3_XPATH = "(//header[@class='uf-tile-copy'])[3]"
    click_AnimeFrame4_XPATH = "(//header[@class='uf-tile-copy'])[4]"
    click_AnimeFrame5_XPATH = "(//header[@class='uf-tile-copy'])[5]"
    click_AnimeFrame6_XPATH = "(//header[@class='uf-tile-copy'])[6]"

    def __init__(self, driver):
        self.driver = driver

    def click_PatientInfo(self):
        self.driver.find_element(By.XPATH, self.click_PatientInfo_XPATH).click()
        self.driver.maximize_window()
        time.sleep(4)

    def clickAnimeBlog_1(self):
        anime1 = self.driver.find_element(By.XPATH, self.click_AnimeFrame1_XPATH)
        ActionChains(self.driver).move_to_element(anime1).perform()
        time.sleep(2)

    def clickAnimeBlog_2(self):
        anime2 = self.driver.find_element(By.XPATH, self.click_AnimeFrame2_XPATH)
        ActionChains(self.driver).move_to_element(anime2).perform()
        time.sleep(2)

    def clickAnimeBlog_3(self):
        anime3 = self.driver.find_element(By.XPATH, self.click_AnimeFrame3_XPATH)
        ActionChains(self.driver).move_to_element(anime3).perform()
        time.sleep(2)

    def clickAnimeBlog_4(self):
        anime4 = self.driver.find_element(By.XPATH, self.click_AnimeFrame4_XPATH)
        ActionChains(self.driver).move_to_element(anime4).perform()
        time.sleep(2)

    def clickAnimeBlog_5(self):
        anime5 = self.driver.find_element(By.XPATH, self.click_AnimeFrame5_XPATH)
        ActionChains(self.driver).move_to_element(anime5).perform()
        time.sleep(2)

    def clickAnimeBlog_6(self):
        anime6 = self.driver.find_element(By.XPATH, self.click_AnimeFrame6_XPATH)
        ActionChains(self.driver).move_to_element(anime6).perform()
        time.sleep(2)


class Feedback:
    click_PatientInfo_XPATH = "//a[normalize-space()='Patient Information']"
    click_firstname_name = "firstname"
    click_lastname_name = "lastname"
    click_Email_name = "email"
    click_Phone_name = "phone"
    click_postalcode_name = "zip"
    click_country_XPATH = "//select[@name='country']"
    click_YESradiobtn_XPATH = "//span[normalize-space()='Yes']"
    click_NOradiobtn_XPATH = "//span[normalize-space()='No']"
    click_comments_name = "comments_questions"
    click_contactUs_XPATH = "//input[@value='Contact Us']"

    def __init__(self, driver):
        self.driver = driver

    def click_PatientInfo(self):
        self.driver.find_element(By.XPATH, self.click_PatientInfo_XPATH).click()
        self.driver.maximize_window()
        time.sleep(4)

    def setFirstname(self, firstname):
        self.driver.find_element(By.NAME, self.click_firstname_name).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.NAME, self.click_lastname_name).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.click_Email_name).send_keys(email)

    def setPostalcode(self, postal):
        self.driver.find_element(By.NAME, self.click_postalcode_name).send_keys(postal)

    def setPhone(self, phone):
        self.driver.find_element(By.NAME, self.click_Phone_name).send_keys(phone)

    def setCountry(self):
        country = Select(self.driver.find_element(By.XPATH, self.click_country_XPATH))

        for options in country.options:
            if options.text == "Brazil":
                options.click()

    def clickRadioButton(self, physician):
        if physician == "yes":
            self.driver.find_element(By.XPATH, self.click_YESradiobtn_XPATH).click()
        elif physician == "no":
            self.driver.find_element(By.XPATH, self.click_NOradiobtn_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.click_YESradiobtn_XPATH).click()

    def setComments(self, comments):
        self.driver.find_element(By.NAME, self.click_comments_name).send_keys(comments)

