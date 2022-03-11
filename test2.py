from funciones import sumar
import unittest
import os
from funciones import saludar

class TestSaludar(unittest.TestCase):

    def test_success(self):
        resultado= saludar("Andres")
        self.assertEqual(resultado,"Hola Andres")

  

if __name__== '__main__':
    unittest.main()
