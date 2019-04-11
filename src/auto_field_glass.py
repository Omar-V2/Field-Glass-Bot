import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import Credentials
from envar import EnvironmentVariables


driver = webdriver.Chrome()
driver.get("https://www.fieldglass.net/?next=%2Fworker_desktop.do")
username_field = driver.find_element_by_id("usernameId_new")
password_field = driver.find_element_by_id("passwordId_new")
# If you are entering your credentials in the credntials.py file (not recommended)
if Credentials.username and Credentials.password:
    username_field.send_keys(Credentials.username)
    password_field.send_keys(Credentials.password)
else: # using env variable method (recommended)
    username = os.environ.get(EnvironmentVariables.USERNAME_VAR) # Replace with the name of the evnironement variable you created
    password = os.environ.get(EnvironmentVariables.PASSWORD_VAR)
    if username and password:
        username_field.send_keys(username)
        password_field.send_keys(password)
    else:
        raise NameError("You have not created an environment variable for your field glass username and/or password")

driver.find_element_by_class_name("formLoginButton_new").click()
driver.find_element_by_link_text("Complete Time Sheet").click()

cell_paths = []

for i, j in zip(range(4, 8), [8, 11, 12, 17]): # these are the work intervals of the day
    cell_paths.append(["/html/body/div[3]/div[5]/div[1]/div[4]/div[2]/form/table/tbody/tr[{}]/td[1]/input".format(i), j])

for path in cell_paths:
    cell = driver.find_element_by_xpath(path[0])
    cell.send_keys(path[1])

for i in range(1, 5):
    driver.find_element_by_id("copyIcon_{}".format(i)).click()
    time.sleep(0.1)

[driver.find_element_by_xpath("//*[@id=\"t_z12061520440238615056a6f_b_{}_r1\"]".format(i)).send_keys(8) for i in range(1, 6)] 