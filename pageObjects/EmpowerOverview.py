import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Scroll:
    Scroll_ByElement_Xpath = "//h2[normalize-space()='Actionable reports guide next steps, including:']"

    def __init__(self, driver):
        self.driver = driver

    def Scroll_ByElement(self):
        # Scroll till the visible of element
        scroll = self.driver.find_element(By.XPATH, self.Scroll_ByElement_Xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        value = self.driver.execute_script("return window.pageYOffset;")
        print("Successfully Scrolled:", value)
        time.sleep(2)

    def Scroll_toBottom(self):
        # Scroll till the end of the page
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("Successfully Scrolled:", value)
        time.sleep(2)

    def Scroll_toTop(self):
        # Scroll back to the full page
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
        value = self.driver.execute_script("return window.pageYOffset;")
        print("Successfully Scrolled:", value)
        print()
        time.sleep(2)


class Learnmore:
    overview_XPATH = "(//a[normalize-space()='Overview'])[1]"
    learnmore_XPATH = "//a[normalize-space()='Learn more']"
    scroll_XPATH = "//h2[normalize-space()='Streamlined family cancer history intake with NEVA']"

    def __init__(self, driver):
        self.driver = driver

    def clickOverview(self):
        self.driver.find_element(By.XPATH, self.overview_XPATH).click()
        time.sleep(2)

    def learnmore(self):
        scroll = self.driver.find_element(By.XPATH, self.scroll_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.learnmore_XPATH).click()
        print(self.driver.title)
        time.sleep(2)


class Feedback_learnmore:
    overview_XPATH = "(//a[normalize-space()='Overview'])[1]"
    scroll_XPATH = "//h2[normalize-space()='Streamlined family cancer history intake with NEVA']"
    learnmore_XPATH = "//a[normalize-space()='Learn more']"
    click_firstname_name = "firstname"
    click_lastname_name = "lastname"
    click_Email_name = "email"
    click_Phone_name = "phone"
    click_postalcode_name = "zip"
    click_country_XPATH = "//select[@name='country']"
    click_YESradiobtn_XPATH = "//span[normalize-space()='Yes']"
    click_NOradiobtn_XPATH = "//span[normalize-space()='No']"
    click_contactUs_XPATH = "//input[@value='Contact Us']"

    def __init__(self, driver):
        self.driver = driver

    def clickOverview(self):
        self.driver.find_element(By.XPATH, self.overview_XPATH).click()
        time.sleep(2)

    def learnmore(self):
        scroll = self.driver.find_element(By.XPATH, self.scroll_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.learnmore_XPATH).click()
        time.sleep(2)

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
        scroll = self.driver.find_element(By.XPATH, self.click_country_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
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


class AnimeFrame:
    overview_XPATH = "(//a[normalize-space()='Overview'])[1]"
    anime1 = "//h2[normalize-space()='Natera Empower']"
    anime2 = "//h2[contains(text(),'A Family’s History: Casey’s Journey With Hereditar')]"
    anime3 = "//h2[contains(text(),'Clinical Impact of Informative and Actionable Resu')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOverview(self):
        self.driver.find_element(By.XPATH, self.overview_XPATH).click()
        time.sleep(2)

    def frames(self):
        frame1 = self.driver.find_element(By.XPATH, self.anime1)
        ActionChains(self.driver).move_to_element(frame1).perform()
        time.sleep(2)

        frame2 = self.driver.find_element(By.XPATH, self.anime2)
        ActionChains(self.driver).move_to_element(frame2).perform()
        time.sleep(2)

        frame3 = self.driver.find_element(By.XPATH, self.anime3)
        ActionChains(self.driver).move_to_element(frame3).perform()
        time.sleep(2)


class Feedback_Empower:
    overview_XPATH = "(//a[normalize-space()='Overview'])[1]"
    click_firstname_name = "firstname"
    click_lastname_name = "lastname"
    click_Email_name = "email"
    click_Phone_name = "phone"
    click_postalcode_name = "zip"
    click_country_XPATH = "//select[@name='country']"
    click_YESradiobtn_XPATH = "//span[normalize-space()='Yes']"
    click_NOradiobtn_XPATH = "//span[normalize-space()='No']"
    click_comments_XPATH = "//*[@id='comments_questions-41106803-ea44-4982-a92e-16af434be87e']"
    contactUs_XPATH = "//input[@value='Contact Us']"

    def __init__(self, driver):
        self.driver = driver

    def clickOverview(self):
        self.driver.find_element(By.XPATH, self.overview_XPATH).click()
        time.sleep(2)

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
        scroll = self.driver.find_element(By.XPATH, self.click_country_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
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

    def clickComments(self, comments):
        self.driver.find_element(By.XPATH, self.click_comments_XPATH).send_keys(comments)

    def contact_us(self):
        ContactUs = self.driver.find_element(By.XPATH, self.contactUs_XPATH)
        print("ContactUs is Enabled:", ContactUs.is_enabled())

