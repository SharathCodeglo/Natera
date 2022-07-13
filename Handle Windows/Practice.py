from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Selenium")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)

Results = driver.find_elements(By.PARTIAL_LINK_TEXT, "Selenium")
print(len(Results))

for res in Results:
    res.click()

Windows_IDs = driver.window_handles

for ID in Windows_IDs:
    driver.switch_to.window(ID)
    print(driver.title)
    time.sleep(3)
    if driver.title == "Selenium disulfide - Wikipedia" or driver.title == "Selenium in biology - Wikipedia":
        driver.close()

