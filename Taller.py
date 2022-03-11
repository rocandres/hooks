import unittest
from selenium import webdriver
import unittest
from time import sleep
from warnings import filterwarnings
filterwarnings("ignore")


class TestSe(unittest.TestCase):

    def setUp(self) :
        self.browser= webdriver.Chrome(executable_path='./driver/chromedriver')


    def test_load(self):
        browser=self.browser
        browser.get("https://demo.guru99.com/test/login.html")
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