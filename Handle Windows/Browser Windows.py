import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
# driver.maximize_window()
window_ID = driver.current_window_handle
print(window_ID)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
All_ID = driver.window_handles
# print(All_ID)
#
# driver.switch_to.window(All_ID[1])
# print("Title of Child Window:", driver.title)
# time.sleep(3)
# driver.close()

# driver.switch_to.window(All_ID[0])
# print("Title of Parent Window:", driver.title)

# Approach 2
for ID in All_ID:
    driver.switch_to.window(ID)
    print(driver.title)
