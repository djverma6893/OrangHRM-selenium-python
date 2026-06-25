from PageObjects.Dashboard import Dashboard
from Utilities.Logger import LogGen
from Utilities.ReadConfig import ReadConfig
from TestCases.conftest import setup
import pytest
import time

class TestDashboard:
    log=LogGen.loggen()
    baseurl=ReadConfig.geturl()
    # baseurl = ReadConfig.geturl()
    # log = LogGen.loggen()
    @pytest.fixture(autouse=True)
    def driver_setup(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(10)
        self.dashob=Dashboard(self.driver)



    def test_dashboard_click(self):
        # self.dashob = Dashboard(self.driver)
        self.dashob.click_dashboard()
        self.log.info("Dashboard clicked")
        title=self.dashob.check_dashboard_title()
        self.log.info(title)
        if title=="Dashboard":
            # self.driver.quit()
            assert True
        else:
            # self.driver.quit()
            assert False
    def test_profile_options(self):
        opts=self.dashob.check_profile_options()
        self.log.info(opts)
        if len(opts)==4:
            assert True
        else:
            assert False
    def test_about(self):
        # dashob = Dashboard(self.driver)
        self.dashob.click_profile()
        text=self.dashob.click_about()
        self.log.info(f"title of about {text}")
        if text:
            assert True
        else:
            assert False

    def test_support(self):
        self.dashob.click_profile()
        text=self.dashob.click_support()
        self.log.info(f"title of support {text}")
        if text:
            assert True
        else:
            assert False
    def test_logout(self):
        self.dashob.click_profile()
        text=self.dashob.check_logout()
        self.log.info(f"title of logout {text}")
        if text:
            assert True
        else:
            assert False

    def test_time_work(self):
        text=self.dashob.check_time_at_work()
        self.log.info(f"title of time_work {text}")
        if text:
            assert True
        else:
            assert False
    def test_actions(self):
        text=self.dashob.check_my_actions()
        self.log.info(f"title of actions {text}")
        if text:
            self.log.info("test_actions passed")
            assert True
        else:
            self.log.info("test_actions failed")
            assert False
    def test_Quick_lunch(self):
        text=self.dashob.check_quick_lunch()
        self.log.info(f"title of quick_lunch {text}")
        if text:
            self.log.info("test_Quick_lunch passed")
            assert True
        else:
            self.log.info("test_Quick_lunch failed")
            assert False
    def test_buzz_post(self):
        text=self.dashob.check_latest_post()
        self.log.info(f"title of quick_lunch {text}")
        if text:
            self.log.info("test_buzz_post passed")
            assert True
        else:
            self.log.info("test_buzz_post failed")
            assert False

    def test_employee_leave(self):
        text=self.dashob.check_leave_section()
        self.log.info(f"title of quick_lunch {text}")
        if text:
            self.log.info("test_employee_leave passed")
            assert True
        else:
            self.log.info("test_employee_leave failed")
            assert False

    def test_employee_distribution(self):
        text=self.dashob.check_employee_distribution()
        self.log.info(f"title of quick_lunch {text}")
        if text:
            self.log.info("test_employee_distribution passed")
            assert True
        else:
            self.log.info("test_employee_distribution failed")
            assert False
    def test_employee_distribution_location(self):
        text=self.dashob.check_employment_distribution_location()
        self.log.info(f"title of quick_lunch  {text}")
        if text:
            self.log.info("test_employee_distribution_location passed")
            assert True
        else:
            self.log.info("test_employee_distribution_location failed")
            assert False
