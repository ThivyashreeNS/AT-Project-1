"""test_loginTestSuite.py"""
from Resources.Data import  WebData
# Import shared resources for test cases and Excel operations.
from Common.common import get_test_case_instance, xlobj

# Define a test function for the first login test case.
def test_TC_Login_01():
    # Get an instance of the Project01TestCases class.
    shree = get_test_case_instance()
    # Call the login test case method and get the current URL after login
    current_url, error = shree.TC_Login_01()
    # Check if the current URL matches the expected dashboard URL.
    if current_url == WebData.dashboard_url:
        # If logged in successfully, write a success message to the Excel file.
        xlobj.write_data(2, 11, "The user is logged in successfully.")
        assert True
    else:
        # If login failed, write an error message to the Excel file.
        xlobj.write_data(2, 11, "Invalid credentials")
        assert False
    # Close the driver after the test
    shree.close_driver()

# Define a test function for the second login test case.
def test_TC_Login_02():
    shree = get_test_case_instance()
    current_url, error_text = shree.TC_Login_02()
    if current_url == WebData.dashboard_url:
        xlobj.write_data(3, 11, "The user is logged in successfully.")
        # Assertion passes if login is successful.
        assert True
    else:
        # If login failed, write the error message to the Excel file.
        xlobj.write_data(3, 11, error_text)
        assert False
    # Close the driver after the test
    shree.close_driver()