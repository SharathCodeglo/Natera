import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Scrolling the page will not achieve by "ActionChains"
# Instead of we can apply javascript language to achieve scrolling the page

# Scroll by Pixels
driver.execute_script("window.scrollBy(0,3000)")  # javascript builtin function
value = driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:", value)
time.sleep(2)

# Scroll by till the visible of element
India = driver.find_element(By.XPATH, "//td[normalize-space()='India']")
driver.execute_script("arguments[0].scrollIntoView();", India)
value = driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:", value)
time.sleep(2)

# Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:", value)
time.sleep(2)

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("No.of pixels moved:", value)

