from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Nav_Signatera:
    click_ourpeople_xpath = "//*[@id='menu-item-49']/a/span[1]"
    click_oncology_xpath = "//*[@id='menu-item-55']/a/span[1]"
    click_signatera_xpath = "//span[normalize-space()='Residual Disease Test (MRD)']"

    def __init__(self, driver):
        self.driver = driver  # self.driver is a "class variable"

    def select_signatera(self):
        click_ourpeople = self.driver.find_element(By.XPATH, self.click_ourpeople_xpath)
        click_oncology = self.driver.find_element(By.XPATH, self.click_oncology_xpath)
        click_signatera = self.driver.find_element(By.XPATH, self.click_signatera_xpath)
        ActionChains(self.driver).move_to_element(click_ourpeople).move_to_element(click_oncology).\
            move_to_element(click_signatera).click().perform()

