import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class AnimeFrames:
    click_ClinicianInfo_XPATH = "(//a[normalize-space()='Clinician Information'])[1]"
    click_Frame1_XPATH = "(//header[@class='uf-tile-copy'])[1]"
    click_Frame2_XPATH = "(//header[@class='uf-tile-copy'])[2]"
    click_Frame3_XPATH = "(//header[@class='uf-tile-copy'])[3]"

    def __init__(self, driver):
        self.driver = driver

    def click_ClinicianInfo(self):
        self.driver.find_element(By.XPATH, self.click_ClinicianInfo_XPATH).click()
        self.driver.maximize_window()
        time.sleep(4)

    def clickAnimeBlog_1(self):
        anime1 = self.driver.find_element(By.XPATH, self.click_Frame1_XPATH)
        ActionChains(self.driver).move_to_element(anime1).perform()
        time.sleep(2)

    def clickAnimeBlog_2(self):
        anime2 = self.driver.find_element(By.XPATH, self.click_Frame2_XPATH)
        ActionChains(self.driver).move_to_element(anime2).perform()
        time.sleep(2)

    def clickAnimeBlog_3(self):
        anime3 = self.driver.find_element(By.XPATH, self.click_Frame3_XPATH)
        ActionChains(self.driver).move_to_element(anime3).perform()
        time.sleep(2)


class ViewPresentation:
    click_ClinicianInfo_XPATH = "(//a[normalize-space()='Clinician Information'])[1]"
    present = "//h2[contains(text(),'Learn what was discovered at our satellite symposi')]"
    click_ViewPresentation_XPATH = "//a[normalize-space()='View presentation']"
    click_firstname_name = "firstname"
    click_lastname_name = "lastname"
    click_Email_name = "email"
    click_company_name = "company"
    click_postalcode_name = "zip"
    click_country_XPATH = "//select[@name='country']"
    click_YESradiobtn_XPATH = "//span[normalize-space()='Yes']"
    click_NOradiobtn_XPATH = "//span[normalize-space()='No']"
    click_contactUs_XPATH = "//input[@value='Contact Us']"
    click_close_XPATH = "//button[@aria-label='Close modal']"

    def __init__(self, driver):
        self.driver = driver

    def click_ClinicianInfo(self):
        self.driver.find_element(By.XPATH, self.click_ClinicianInfo_XPATH).click()
        time.sleep(4)

    def click_presentation(self):
        Present = self.driver.find_element(By.XPATH, self.present)
        self.driver.execute_script("arguments[0].scrollIntoView();", Present)
        self.driver.find_element(By.XPATH, self.click_ViewPresentation_XPATH).click()

    def setFirstname(self, firstname):
        self.driver.find_element(By.NAME, self.click_firstname_name).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.NAME, self.click_lastname_name).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(By.NAME, self.click_Email_name).send_keys(email)

    def setPostalcode(self, postal):
        self.driver.find_element(By.NAME, self.click_postalcode_name).send_keys(postal)

    def setCompanyName(self, company):
        self.driver.find_element(By.NAME, self.click_company_name).send_keys(company)

    def setCountry(self):
        country = Select(self.driver.find_element(By.XPATH, self.click_country_XPATH))

        for options in country.options:
            if options.text == "China":
                options.click()
                break

    def clickRadioButton(self, physician):
        if physician == "yes":
            self.driver.find_element(By.XPATH, self.click_YESradiobtn_XPATH).click()
        elif physician == "no":
            self.driver.find_element(By.XPATH, self.click_NOradiobtn_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.click_YESradiobtn_XPATH).click()

    def clickClose(self):
        self.driver.find_element(By.XPATH, self.click_close_XPATH).click()


class Feedback:
    click_ClinicianInfo_XPATH = "(//a[normalize-space()='Clinician Information'])[1]"
    click_overview_XPATH = "//a[normalize-space()='Overview']"
    click_firstname_XPATH = "//*[@id='firstname-30bcbe40-1224-460b-b637-c76de34d4720']"
    click_lastname_name = "//*[@id='lastname-30bcbe40-1224-460b-b637-c76de34d4720']"
    click_Email_name = "//*[@id='email-30bcbe40-1224-460b-b637-c76de34d4720']"
    click_company_name = "//*[@id='company-30bcbe40-1224-460b-b637-c76de34d4720']"
    click_Phone_name = "phone"
    click_postalcode_name = "//*[@id='zip-30bcbe40-1224-460b-b637-c76de34d4720']"
    click_country_XPATH = "//*[@id='country-30bcbe40-1224-460b-b637-c76de34d4720']"
    click_YESradiobtn_XPATH = "(//span[contains(text(),'Yes')])[2]"
    click_NOradiobtn_XPATH = "(//span[contains(text(),'No')])[3]"
    click_comments_name = "comments_questions"
    click_contactUs_XPATH = "//input[@value='Contact Us']"

    def __init__(self, driver):
        self.driver = driver

    def click_ClinicianInfo(self):
        self.driver.find_element(By.XPATH, self.click_ClinicianInfo_XPATH).click()
        time.sleep(4)

    def setFirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.click_firstname_XPATH).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element(By.XPATH, self.click_lastname_name).send_keys(lastname)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.click_Email_name).send_keys(email)

    def setPostalcode(self, postal):
        self.driver.find_element(By.XPATH, self.click_postalcode_name).send_keys(postal)

    def setCompanyName(self, company):
        self.driver.find_element(By.XPATH, self.click_company_name).send_keys(company)

    def setPhone(self, phone):
        self.driver.find_element(By.NAME, self.click_Phone_name).send_keys(phone)

    def setCountry(self):
        country = Select(self.driver.find_element(By.XPATH, self.click_country_XPATH))

        for options in country.options:
            # print(options.text)
            if options.text == "India":
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

