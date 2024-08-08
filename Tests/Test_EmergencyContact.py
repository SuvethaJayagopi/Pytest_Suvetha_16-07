import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.EmergencyContact import EmergencyContactPage
from Utility import ExcelReader

@pytest.mark.usefixtures("setup_and_teardown")
class TestEmergencyContact:
    @pytest.mark.smoke
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "emergency"))
    def test_add_emergency_contact(self, name, relationship, telephone, mobile, work):  
        emergency_contact_page = EmergencyContactPage(self.driver)  
        emergency_contact_page.valid_login()  
        emergency_contact_page.emergencyContact(name, relationship, telephone, mobile, work)  
        emergency_contact_page.save_details()  
        emergency_contact_page.assert_update_message_displayed()

    @pytest.mark.regression
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "emergency"))
    def test_add_emergency_contact_cancel(self, name, relationship, telephone, mobile, work):  
        emergency_contact_page = EmergencyContactPage(self.driver)  
        emergency_contact_page.valid_login()  
        emergency_contact_page.emergencyContact(name, relationship, telephone, mobile, work)  
        emergency_contact_page.cancel_details()  

    @pytest.mark.smoke
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "mandatory"))
    def test_add_emergency_contact_mandatory(self, name, relationship, telephone, mobile, work):  
        emergency_contact_page = EmergencyContactPage(self.driver)  
        emergency_contact_page.valid_login()  
        emergency_contact_page.emergencyContact_mandatory(name, relationship, telephone)  
        emergency_contact_page.save_details()  
        emergency_contact_page.assert_update_message_displayed()

    @pytest.mark.smoke
    @pytest.mark.parametrize("name,relationship,telephone,mobile,work", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\EmergencyContactData.xlsx", "required"))
    def test_add_emergency_contact_required(self, name, relationship, telephone, mobile, work):  
        emergency_contact_page = EmergencyContactPage(self.driver)  
        emergency_contact_page.valid_login()  
        emergency_contact_page.emergencyContact_required(name, relationship)  
        emergency_contact_page.save_details()  
        emergency_contact_page.assert_error_message_displayed()

    
