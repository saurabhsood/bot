
from typing import KeysView
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec, wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException
class ShopatSCBot:

    url = 'https://shopatsc.com/collections/playstation-5/products/playstation5-digital-edition'
begintime = datetime.now()
amazon= ShopatSCBot() 
driv = Driver('c')
driv.initalizeWebDriver('s')
driv.openUrl(amazon.url)
#driv.driver.refresh()
waitTime=10000
while True:
    try:
        wdwait = WebDriverWait(driv.driver, waitTime)
        search_box = driv.driver.find_element_by_name("shopify_product_id")
        val= search_box.get_property("value")
        val='groups-btn prod_id_'+val
        #print(val)
        addbutton = driv.driver.find_elements_by_xpath('//div[@class = "'+val+'"]')
        addcbutton = addbutton[0].find_element_by_id('product-add-to-cart')
        addcbutton.click()
        cart= driv.driver.find_element_by_id('dropdown-cart')
        WebDriverWait(cart, waitTime).until(ec.element_to_be_clickable((By.XPATH, '//a[@class = "btn btn-view-cart"]'))).click()
        #Proceed From Cart
        cartdiv = driv.driver.find_element_by_xpath('//div[@class = "box-title"]')
        cartbutton = wdwait.until(ec.element_to_be_clickable((By.XPATH, '//input[@id = "checkout_button"]')))
        cartbutton.click()
        #print(check.get_property('value'))
        #check.submit()
        #check.submit()
        #print(tr.find_element_by_link_text('View Cart'))

        #form
        try: 
            
            out_button = wdwait.until(ec.element_to_be_clickable((By.ID, 'continue_button')))
            fName = driv.driver.find_element_by_id('checkout_shipping_address_first_name')
            fName.send_keys('Saurabh')
            lName = driv.driver.find_element_by_id('checkout_shipping_address_last_name')
            lName.send_keys('Sood')
            address = driv.driver.find_element_by_id('checkout_shipping_address_address1')
            address.send_keys('Block C4F Janakpuri')
            address2 = driv.driver.find_element_by_id('checkout_shipping_address_address2')
            address2.send_keys('C4F-171')
            city = driv.driver.find_element_by_id('checkout_shipping_address_city')
            city.send_keys('New Delhi')
            country = driv.driver.find_element_by_id('checkout_shipping_address_country')
            country.send_keys('India')
            state = driv.driver.find_element_by_id('checkout_shipping_address_province')
            state.send_keys('Delhi')
            zip = driv.driver.find_element_by_id('checkout_shipping_address_zip')
            zip.send_keys('Delhi')
            phone = driv.driver.find_element_by_id('checkout_shipping_address_phone')
            phone.send_keys('9999837894')
            out_button.click()
            #complete order
            wdwait.until(ec.element_to_be_clickable((By.ID, 'continue_button'))).click()
            #payment check
            wdwait.until(ec.element_to_be_clickable((By.ID, 'continue_button'))).click()
        except:
            wdwait.until(ec.element_to_be_clickable((By.ID, 'continue_button'))).click()
            wdwait.until(ec.element_to_be_clickable((By.ID, 'continue_button'))).click()    
        break
    except :
        print('not in stock')
        time.sleep(1)
        driv.openUrl(amazon.url)
        
print(datetime.now()-begintime)
time.sleep(100000)
    
   
       

 


