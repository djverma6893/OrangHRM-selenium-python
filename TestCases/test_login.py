import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginObjects import LoginObject
from Utilities.ReadConfig import ReadConfig
import time

class Test_001_login:
    baseurl= ReadConfig.geturl()
    username= ReadConfig.getusername()
    password= ReadConfig.getpassword()

    def test_homepage_title(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        title= self.driver.title
        if title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        lgob=LoginObject(self.driver)
        lgob.setUsername(self.username)
        lgob.setPassword(self.password)
        lgob.clickLogin()

        time.sleep(5)
        title = self.driver.title
        dashboard = self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span" ).text
        if dashboard == "Dashboard":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False


