"""LoginPage.py"""

# Import necessary modules from Selenium and other libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Resources.Locators import TestLocators
from Resources.Data import WebData
from Common.ExcelFunctions import ExcelFunctions

# Class have the login page functionality
class LoginPage:
    # Constructor to initialize the login page with the provided WebDriver instance.
    def __init__(self, driver):
        # Storing the driver instance
        self.driver = driver
        # Initializing WebDriverWait for waiting for conditions
        self.wait = WebDriverWait(self.driver, 20)
        # Initialize ExcelFunctions for data handling
        self.xlobj = ExcelFunctions(WebData().excel_file, WebData().sheet_number)

    # Login method using credentials from Excel.
    def login(self, username_row, password_row):
        # Read username and password from Excel
        username = self.xlobj.read_data(username_row, 9)
        password = self.xlobj.read_data(password_row, 10)

        try:
            # Wait for the username & password field and input data, then click login.
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().username_name))).send_keys(username)
            self.wait.until(EC.presence_of_element_located((By.NAME, TestLocators().password_name))).send_keys(password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().login_button))).click()

            # Check for error message if the login was unsuccessful
            try:
                error_element = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().error_element)))
                # If the error element is visible, get the error text
                if error_element.is_displayed():
                    error_text = error_element.text
                    print("Login failed:", error_text)
                    return self.driver.current_url, error_text  # Return current URL and error text
            # Return any exceptions encountered
            except Exception as error:
                pass  # Login successful if no error

            print("Login successful.")
            return self.driver.current_url, None

        # Return current URL after successful login
        except Exception as error:
            print("Error during login:", error)
            return self.driver.current_url, error

    # Logout method
    def logout(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().logout_dropdown))).click()
            # Wait for and click the logout button
            logout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, TestLocators().logout_button)))
            logout_button.click()

            print("Logout successful.")
        except Exception as error:
            print("Error during logout:", error)