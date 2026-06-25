from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.LoginObjects import LoginObject
import time
class Dashboard:
    dashboar_xpath="//span[text()='Dashboard']"
    title_xpath="//h6[text()= 'Dashboard']"
    upgrade_xpath="//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/a/button"
    profile_xpath="//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/img"
    dropdown_xpath="//ul[@class='oxd-dropdown-menu']/li"
     # page different sections
    time_at_work_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div/div[1]"
    my_action_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div/div[1]"
    Quick_lunch_xpaht="//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div/div[1]"
    Punch_time_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/button"
    buzz_post_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[4]/div/div[1]"
    Employeess_on_leave_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[5]/div/div[1]"
    Distribution_by_sub_unit_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[5]/div/div[1]"
    distribution_by_location_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[7]/div/div[1]/div"
    #about
    about_title_xpath="//*[@id='app']/div[2]/div/div/div/div[1]"
    about_close_xpath="//*[@id='app']/div[2]/div/div/div/button"
    #support
    sprt_title_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6"
    #logout
    login_title_xpath="//*[@id='app']/div[1]/div/div[1]/div/div[2]/h5"
    



    def __init__(self, driver):
        self.driver = driver
        lgob = LoginObject(self.driver)
        lgob.setUsername("Admin")
        lgob.setPassword("admin123")
        lgob.clickLogin()
        # wait=self.driver,10
        time.sleep(3)

    def click_dashboard(self):
        dash= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.dashboar_xpath)))
        dash.click()

    def check_dashboard_title(self):
        title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.title_xpath)))
        return title.text
    def click_profile(self):
        profile=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.profile_xpath)))
        profile.click()
    def check_upgrade(self):
        upgrade=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.upgrade_xpath)))
        upgrade.click()
        time.sleep(3)
        #Upgrade to Advanced from Open Source | OrangeHRM
        title=self.driver.title()
        self.driver.close()
        return title
        # return self.driver.title()

    def check_profile_options(self):
        self.click_profile()
        options=[]
        drpdwn=self.driver.find_elements(By.XPATH, self.dropdown_xpath)
        for option in drpdwn:
            print(option.text)
            options.append(option.text)

        return options
    def click_about(self):
        drpdwn = self.driver.find_elements(By.XPATH, self.dropdown_xpath)
        drpdwn[0].click()
        # aboutpopup=self.driver.switch_to_alert()
        # text=aboutpopup.text
        # aboutpopup.dismiss()
        title=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.about_title_xpath)))
        text=title.text
        self.driver.find_element(By.XPATH, self.about_close_xpath).click()
        return text


    def click_support(self):
        drpdwn = self.driver.find_elements(By.XPATH, self.dropdown_xpath)
        drpdwn[1].click()
        title=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.sprt_title_xpath)))
        text=title.text
        return text
    def check_logout(self):
        drpdwn = self.driver.find_elements(By.XPATH, self.dropdown_xpath)
        drpdwn[3].click()
        title = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.login_title_xpath)))
        text = title.text
        return text
    def check_time_at_work(self):

        title= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.time_at_work_xpath)))
        return title.text
    def check_my_actions(self):
        title= self.driver.find_element(By.XPATH, self.my_action_xpath)
        return title.text
    def check_quick_lunch(self):
        title= self.driver.find_element(By.XPATH, self.Quick_lunch_xpaht)
        return title.text
    def check_latest_post(self):
        title= self.driver.find_element(By.XPATH, self.buzz_post_xpath)
        return title.text
    def check_leave_section(self):
        title=self.driver.find_element(By.XPATH, self.Employeess_on_leave_xpath)
        return title.text
    def check_employee_distribution(self):
        title=self.driver.find_element(By.XPATH, self.Distribution_by_sub_unit_xpath)
        return title.text
    def check_employment_distribution_location(self):
        title=self.driver.find_element(By.XPATH, self.distribution_by_location_xpath)
        return title.text


