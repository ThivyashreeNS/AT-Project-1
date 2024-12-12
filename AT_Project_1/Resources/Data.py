"""
Data.py
This Python file holds basic data """
import os
class WebData:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    # Correct relative path to the Excel file using os.path.join
    excel_file =  os.path.join(os.path.dirname(__file__), '..', 'Resources', 'test_data.xlsx')
    sheet_number = "DataSheet"

    firstname = "Naruto"
    middlename = "Uzu"
    lastname = "maki"
    photo = os.path.join(os.path.dirname(__file__), '..', 'Resources', 'butterfly.jpeg')

    license_number = "1234567890"

