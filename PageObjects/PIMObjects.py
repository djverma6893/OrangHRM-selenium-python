from selenium.webdriver.common.by import By
from PageObjects.LoginObjects import LoginObject
import time

class PIMObjects:
    pim_xpath="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    add_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    firstname_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    middlename_xpath="//input[@name='middleName']"
    lastname_xpath="//input[@name='lastName']"
    EmployeeId_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    save_xpath="//button[@type='submit']"
    otherId_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"
    license_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
    #license expire date xpath has two element with same xpath 1st one is for license and 2nd one is for date of birth
    license_expire_xpath="//input[@placeholder='yyyy-dd-mm']"
    nationality_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div"
    marital_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]"
    male_xpath="//label[text()='Male']"
    female_xpath="//label[text()='Female']"
    #save button xpath hase 2 element
    save1_xpath="//button[@type='submit']"
    blood_type_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    test_field_xpath="//*[@id='app']div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[2]/input"
    contact_details_xpath="//a[text()='Contact Details']"

    def __init__(self, driver):
        self.driver = driver
        lgob = LoginObject(self.driver)
        lgob.setUsername("Admin")
        lgob.setPassword("admin123")
        lgob.clickLogin()
        time.sleep(3)

    def click_pim(self):
        self.driver.find_element(By.XPATH,self.pim_xpath).click()
    def click_add_employee(self):
        self.driver.find_element(By.XPATH,self.add_xpath).click()

    def set_firstname(self,firstname):
        fname=self.driver.find_element(By.XPATH,self.firstname_xpath)
        fname.clear()
        fname.send_keys(firstname)

    def set_middlename(self, middlename):
        mname=self.driver.find_element(By.XPATH,self.middlename_xpath)
        mname.clear()
        mname.send_keys(middlename)
    def set_lastname(self, lastname):
        lname=self.driver.find_element(By.XPATH,self.lastname_xpath)
        lname.clear()
        lname.send_keys(lastname)
    def set_EmployeeID(self, EmployeeID):
        eId = self.driver.find_element(By.XPATH,self.EmployeeId_xpath)
        eId.clear()
        eId.send_keys(EmployeeID)
    def click_save(self):
        self.driver.find_element(By.XPATH,self.save_xpath).click()

    def set_otherID(self, otherID):
        otherID=self.driver.find_element(By.XPATH,self.otherId_xpath)
        otherID.clear()
        otherID.send_keys(otherID)
    def set_license(self,licenseNO):
        license_no=self.driver.find_element(By.XPATH,self.license_xpath)
        license_no.clear()
        license_no.send_keys(licenseNO)
    def set_licenseExpire(self,licenseexpire):
        license_expire=self.driver.find_elements(By.XPATH,self.license_expire_xpath)[0]
        license_expire.clear()
        license_expire.send_keys(licenseexpire)
    def set_nationality(self,nationality):
        nationality=self.driver.find_element(By.XPATH,self.nationality_xpath)
        nationality.clear()
        nationality.send_keys(nationality)
    def set_maritalstatus(self, maritalstatus):
        maritalstatus=self.driver.find_element(By.XPATH,self.marital_xpath)
        maritalstatus.clear()
        maritalstatus.send_keys(maritalstatus)
    def set_dob(self,dob):
        db= self.driver.find_elements(By.XPATH, self.license_expire_xpath)[1]
        db.clear()
        db.send_keys(dob)
    def set_gender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH, self.male_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.female_xpath).click()
    def click_save1(self):
        save1=self.driver.find_elements(By.XPATH,self.save1_xpath)[0]
        save1.click()
    def set_bloodtype(self,bloodtype):
        bltype=self.driver.find_element(By.XPATH, self.blood_type_xpath)
        bltype.clear()
        bltype.send_keys(bloodtype)
    def set_testfield(self,testfield):
        testfield=self.driver.find_element(By.XPATH, self.test_field_xpath)
        testfield.clear()
        testfield.send_keys(testfield)

    def click_save2(self):
        save2=self.driver.find_elements(By.XPATH, self.save_xpath)[1]
        save2.click()






