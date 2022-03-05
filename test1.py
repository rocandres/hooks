from funciones import saludar
import unittest

class TestSaludar(unittest.TestCase):

    def test_success(self):
        resultado= saludar("Andres")
        self.assertEqual(resultado,"Hola Andres")

    def test_dos(self):
        resultado= saludar("Andres")
        self.assertEqual(resultado,"Hola Andres")    

if __name__== '__main__':
    unittest.main()
