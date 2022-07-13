from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "REGISTER").click()
dd_element = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))
# this above statement will select the dropdown to choose the option

# Select option from dropdown
# dd_element.select_by_visible_text("India")
# dd_element.select_by_value("12")
dd_element.select_by_index(10)

# capture all the options
all_options = dd_element.options
print(" Total options: ", len(all_options))

for opt in all_options:
    if opt.text == "India":
        opt.click()
        break

for option in all_options:
    print(option.text)
