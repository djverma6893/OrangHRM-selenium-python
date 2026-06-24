import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.PIMObjects import PIMObjects
from TestCases.conftest import setup
from Utilities.ReadConfig import ReadConfig
from Utilities.Logger import LogGen
import time
# pytest.mark.usefixtures('setup')
class Test_002_add_new_employee:
    baseurl = ReadConfig.geturl()
    log= LogGen.loggen()
    # driver=setup
    # driver.get(baseurl)
    # driver.implicitly_wait(10)


    @pytest.fixture(autouse=True)
    def driver_setup(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.pimob = PIMObjects(self.driver)
        # self.pimob.click_pim()



    # @pytest.fixture(autouse=True)
    def test_click_pim(self):
        pim= self.pimob.click_pim()
        text= pim.text
        pim.click()
        self.log.info("     PIM clicked              ")
        # self.driver.close()
        assert (True if text=="PIM" else False)
    # @pytest.fixture(autouse=True)
    def test_add_employee(self):
        pim = self.pimob.click_pim()
        text = pim.text
        pim.click()
        self.log.info("     PIM clicked              ")
        add_emp_title= self.pimob.click_add_employee()
        self.log.info("     Add Employee clicked              ")
        self.pimob.set_firstname("alex")
        self.pimob.set_middlename("Salman")
        self.pimob.set_lastname("Mehta")
        self.log.info("     New employee full name has been filled    ")
        self.pimob.set_EmployeeID("5172")
        self.log.info(" new employee Id number is 5172")
        self.pimob.click_save()
        self.log.info("     Saved Employee basic details             ")
        time.sleep(5)
        self.pimob.set_license("2038420340")
        self.log.info("entered license number is 2038420340")
        self.pimob.set_licenseExpire("2029-01-01")
        self.log.info("license expire date is 2029-01-01")
        self.pimob.set_nationality("Indian")
        self.log.info("Nationality is Indian")
        self.pimob.set_maritalstatus("Single")
        self.log.info("Marital status is Single")
        self.pimob.set_dob("2003-01-01")
        self.log.info("DOB is 2003-01-01")
        self.pimob.set_gender("Male")
        self.log.info("Gender is Male")
        self.pimob.click_save1()
        self.log.info("personal details has been saved")
        self.pimob.set_bloodtype("AB-")
        self.log.info("blood type is AB-")
        self.pimob.set_testfield("Corona")
        self.log.info("testfield is Corona")
        self.pimob.click_save2()
        self.log.info("saved custom fields")
        self.pimob.click_contact_details()
        self.log.info("contact details has been clicked")
        self.pimob.set_street1("babuganj")
        self.log.info("street 1 is babuganj")
        self.pimob.set_street2("Tilouthu")
        self.log.info("street 2 is Tilouthu")
        self.pimob.set_city("Sasaram")
        self.log.info("city is Sasaram")
        self.pimob.set_state("Bihar")
        self.log.info("state is Bihar")
        self.pimob.set_zipcode("821312")
        self.log.info("zipcode is 821312")
        self.pimob.set_country("India")
        self.log.info("country is India")
        self.pimob.set_home_contact("6282392392")
        self.log.info("home contact is 6282392392")
        self.pimob.set_mobile_number("7766882232")
        self.log.info("mobile number is 7766882232")
        self.pimob.set_work_number("9283928332")
        self.log.info("work number is 9283928332")
        self.pimob.set_email("vermatest4141@gmail.com")
        self.log.info("email is vermatest4141@gmail")
        self.pimob.set_other_email("asdfjklgh@gmail.com")
        self.log.info("other email is asdfjklgh@gmail")
        self.pimob.click_save_contacts()
        self.log.info("contact details has been saved")

        time.sleep(5)



















