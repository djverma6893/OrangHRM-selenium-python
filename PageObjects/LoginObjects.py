from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class LoginObject:
    username_xpath= "//input[@name='username']"
    password_xpath= "//input[@name='password']"
    login_xpath= "//button[@type='submit']"
    logout_xpath="//a[normalize-space()='Logout']"
    username_title_xpath="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[1]/label"
    password_title_xpath="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[1]/label"
    login_title_xpath="//*[@id='app']/div[1]/div/div[1]/div/div[2]/h5"
    forgotpass_title_xpath="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"
    resetPass_title_xpath="//*[@id='app']/div[1]/div[1]/div/form/h6"
    dashboard_xpath="//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span"
    def __init__(self, driver):
        self.driver = driver

    def getLogin_title(self):
        return self.driver.find_element(By.XPATH, self.login_title_xpath)

    def getUsername_title(self):
        return self.driver.find_element(By.XPATH, self.username_title_xpath)

    def getPassword_title(self):
        return self.driver.find_element(By.XPATH, self.password_title_xpath)

    def getresetpass_title(self):
        return self.driver.find_element(By.XPATH, self.resetPass_title_xpath)

    def getForgotpass_title(self):
        return self.driver.find_element(By.XPATH, self.forgotpass_title_xpath)

    def getdashboard_title(self):
        try:
            return self.driver.find_element(By.XPATH, self.dashboard_xpath).text
        except NoSuchElementException:
            return ""

    def setUsername(self, username):
        user = self.driver.find_element(By.XPATH, self.username_xpath)
        user.clear()
        user.send_keys(username)
    def setPassword(self, password):
        password_element = self.driver.find_element(By.XPATH, self.password_xpath)
        password_element.clear()
        password_element.send_keys(password)

    def clickLogin(self ):
        self.driver.find_element(By.XPATH, self.login_xpath).click()
    def clickLogout(self):
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[3]/ul/li").click()
        self.driver.find_element(By.XPATH, self.logout_xpath).click()


