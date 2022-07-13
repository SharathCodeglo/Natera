import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Scroll:
    Scroll_ByElement_Xpath = "//h2[normalize-space()='Know the Facts About Bladder Cancer']"

    def __init__(self, driver):
        self.driver = driver

    def Scroll_ByElement(self):
        # Scroll till the visible of element
        Frame1 = self.driver.find_element(By.XPATH, self.Scroll_ByElement_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", Frame1)
        value = self.driver.execute_script("return window.pageYOffset;")
        print("Successfully Scrolled:", value)
        time.sleep(3)

    def Scroll_toBottom(self):
        # Scroll till the end of the page
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("Successfully Scrolled:", value)
        time.sleep(3)

    def Scroll_toTop(self):
        # Scroll back to the full page
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("Successfully Scrolled:", value)
        print("*****Clinical Experts module as Successfully Verified*****")
        print()


class AnimatedBlogs:
    hover_anime1_xpath = "(//header[@class='uf-tile-copy'])[1]"
    hover_anime2_xpath = "(//header[@class='uf-tile-copy'])[2]"
    hover_anime3_xpath = "(//header[@class='uf-tile-copy'])[3]"

    def __init__(self, driver):
        self.driver = driver

    def clickAnimeBlog_1(self):
        anime1 = self.driver.find_element(By.XPATH, self.hover_anime1_xpath)
        ActionChains(self.driver).move_to_element(anime1).perform()
        time.sleep(2)

    def clickAnimeBlog_2(self):
        anime2 = self.driver.find_element(By.XPATH, self.hover_anime2_xpath)
        ActionChains(self.driver).move_to_element(anime2).perform()
        time.sleep(2)

    def clickAnimeBlog_3(self):
        anime3 = self.driver.find_element(By.XPATH, self.hover_anime3_xpath)
        ActionChains(self.driver).move_to_element(anime3).perform()
        time.sleep(2)


class Feedback:
    click_overview_XPATH = "//a[normalize-space()='Overview']"
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

