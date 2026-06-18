from Utilities import XLUtils
from Utilities.Logger import LogGen
from Utilities.ReadConfig import ReadConfig
from PageObjects.LoginObjects import LoginObject
import time
import pytest

class Test_LoginDDT:
    xl= XLUtils
    baseurl=ReadConfig.geturl()
    # username=ReadConfig.getusername()
    # password=ReadConfig.getpassword()
    log = LogGen.loggen()
    xlpath="C:\\Users\\HP\\Desktop\\OrangHRM-Selenium-python\\TestData\\LoginDDT.xlsx"
    sheetname= "Sheet1"



    def test_login_ddt(self,setup):
        driver = setup
        driver.get(self.baseurl)
        driver.implicitly_wait(10)
        driver.maximize_window()
        rowcount= self.xl.getRowCount(self.xlpath,self.sheetname)
        self.xl.writedata(self.xlpath, self.sheetname, 1,4, "Test Case")
        statuslist=[]
        for r in range(2,rowcount+1):
            username= self.xl.readData(self.xlpath,self.sheetname,r,1,)
            password = self.xl.readData(self.xlpath,self.sheetname,r,2,)
            expect= self.xl.readData(self.xlpath,self.sheetname,r,3,)
            lgob= LoginObject(driver)
            lgob.setUsername(username)
            lgob.setPassword(password)
            lgob.clickLogin()
            time.sleep(5)
            text= lgob.getdashboard_title()
            if text =="Dashboard":
                if expect == "pass":
                    self.log.info("successfully logged in and meet the expectation")
                    lgob.clickLogout()
                    # driver.close()
                    self.xl.writedata(self.xlpath,self.sheetname,r,4,"pass")
                    statuslist.append("Pass")

                else:
                    self.log.info("successfully logged in but unbale to  meet the expectation")
                    lgob.clickLogout()
                    self.xl.writedata(self.xlpath, self.sheetname, r, 4, "fail")
                    statuslist.append("Fail")
                    # driver.close()

            else:
                if expect =="fail":
                    self.log.info("invalid credentials and meet the expectations")
                    self.xl.writedata(self.xlpath, self.sheetname, r, 4, "pass")
                    statuslist.append("Pass")
                    # driver.close()

                else:
                    self.log.info("invalid credentials but unable to meet the expectations")
                    self.xl.writedata(self.xlpath, self.sheetname, r, 4, "fail")
                    statuslist.append("Fail")
                    # driver.close()

        if "Fail" in statuslist:
            driver.close()
            assert False
        else:
            driver.close()
            assert True






