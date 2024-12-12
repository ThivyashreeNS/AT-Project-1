"""Project01TestCases.py"""

# Import necessary modules from Selenium and other libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Resources.Data import WebData
from Pages.LoginPage import LoginPage
from Pages.PIMPage import PIMPage

# Main test class inheriting WebData
class Project01TestCases(WebData):

    # Constructor for initializing the test class
    def __init__(self):
        self.url = WebData().url
        # Initializing Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)

        # Initialize the LoginPage class for login operations
        self.login_page = LoginPage(self.driver)
        # Initialize the PIMPage class for employee management operations
        self.pim_page = PIMPage(self.driver)

    # Test case for first login scenario
    def TC_Login_01(self):
        # Call the login method from LoginPage
        return self.login_page.login(2, 2)

    # Test case for second login scenario
    def TC_Login_02(self):
        return self.login_page.login(3, 3)

    # Test case for adding a new employee to PIM section
    def TC_PIM_01(self):
        # First, log in using credentials from row 4
        self.login_page.login(4, 4)
        # call the add_employee method from PIMPage to add a new employee
        return self.pim_page.add_employee()

    # Test case for editing an existing employee's details in PIM section
    def TC_PIM_02(self):
        self.login_page.login(5, 5)
        return self.pim_page.edit_employee()

    # Test case for deleting an employee from PIM section
    def TC_PIM_03(self):
        self.login_page.login(6, 6)
        return self.pim_page.delete_employee()

    # Method to close the browser after all tests are completed
    def close_driver(self):
        self.login_page.logout()  # Call the logout method before closing
        self.driver.quit()
