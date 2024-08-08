import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Personal_details import PersonalDetailsPage
from Utility import ExcelReader

@pytest.mark.usefixtures("setup_and_teardown")
class TestPersonalDetails:

    @pytest.mark.smoke
    @pytest.mark.parametrize("Fname,Mname,Lname,Employee_id,Othr_id,Lnumber,Exp_date,dob", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\PersonalDetailsData.xlsx", "PersonalDetails"))
    def test_personal_details(self, Fname, Mname, Lname, Employee_id, Othr_id, Lnumber, Exp_date, dob):
        personal_details_page = PersonalDetailsPage(self.driver)
        personal_details_page.valid_login()  
        personal_details_page.personalDetails(Fname, Mname, Lname, Employee_id, Othr_id, Lnumber, Exp_date, dob)
        personal_details_page.select_gender("female")
        personal_details_page.select_country("Indian")
        personal_details_page.select_status("Single")
        personal_details_page.save_details()
        personal_details_page.assert_details_saved_successfully()

    @pytest.mark.smoke
    @pytest.mark.parametrize("Fname,Mname,Lname", [("Monik", "Jayagopi", "J"),])
    def test_personal_details_mandatory(self, Fname, Mname, Lname):
        personal_details_page = PersonalDetailsPage(self.driver)
        personal_details_page.valid_login()  
        personal_details_page.personalDetails_mandatory(Fname, Mname, Lname)
        personal_details_page.save_details()
        personal_details_page.assert_details_saved_successfully()

    