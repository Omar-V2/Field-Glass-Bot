import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


# open the browser, go to fieldglass and locate login input fields
driver = webdriver.Chrome()
driver.get("https://www.fieldglass.net/?next=%2Fworker_desktop.do")
username_field = driver.find_element_by_id("usernameId_new")
password_field = driver.find_element_by_id("passwordId_new")

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

driver.find_element_by_class_name("formLoginButton_new").click()
driver.find_element_by_link_text("Complete Time Sheet").click()

cell_paths = []

for i, j in zip(range(4, 8), [8, 11, 12, 17]): # these are the work intervals of the day
    cell_paths.append(["/html/body/div[3]/div[5]/div[1]/div[4]/div[2]/form/table/tbody/tr[{}]/td[1]/input".format(i), j])

for path in cell_paths:
    cell = driver.find_element_by_xpath(path[0])
    cell.send_keys(path[1])
cell.send_keys(Keys.ENTER)

for i in range(1, 5):
    driver.find_element_by_id("copyIcon_{}".format(i)).click()
    time.sleep(0.1)

[driver.find_element_by_xpath("//*[@id=\"t_z12061520440238615056a6f_b_{}_r1\"]".format(i)).send_keys(8) for i in range(1, 6)] 