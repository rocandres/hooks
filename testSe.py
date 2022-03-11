import unittest
from selenium import webdriver
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class LoginForm(unittest.TestCase):
    def setUp(self):

        # Put your username and authey below
        # You can find your authkey at crossbrowsertesting.com/account
        self.username = "andres.rodriguez.cabanzo@unillanos.edu.co"
        self.authkey  = "ucdfa57a0fe622ed"

        self.api_session = requests.Session()
        self.api_session.auth = (self.username,self.authkey)

        self.test_result = None

        caps = {}
        
        caps['name'] = 'Login Form Example'
        caps['build'] = '1.0'
        caps['browserName'] = 'Chrome'
        caps['version'] = '72'
        caps['platform'] = 'Windows 10'
        caps['record_network'] = 'false'

        # start the remote browser on our server
        self.driver = webdriver.Remote(
            desired_capabilities=caps,
            command_executor="http://%s:%s@hub.crossbrowsertesting.com:80/wd/hub"%(self.username,self.authkey)
        )

        

    def test_CBT(self):
        print('Loading Url')
        self.driver.get('https://demo.guru99.com/test/login.html')
        self.driver.maximize_window()
        print('Ingresando mail:')
        email= self.driver.find_element_by_id("email")
        email.send_keys('admin@gmail.com')
        sleep(1)
        print('Ingresando password:')
        password=self.driver.find_element_by_id("passwd")
        password.send_keys('demoadmin')
        sleep(1)
        print('Dando click a boton login:')
        buttonLogin=self.driver.find_element_by_id("SubmitLogin")
        buttonLogin.click()
        sleep(1)
        estado=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/h3")
        self.assertIn("Successfully",estado.text," Ha fallado el inicio de sesión")
        self.test_result = 'pass'

    def tearDown(self):
        print("Done with session %s" % self.driver.session_id)
        self.driver.quit()
        # Here we make the api call to set the test's score.
        # Pass it it passes, fail if an assertion fails, unset if the test didn't finish
        if self.test_result is not None:
            self.api_session.put('https://crossbrowsertesting.com/api/v3/selenium/' + self.driver.session_id,
                data={'action':'set_score', 'score':self.test_result})


if __name__ == '__main__':
    unittest.main()