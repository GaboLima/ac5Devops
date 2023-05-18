from calculadora import Calculadora
from unittest import TestCase, main

class Testes (TestCase):
    def test_adc(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.adicao(10,1), 11)

    def test_sub(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.subtracao(10, 1), 9)

    def test_mult(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.multiplicacao(10, 1), 10)
    
    def test_div(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.divisao(10, 1), 10)    

if __name__ == "__main__":
    main()