from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from credentials import Credentials



driver = webdriver.Chrome()
driver.get("https://www.fieldglass.net/?next=%2Fworker_desktop.do")
username = driver.find_element_by_id("usernameId_new")
password = driver.find_element_by_id("passwordId_new")
username.send_keys(Credentials.u_f)
password.send_keys(Credentials.p_f)
driver.find_element_by_class_name("formLoginButton_new").click()
driver.find_element_by_link_text("Complete Time Sheet").click()

cell_paths = []

for i, j in zip(range(4, 8), [8, 11, 12, 17]): # these are the work intervals of the day
    cell_paths.append(["/html/body/div[3]/div[5]/div[1]/div[4]/div[2]/form/table/tbody/tr[{}]/td[1]/input".format(i), j])



for path in cell_paths:
    cell = driver.find_element_by_xpath(path[0])
    cell.send_keys(path[1])

[driver.find_element_by_id("copyIcon_{}".format(i)).click() for i in range(1, 5)]

[driver.find_element_by_xpath("//*[@id=\"t_z12061520440238615056a6f_b_{}_r1\"]".format(i)).send_keys(8) for i in range(1, 6)] 