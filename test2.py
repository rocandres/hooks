from funciones import sumar
import unittest
import os

class TestSaludar(unittest.TestCase):

    def test_success(self):
        res=os.environ['prueba']
        print(res)
        self.assertEqual(res,"Sabado")

  

if __name__== '__main__':
    unittest.main()
