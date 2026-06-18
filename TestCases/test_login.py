import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.LoginObjects import LoginObject
from Utilities.ReadConfig import ReadConfig
from Utilities.Logger import LogGen
import time

class Test_001_login:
    baseurl= ReadConfig.geturl()
    username= ReadConfig.getusername()
    password= ReadConfig.getpassword()
    logger= LogGen.loggen()

    def test_homepage_title(self,setup):
        self.driver = setup
        self.logger.info("********* Setup complete *********")
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        title= self.driver.title
        self.logger.info(f"{title} page title")
        if title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

    def test_login_title(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        lgob=LoginObject(self.driver)
        text=lgob.getLogin_title().text
        if text == "Login":
            self.logger.info(f" correct Login tile ***{text}***")
            self.driver.close()
            assert True
        else:
            self.logger.info(f" failed username tile ***{text}*** ")
            self.driver.close()
            assert False

    def test_username(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        lgob=LoginObject(self.driver)

        text=lgob.getUsername_title().text
        if text == "Username":
            self.logger.info(f" correct username tile {text} ")
            self.driver.close()
            assert True
        else:
            self.logger.info(f" failed username tile {text} ")
            self.driver.close()
            assert False
    def test_password(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        lgob=LoginObject(self.driver)

        text=lgob.getPassword_title().text
        print(text)
        if text == "Password":
            self.logger.info(f" correct Password tile {text} ")
            self.driver.close()
            assert True
        else:
            self.logger.info(f" failed Password tile {text} ")
            self.driver.close()
            assert False
    def test_forgot_password_title(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        lgob=LoginObject(self.driver)

        text=lgob.getForgotpass_title().text
        print(text)
        if text == "Forgot your password?":
            self.logger.info(f" correct Password tile {text} ")
            self.driver.close()
            assert True
        else:
            self.logger.info(f" failed Password tile {text} ")
            self.driver.close()
            assert False
    def test_forgot_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        lgob=LoginObject(self.driver)
        lgob.getForgotpass_title().click()
        text= lgob.getresetpass_title().text
        if text == "Reset Password":
            self.logger.info(" successfully landed on reset password page")
            self.driver.close()
            assert True
        else:
            self.logger.info(f" failed to land on reset password page")
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
        self.logger.info("    Login clicked    ")
        time.sleep(5)
        title = self.driver.title
        dashboard = self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span" ).text
        if dashboard == "Dashboard":
            self.logger.info("  Login completed    ")
            self.driver.close()

            assert True
        else:
            self.logger.info("  Login failed    ")
            self.driver.close()
            assert False

    def test_logout(self, setup):
        driver = setup
        driver.get(self.baseurl)
        driver.implicitly_wait(10)
        lgob=LoginObject(driver)
        lgob.setUsername(self.username)
        lgob.setPassword(self.password)
        lgob.clickLogin()
        time.sleep(5)
        lgob.clickLogout()
        self.logger.info("    Logout clicked    ")
        if lgob.getLogin_title():
            self.logger.info("successfully landed on login page")
            driver.close()
            assert True
        else:
            self.logger.info("    Logout failed    ")
            driver.close()
            assert False


