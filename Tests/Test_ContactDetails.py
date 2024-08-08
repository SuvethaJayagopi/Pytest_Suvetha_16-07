import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Contact_details import ContactDetailsPage
from Utility import ExcelReader

@pytest.mark.usefixtures("setup_and_teardown")
class TestContactDetails:
    @pytest.mark.smoke
    @pytest.mark.parametrize("street1,street2,city,state,zip_code,home,mobile,work,work_email,other_email", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\ContactData.xlsx", "contact"))
    def test_contact_details_same_email(self, street1, street2, city, state, zip_code, home, mobile, work, work_email, other_email):
        contact_details_page = ContactDetailsPage(self.driver)
        contact_details_page.valid_login()  
        contact_details_page.contactDetails(street1, street2, city, state, zip_code, home, mobile, work, work_email, other_email)
        contact_details_page.select_country("Algeria")
        contact_details_page.save_details()
        contact_details_page.assert_details_saved_successfully() 

    @pytest.mark.smoke
    @pytest.mark.parametrize("street1,street2,city,state,zip_code,home,mobile,work,work_email,other_email", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\ContactData.xlsx", "sameEmail"))
    def test_contact_details_different_email(self, street1, street2, city, state, zip_code, home, mobile, work, work_email, other_email):
        contact_details_page = ContactDetailsPage(self.driver)
        contact_details_page.valid_login()  
        contact_details_page.contactDetails(street1, street2, city, state, zip_code, home, mobile, work, work_email, other_email)
        contact_details_page.select_country("Algeria")
        contact_details_page.save_details()
        contact_details_page.assert_same_email_error_displayed()