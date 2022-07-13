import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Scroll:
    Scroll_ByElement_Xpath = "//h2[contains(text(),'One tumor sample – two tests')]"

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


class InnerLink:
    list_of_boosted_genes_XPATH = "//a[normalize-space()='See full list of boosted genes']"
    download_boosted_genes_XPATH = "//a[normalize-space()='Download PDF']"

    def __init__(self, driver):
        self.driver = driver

    def clickListOfGenes(self):
        self.driver.find_element(By.XPATH, self.list_of_boosted_genes_XPATH).click()
        time.sleep(2)
        Windows_ID = self.driver.window_handles

        for ID in Windows_ID:
            self.driver.switch_to.window(ID)
            time.sleep(2)
            if self.driver.title == "Altera | Natera":
                self.driver.close()

    def downloadListOfGenes(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, self.download_boosted_genes_XPATH).click()
        time.sleep(2)


class LearnMore:
    learnmore_XPATH = "//a[normalize-space()='Learn More']"

    def __init__(self, driver):
        self.driver = driver

    def learnmore(self):
        self.driver.find_element(By.XPATH, self.learnmore_XPATH).click()
        print(self.driver.title)
        time.sleep(2)


class Flipbook_LearnMore:
    learnmore_XPATH = "//a[normalize-space()='Learn More']"
    flipbook1_XPATH = "//*[@id='et-boc']/div/div/div[3]/div/div/div[3]/div/div/table/tbody/tr[1]/td[3]/a"
    flipbook2_XPATH = "//*[@id='et-boc']/div/div/div[3]/div/div/div[3]/div/div/table/tbody/tr[2]/td[3]/a"
    flipbook3_XPATH = "//*[@id='et-boc']/div/div/div[3]/div/div/div[3]/div/div/table/tbody/tr[3]/td[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def learnmore(self):
        self.driver.find_element(By.XPATH, self.learnmore_XPATH).click()

    def flipbooks(self):
        flip1 = self.driver.find_element(By.XPATH, self.flipbook1_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", flip1)
        print("Flipbook_1 isEnabled:", flip1.is_enabled())
        ActionChains(self.driver).move_to_element(flip1).perform()
        time.sleep(2)

        flip2 = self.driver.find_element(By.XPATH, self.flipbook2_XPATH)
        print("Flipbook_2 isEnabled:", flip2.is_enabled())
        ActionChains(self.driver).move_to_element(flip2).perform()
        time.sleep(2)

        flip3 = self.driver.find_element(By.XPATH, self.flipbook3_XPATH)
        print("Flipbook_3 isEnabled:", flip3.is_enabled())
        ActionChains(self.driver).move_to_element(flip3).perform()
        time.sleep(2)


class ReadInspirePublication_LearnMore:
    learnmore_XPATH = "//a[normalize-space()='Learn More']"
    read_inspire_publication_XPATH = "//a[normalize-space()='Read the INSPIRE publication']"
    click_firstname_name = "firstname"
    click_lastname_name = "lastname"
    click_Email_name = "email"
    click_company_name = "company"
    click_postalcode_name = "zip"
    click_country_XPATH = "//select[@name='country']"
    click_YESradiobtn_XPATH = "//span[normalize-space()='Yes']"
    click_NOradiobtn_XPATH = "//span[normalize-space()='No']"
    click_DownloadNow_XPATH = "//input[@value='Download Now']"
    close_modal_XPATH = "//button[@aria-label='Close modal']"

    def __init__(self, driver):
        self.driver = driver

    def learnmore(self):
        self.driver.find_element(By.XPATH, self.learnmore_XPATH).click()
        time.sleep(3)

    def clickRIP(self):
        scroll = self.driver.find_element(By.XPATH, self.read_inspire_publication_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.read_inspire_publication_XPATH).click()
        time.sleep(2)

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
            # print(options.text)
            if options.text == "Brazil":
                options.click()

    def clickRadioButton(self, physician):
        if physician == "yes":
            self.driver.find_element(By.XPATH, self.click_YESradiobtn_XPATH).click()
        elif physician == "no":
            self.driver.find_element(By.XPATH, self.click_NOradiobtn_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.click_YESradiobtn_XPATH).click()

    def download(self):
        download = self.driver.find_element(By.XPATH, self.click_DownloadNow_XPATH)
        print("Download button is Enabled:", download.is_enabled())
        time.sleep(2)


class ReadMore_learnmore:
    learnmore1_XPATH = "//a[normalize-space()='Learn More']"
    read_more_XPATH = "//a[normalize-space()='Read More']"
    learnmore2_XPATH = "//a[normalize-space()='Learn More']"
    downloadStudyOverview_XPATH = "//a[normalize-space()='Download the Study Overview']"
    downloadPDF_XPATH = "//a[normalize-space()='Download PDF']"

    def __init__(self, driver):
        self.driver = driver

    def learnmore1(self):
        self.driver.find_element(By.XPATH, self.learnmore1_XPATH).click()
        time.sleep(3)

    def readmore(self):
        scroll = self.driver.find_element(By.XPATH, self.read_more_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.read_more_XPATH).click()
        time.sleep(2)

    def learnmore2(self):
        learn = self.driver.find_element(By.XPATH, self.learnmore2_XPATH)
        print("Learn More is Enabled:", learn.is_enabled())

    def downloadstudy(self):
        scroll = self.driver.find_element(By.XPATH, self.downloadStudyOverview_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.find_element(By.XPATH, self.downloadStudyOverview_XPATH).click()
        time.sleep(2)

        Windows_IDs = self.driver.window_handles

        for ID in Windows_IDs:
            self.driver.switch_to.window(ID)
            # print(self.driver.title)
            time.sleep(2)
            if self.driver.title == "Bespoke IO | Clinicians | Natera":
                self.driver.close()


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

    def clickOverview(self):
        self.driver.find_element(By.XPATH, self.click_overview_XPATH).click()
        time.sleep(2)

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

    def setComments(self, comments):
        self.driver.find_element(By.NAME, self.click_comments_name).send_keys(comments)
        time.sleep(2)


