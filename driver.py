from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
class Driver:
    
    fireFox_Driver='lib/geckodriver.exe'
    chrome_Driver='lib/chromedriver.exe'

    dataLoc={'a':'amazon','s':'shopatsc'}

    def __init__(self, browser):
        self.browser = browser
        self.driver=''

    def initalizeWebDriver(self,ws):
        driver=''
        if self.browser=='c':
            chrome_options = Options()
            chrome_options.add_argument("--user-data-dir=D:/Learning/bot/data/"+self.dataLoc.get(ws))
            driver = webdriver.Chrome(self.chrome_Driver,options=chrome_options)
        else:
            driver = webdriver.Firefox(executable_path = self.fireFox_Driver)
        self.driver = driver
    
    def openUrl(self,url):
        self.driver.get(url)


