# PS5 Bot

This project contains bots for two websites.
Amazon
Shopatsc

We can purchase PS5 or other items using these two bots on chrome.

1. Setup
    * Install Python

    * Install Selenium using below command

      >   pip install selenium

2. Script Run
    * Import project on Visual Studio Code
    * Modify below line at driver.py

        >  chrome_options.add_argument("--user-data-dir=D:/Learning/bot/data/"+self.dataLoc.get(ws))

        Modify D:/Learning/bot/data with your path where you want to save your Chrome data.

    * Modify product url in amazon.py or shopatsc.py
        >   url = 'https://www.amazon.in/dp/B08FVRQ7BZ/?colid=25Y6XQ3N6F5E2&coliid=I1YZ4JREIZ7BKY&ref_=wl_qv_pab' 

        Replace this URL with your item which you want to purchase.

    * run amazon.py / shopatsc.py

To save your session details  , run the bot once and open new tab on the same window where amazon / shopatsc is running. Login into amazon/shopatsc. this will save your session details in one of the  session folder which we had specified earlier. Now close the browser and re run the script. You don't have to relogin to these websites again.

Before PS5 sale. Please run this script once on any product.

