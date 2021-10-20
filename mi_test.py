import unittest
from saludo import Saludo

class Test_Saludo(unittest.TestCase):
    def test_1(self):
        a = Saludo()
        self.assertEqual(a.saludar(), "Hola")

if __name__ == "__main__":
    unittest.main()