from selenium.webdriver.common.by import By
from PageObjects.LoginObjects import LoginObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class PIMObjects:
    pim_xpath="//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a"
    add_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    # add_xpath="//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    firstname_xpath="//input[@name='firstName']"
    middlename_xpath="//input[@name='middleName']"
    lastname_xpath="//input[@name='lastName']"
    EmployeeId_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    save_xpath="//button[@type='submit']"
    otherId_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input"
    license_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input"
    #license expire date xpath has two element with same xpath 1st one is for license and 2nd one is for date of birth
    license_expire_xpath="//input[@placeholder='yyyy-dd-mm']"
    nationality_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div"
    marital_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div"
    male_xpath="//label[text()='Male']"
    female_xpath="//label[text()='Female']"
    #save button xpath hase 2 element
    save1_xpath="//button[@type='submit']"
    blood_type_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"
    test_field_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div[2]/div/div[2]/input"
    contact_details_xpath="//a[text()='Contact Details']"
    # contact_details_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]"
    street1_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input"
    street2_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input"
    city_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input"
    state_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input"
    pincode_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input"
    country_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]"
    #telephone
    home_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input"
    mobile_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input"
    work_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input"
    #email
    email_xpth="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input"
    other_email_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/input"
    #save contact details
    contact_save_xpath="//button[@type='submit']"






    def __init__(self, driver):
        self.driver = driver
        lgob = LoginObject(self.driver)
        lgob.setUsername("Admin")
        lgob.setPassword("admin123")
        lgob.clickLogin()
        time.sleep(3)

    def click_pim(self):
        return self.driver.find_element(By.XPATH,self.pim_xpath)
    def click_add_employee(self):
        self.driver.find_element(By.XPATH,self.add_xpath).click()
        time.sleep(3)
        title= self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6").text
        return title

    def set_firstname(self, username):
        element= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.firstname_xpath)))
        element.send_keys(username)
        # self.driver.find_element(By.XPATH,self.firstname_xpath).send_keys(username)
        # fname.clear()
        # fname.send_keys(firstname)

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
    def set_nationality(self,nationality1):
        nationality=self.driver.find_element(By.XPATH,self.nationality_xpath)
        nationality.click()
        act = ActionChains(self.driver)
        # act.send_keys(nationality1[0]).perform()
        text=""
        while text!=nationality1:
            act.send_keys(Keys.ARROW_DOWN).perform()
            # self.driver.get_attribute('class')
            text=nationality.text
            # text=nationality.send_keys(Keys.DOWN)
        act.send_keys(Keys.ENTER).perform()




        # nationality.clear()
        # nationality.send_keys(nationality)
    def set_maritalstatus(self, maritalstatus1):
        maritalstatus=self.driver.find_element(By.XPATH,self.marital_xpath)
        maritalstatus.click()
        act = ActionChains(self.driver)
        text=""
        while text!=maritalstatus1:
            act.send_keys(Keys.ARROW_DOWN).perform()
            text=maritalstatus.text
        act.send_keys(Keys.ENTER).perform()

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
        bltype.click()
        text=""
        act = ActionChains(self.driver)
        while text!=bloodtype:
            act.send_keys(Keys.ARROW_DOWN).perform()
            text=bltype.text
        act.send_keys(Keys.ENTER).perform()

    def set_testfield(self,testfield1):
        testfield=self.driver.find_element(By.XPATH, self.test_field_xpath)
        testfield.clear()
        testfield.send_keys(testfield1)

    def click_save2(self):
        save2=self.driver.find_elements(By.XPATH, self.save_xpath)[1]
        save2.click()



    def click_contact_details(self):
        contact_details= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.contact_details_xpath)))
        self.driver.execute_script("arguments[0].click();", contact_details)
        # contact_details.click()
    def set_street1(self, street1):
        stree=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, self.street1_xpath)))
        stree.send_keys(street1)
    def set_street2(self, street2):
        self.driver.find_element(By.XPATH, self.street2_xpath).send_keys(street2)

    def set_city(self, city):
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)
    def set_state(self, state):
        self.driver.find_element(By.XPATH, self.state_xpath).send_keys(state)
    def set_zipcode(self, zipcode):
        self.driver.find_element(By.XPATH, self.pincode_xpath).send_keys(zipcode)
    def set_country(self, country):
        cntry=self.driver.find_element(By.XPATH, self.country_xpath)
        cntry.click()
        act=ActionChains(self.driver)
        # act.send_keys(country[0]).perform()
        text=""
        while text!=country:
            text=cntry.text
            act.send_keys(Keys.ARROW_DOWN).perform()

        act.send_keys(Keys.ENTER).perform()
    # time.sleep(25)
    # set telephone details
    def set_home_contact(self, home_contact):
        self.driver.find_element(By.XPATH, self.home_xpath).send_keys(home_contact)
    def set_mobile_number(self, mobile_number):
        self.driver.find_element(By.XPATH, self.mobile_xpath).send_keys(mobile_number)
    def set_work_number(self, work_number):
        self.driver.find_element(By.XPATH, self.work_xpath).send_keys(work_number)
    #set email details

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.email_xpth).send_keys(email)
    def set_other_email(self, other_email):
        self.driver.find_element(By.XPATH, self.other_email_xpath).send_keys(other_email)

    def click_save_contacts(self):
        self.driver.find_element(By.XPATH, self.contact_save_xpath).click()




