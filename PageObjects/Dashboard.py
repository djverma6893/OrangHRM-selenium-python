from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObjects.LoginObjects import LoginObject
import time
class Dashboard:


    def __init__(self, driver):
        self.driver = driver
        lgob = LoginObject(self.driver)
        lgob.setUsername("Admin")
        lgob.setPassword("admin123")
        lgob.clickLogin()
        time.sleep(3)