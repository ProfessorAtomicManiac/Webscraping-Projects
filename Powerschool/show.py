from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas
import time

#python powerschool.py

driver = webdriver.Chrome()

driver.get("https://powerschool.ccs.k12.in.us/public/")

# To Log into Powerschool
driver.find_element_by_name('account').send_keys('username')
driver.find_element_by_id('fieldPassword').send_keys('password')
driver.find_element_by_id("btn-enter-sign-in").click()
driver.implicitly_wait(10)
driver.find_element_by_id("btn-directory").click()

names = []
addresses = []
phones = []

# How to skip pages while making several .csv files
for i in range(0, 0):
    nextVisible = EC.visibility_of_element_located((By.ID, "myGridNextPage"));
    WebDriverWait(driver, 1).until(nextVisible)
    driver.find_element_by_id("myGridNextPage").click()

# Getting the names/addresses
for i in range(1, 132):
    # Getting how many students are on a page
    names_clickable = EC.element_to_be_clickable((By.ID, "student_detail_pane"));
    WebDriverWait(driver, 5).until(names_clickable)
    students = driver.find_elements_by_id("student_detail_pane")
    namesLength = len(students)

    # Getting the Info
    for link in range(namesLength):
        # Wait since Powerschool has glitch of not loading in content when clicked too fast
        time.sleep(2)

        # Gets the student's name
        names.append(students[link].text)
        print(students[link].text)

        # Opens the pillar
        students[link].click()

        found = False

        try:
            # Finds phone/address to make sure the Pwerschool Glitch doesn't crash the program
            phone_visible = EC.visibility_of_element_located((By.ID, "student_detail_phone"));
            WebDriverWait(driver, 1).until(phone_visible)
            residence_visible = EC.visibility_of_element_located((By.ID, "student_detail_residence"));
            WebDriverWait(driver, 1).until(residence_visible)
            found = True

        except:
            # Makes sure if there's an error, it can be fitted into the .csv file
            print("Error")
            phones.append("Error")
            addresses.append("Error")
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()

        # If it finds the phone/address info, it will extract it
        if (found == True):
            phones.append(driver.find_element_by_id("student_detail_phone").text)
            print(driver.find_element_by_id("student_detail_phone").text)
            addresses.append(driver.find_element_by_id("student_detail_residence").text)
            print(driver.find_element_by_id("student_detail_residence").text)

            # Presses the key "Enter" to exit
            actions = ActionChains(driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()

    # Clicks the next button to go to the next page
    nextVisible = EC.visibility_of_element_located((By.ID, "myGridNextPage"));
    WebDriverWait(driver, 1).until(nextVisible)
    driver.find_element_by_id("myGridNextPage").click()

driver.quit()

# Convert to .csv file
studentsdf = pandas.DataFrame(
    {
        'Name': names,
        'Address': addresses,
        'Phone Number': phones
    })
#print(housesdf)
studentsdf.to_csv('students.csv')
