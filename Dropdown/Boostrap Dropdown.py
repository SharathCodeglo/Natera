from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.natera.com/oncology/signatera-advanced-cancer-detection/")
driver.maximize_window()

company = driver.find_element(By.XPATH, "//span[normalize-space()='Company']")
about_us = driver.find_element(By.XPATH, "//span[normalize-space()='About Us']")

ActionChains(driver).move_to_element(company).move_to_element(about_us).click().perform()


