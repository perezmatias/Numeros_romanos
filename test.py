import unittest
from Convertir_a_Natural import convertir_a_naturales
import Convertir_a_Romanos

class PrimerTests(unittest.TestCase):
    def test_1(self): 
        resultado = convertir_a_naturales("I")
        self.assertEqual(resultado,1)
    def test_2(self): 
        resultado = convertir_a_naturales("II")
        self.assertEqual(resultado,2)
    def test_3(self): 
        resultado = convertir_a_naturales("III")
        self.assertEqual(resultado,3)
    def test_4(self): 
        resultado = convertir_a_naturales("IV")
        self.assertEqual(resultado,4)
    def test_5(self): 
        resultado = convertir_a_naturales("V")
        self.assertEqual(resultado,5)
    def test_6(self): 
        resultado = convertir_a_naturales("VI")
        self.assertEqual(resultado,6)
    def test_7(self): 
        resultado = convertir_a_naturales("VII")
        self.assertEqual(resultado,7)
    def test_8(self): 
        resultado = convertir_a_naturales("VIII")
        self.assertEqual(resultado,8)
    def test_9(self): 
        resultado = convertir_a_naturales("IX")
        self.assertEqual(resultado,9)
    def test_10(self): 
        resultado = convertir_a_naturales("X")
        self.assertEqual(resultado,10)
    def test_12(self): 
        resultado = convertir_a_naturales("XII")
        self.assertEqual(resultado,12)
    def test_13(self): 
        resultado = convertir_a_naturales("XIII")
        self.assertEqual(resultado,13)
    def test_15(self): 
        resultado = convertir_a_naturales("XV")
        self.assertEqual(resultado,15)
    def test_22(self): 
        resultado = convertir_a_naturales("XXII")
        self.assertEqual(resultado,22)
    def test_25(self): 
        resultado = convertir_a_naturales("XXV")
        self.assertEqual(resultado,25)
    def test_27(self): 
        resultado = convertir_a_naturales("XXVII")
        self.assertEqual(resultado,27)
    def test_38(self): 
        resultado = convertir_a_naturales("XXXVIII")
        self.assertEqual(resultado,38)
    def test_39(self): 
        resultado = convertir_a_naturales("XXXIX")
        self.assertEqual(resultado,39)
    def test_44(self): 
        resultado = convertir_a_naturales("XLIV")
        self.assertEqual(resultado,44)
    def test_52(self): 
        resultado = convertir_a_naturales("LII")
        self.assertEqual(resultado,52)
    def test_55(self): 
        resultado = convertir_a_naturales("LV")
        self.assertEqual(resultado,55)
    def test_69(self): 
        resultado = convertir_a_naturales("LXIX")
        self.assertEqual(resultado,69)
    def test_71(self): 
        resultado = convertir_a_naturales("LXXI")
        self.assertEqual(resultado,71)
    def test_88(self): 
        resultado = convertir_a_naturales("LXXXVIII")
        self.assertEqual(resultado,88)
    def test_100(self): 
        resultado = convertir_a_naturales("C")
        self.assertEqual(resultado,100)    
    def test_155(self): 
        resultado = convertir_a_naturales("CLV")
        self.assertEqual(resultado,155)
    def test_399(self): 
        resultado = convertir_a_naturales("CLXXVII")
        self.assertEqual(resultado,177)
    def test_399(self): 
        resultado = convertir_a_naturales("CLXXXIX")
        self.assertEqual(resultado,189)
    def test_222(self): 
        resultado = convertir_a_naturales("CCXXII")
        self.assertEqual(resultado,222)
    def test_350(self): 
        resultado = convertir_a_naturales("CCCL")
        self.assertEqual(resultado,350)
    def test_350(self): 
        resultado = convertir_a_naturales("CCCLXVI")
        self.assertEqual(resultado,366)
    
    def test_399(self): 
        resultado = convertir_a_naturales("CCCXCIX")
        self.assertEqual(resultado,399)
        
class TestRomanToNumber(unittest.TestCase):

    def test_1(self):
        roman = Convertir_a_Romanos.Roman(1)
        self.assertEqual(roman, "I")

    def test_4(self):
        roman = Convertir_a_Romanos.Roman(4)
        self.assertEqual(roman, "IV")

    def test_5(self):
        roman = Convertir_a_Romanos.Roman(5)
        self.assertEqual(roman, "V")

    def test_9(self):
        roman = Convertir_a_Romanos.Roman(9)
        self.assertEqual(roman, "IX")

    def test_10(self):
        roman = Convertir_a_Romanos.Roman(10)
        self.assertEqual(roman, "X")

    def test_40(self):
        roman = Convertir_a_Romanos.Roman(40)
        self.assertEqual(roman, "XL")

    def test_50(self):
        roman = Convertir_a_Romanos.Roman(50)
        self.assertEqual(roman, "L")

    def test_100(self):
        roman = Convertir_a_Romanos.Roman(100)
        self.assertEqual(roman, "C")
    
if __name__ == '__main__':
    unittest.main()