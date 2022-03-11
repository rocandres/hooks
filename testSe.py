import unittest
from selenium import webdriver
import requests
import os
from time import sleep


class TestSe(unittest.TestCase):

    def setUp(self) :
        self.username = os.environ.get('USERNAME')
        self.authkey = os.environ.get('AUTHKEY')

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)

        self.test_result = None

        caps = {}
        caps['browserName'] = 'Chrome'
        caps['version'] = '60x64'
        caps['platform'] = 'Windows 10'
        caps['screenResolution'] = '1366x768'

        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )
        self.driver.implicitly_wait(20)
        
    def test_load(self):
        browser=self.browser
        browser.get("https://demo.guru99.com/test/login.html")
        self.driver.maximize_window()
        email=browser.find_element_by_id("email")
        email.send_keys('admin@gmail.com')
        sleep(1)
        password=browser.find_element_by_id("passwd")
        password.send_keys('demoadmin')
        sleep(1)
        buttonLogin=browser.find_element_by_id("SubmitLogin")
        buttonLogin.click()
        sleep(1)
        estado=browser.find_element_by_xpath("/html/body/div[4]/div/div/h3")
        self.assertIn("Successfully",estado.text," Ha fallado el inicio de sesión")

   
      
        

    def tearDown(self):
        self.browser.quit()    

if __name__== '__main__':
    unittest.main()