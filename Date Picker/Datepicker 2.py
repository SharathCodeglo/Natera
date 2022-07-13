from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# Date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()  # Selection box of datepicker

month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
month.select_by_visible_text("Nov")
year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
year.select_by_visible_text("1994")

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr/td[a]")

for ele in dates:
    if ele.text == "1":
        ele.click()
        break

