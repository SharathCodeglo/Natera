import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignateraForPatients:
    click_forPatients_XPATH = "(//a[normalize-space()='FOR PATIENTS'])[1]"
    find_ScheduleSession_XPATH = "(//a[contains(@class,'link-arrow-wrapper')])[1]"
    find_ScheduleBloodDraw_XPATH = "(//a[contains(@class,'link-arrow-wrapper')])[2]"
    click_PricingAndBilling_XPATH = "(//a[@class='link-arrow-wrapper'])[3]"
    click_firstname_name = "firstname"
    click_lastname_name = "lastname"
    click_Email_name = "email"
    click_company_name = "company"
    click_Phone_name = "phone"
    click_postalcode_name = "zip"
    click_country_XPATH = "//select[@name='country']"
    click_YESradiobtn_XPATH = "//span[normalize-space()='Yes']"
    click_NOradiobtn_XPATH = "//span[normalize-space()='No']"
    click_comments_name = "comments_questions"
    click_contactUs_XPATH = "//input[@value='Contact Us']"

    def __init__(self, driver):
        self.driver = driver

    def clickForPatients(self):
        self.driver.find_element(By.XPATH, self.click_forPatients_XPATH).click()

    def checkScheduleSession(self):
        check1 = self.driver.find_element(By.XPATH, self.find_ScheduleSession_XPATH)
        print("Schedule Session for Patients is Enabled:", check1.is_enabled())

    def checkScheduleBloodDraw(self):
        check2 = self.driver.find_element(By.XPATH, self.find_ScheduleBloodDraw_XPATH)
        print("Schedule Blood Draw for Patients is Enabled:", check2.is_enabled())

    def clickPriceAndBill(self):
        self.driver.find_element(By.XPATH, self.click_PricingAndBilling_XPATH).click()
        time.sleep(3)

    def NewWindow(self):
        Windows_IDs = self.driver.window_handles

        for ID in Windows_IDs:
            self.driver.switch_to.window(ID)
            print(self.driver.title)
            time.sleep(3)
            if self.driver.title == "Signatera – Circulating Tumor DNA Blood Test | Natera":
                self.driver.close()

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
            # print(options.text)
            if options.text == "Japan":
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
        self.driver.close()


class SignateraForClinicians:
    Click_ForClinicians_XPATH = "//*[@id='et_pb_tab_1_tab']"
    ScheduleSession_XPATH = "(//a[@class='link-arrow-wrapper'])[4]"
    LoginToOncology_XPATH = "(//a[@class='link-arrow-wrapper'])[5]"
    LearnMoreNateracore_XPATH = "(//a[@class='link-arrow-wrapper'])[6]"
    ConnectNow_XPATH = "//a[normalize-space()='Connect now']"

    def __init__(self, driver):
        self.driver = driver

    def clickForClinicians(self):
        self.driver.find_element(By.XPATH, self.Click_ForClinicians_XPATH).click()

    def checkScheduleSession(self):
        check1 = self.driver.find_element(By.XPATH, self.ScheduleSession_XPATH)
        print("Schedule Session for Clinicians is Enabled:", check1.is_enabled())

    def checkLoginOncology(self):
        check2 = self.driver.find_element(By.XPATH, self.LoginToOncology_XPATH)
        print("Login Oncology Portal is Enabled:", check2.is_enabled())

    def clickLearnMore(self):
        self.driver.find_element(By.XPATH, self.LearnMoreNateracore_XPATH).click()

    def NewWindow(self):
        Windows_IDs = self.driver.window_handles

        for ID in Windows_IDs:
            self.driver.switch_to.window(ID)
            print(self.driver.title)
            time.sleep(3)
            if self.driver.title == "Signatera – Circulating Tumor DNA Blood Test | Natera":
                self.driver.close()

    def checkconnectnow(self):
        check3 = self.driver.find_element(By.XPATH, self.ConnectNow_XPATH)
        print("Connect Now button is Enabled:", check3.is_enabled())


