import configparser

config = configparser.ConfigParser()
config.read("C:\\Users\\HP\\Desktop\\OrangHRM-Selenium-python\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def geturl():
        url=config.get("custom url","BaseUrl")
        return url
    @staticmethod
    def getusername():
        username=config.get("custom url","Username")
        return username
    @staticmethod
    def getpassword():
        password=config.get("custom url","Password")
        return password