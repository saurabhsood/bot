
from selenium.webdriver.remote.webelement import WebElement
from driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
import time
class AmazonBot:

    url = 'https://www.amazon.in/dp/B08FVRQ7BZ/?colid=25Y6XQ3N6F5E2&coliid=I1YZ4JREIZ7BKY&ref_=wl_qv_pab'
    def __init__(self,browser):
        self.browser = browser
amazon= AmazonBot('') 
driv = Driver('c')
driv.initalizeWebDriver('a')
driv.openUrl(amazon.url)
#driv.driver.refresh()
while True:
    try:
        search_box = driv.driver.find_element_by_id('buy-now-button')
        search_box.click()
        address=driv.driver.find_element_by_id('address-book-entry-0')
        #print(address)
        address.find_element_by_link_text('Deliver to this address').click()
        break
    except:
            print('not in stock')
            time.sleep(5)
            driv.driver.refresh()

 


