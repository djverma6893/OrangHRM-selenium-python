import pytest
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






    def test_add_new_employee(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        pimob=PIMObjects(self.driver)
        pimob.click_pim()

        # self.driver.close()
        assert True
    # def test_add_click(self):
    #     pimob=PIMObjects(self.driver)
    #     pimob.click_add_employee()
    #
    #     time.sleep(5)
    #     self.driver.close()
    #     assert True






