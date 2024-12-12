"""PIMPage.py"""

# Import necessary modules from Selenium and other libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resources.Locators import TestLocators
from Resources.Data import WebData
from Common.ExcelFunctions import ExcelFunctions

import sys
import os

# Add the parent directory of AT_Project_01 to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))



# Class to encapsulate actions related to the PIM page
class PIMPage:
    def __init__(self, driver):
        # Constructor to initialize the PIM page with the provided WebDriver instance.
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.xlobj = ExcelFunctions(WebData().excel_file, WebData().sheet_number)

    # Add a new employee
    def add_employee(self):
        # Navigate to PIM section
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().pim_text))).click()
        print("Navigated to PIM section")

        # Click the add button to add a new employee
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().add_button))).click()
        print("Clicked on Add button")

        # Input first name, middle name, and last name from WebData
        first = self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().first_name)))
        first.send_keys(WebData().firstname)
        print("Entered First Name")
        self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().middle_name))).send_keys(WebData().middlename)
        print("Entered Middle Name")
        self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().last_name))).send_keys(WebData().lastname)
        print("Entered Last Name")

        # Get the employee ID after adding an employee
        employee_id_box = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().employee_id_box)))
        employee_id = employee_id_box.get_attribute("value")
        print(employee_id)

        # Write the employee ID to Excel file
        self.xlobj.write_data(4, 13, employee_id)

        # Click save button
        save = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().save_button)))
        save.click()

        # Wait for and retrieve the toast message confirming addition
        toast_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().toast_add_msg)))
        save_toast_msg = toast_msg.text
        print(save_toast_msg)
        return save_toast_msg

    #  Edit an existing employee's details
    def edit_employee(self):
        # Navigate to PIM
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().pim_text))).click()

        # Search for the employee using previously saved employee ID
        employee_id = self.xlobj.read_data(4, 13)
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().employee_id_box))).send_keys(employee_id)
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().search_button)))
        search = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().search_button)))
        search.click()

        # Edit employee details
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().edit_button)))
        edit_emp = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().edit_button)))
        edit_emp.click()
        print("Clicked on Edit Button")

        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().personal_details))).click()
        print("Clicked on Personal Details")

        # Enter driver license number
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().driver_license_number))).send_keys(WebData.license_number)
        print("Entered Driver License Number")

        # Select nationality from dropdown
        dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().nationality_dropdown)))
        self.driver.execute_script("arguments[0].click();", dropdown)
        scroll = self.wait.until(EC.visibility_of_element_located((By.XPATH, TestLocators().nationality)))
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)
        self.driver.execute_script("arguments[0].click();", scroll)
        print("Selected Nationality: Indian")

        # Save changes
        save = self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().save_button)))
        save.click()

        # Wait for and get the toast message confirming the update
        toast_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().toast_update)))
        update_toast_msg = toast_msg.text
        print(update_toast_msg)
        return update_toast_msg

    #  Delete an existing employee based on employee ID.
    def delete_employee(self):
        # Navigate to PIM
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, TestLocators().pim_text))).click()

        # Search for employee
        employee_id = self.xlobj.read_data(4, 13)
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().employee_id_box))).send_keys(employee_id)
        self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().search_button))).click()

        # Delete employee details
        self.wait.until(EC.element_to_be_clickable((By.XPATH, TestLocators().trash_button))).click()
        delete_employee = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().delete_button)))
        delete_employee.click()

        # Wait and retrieve the text of the toast message confirming the deletion
        toast_msg = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().toast_delete_msg)))
        delete_toast_msg = toast_msg.text
        print(delete_toast_msg)
        return delete_toast_msg
