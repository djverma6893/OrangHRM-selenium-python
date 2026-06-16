from selenium.webdriver.common.by import By
class LoginObject:
    username_xpath= "//input[@name='username']"
    password_xpath= "//input[@name='password']"
    login_xpath= "//button[@type='submit']"
    logout_xpath="//a[normalize-space()='Logout']"
    def __init__(self, driver):
        self.driver = driver


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
        self.driver.find_element(By.XPATH, self.logout_xpath).click()


