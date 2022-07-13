import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0) # Switch to the frame
# driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("10/10/2022")

# Select month and year
year = "2022"
month = "August"
date = "15"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  # Selection Box

while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Next arrow

# Select date
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr//td[a]")

for ele in dates:
    if ele.text == date:
        ele.click()
        break


