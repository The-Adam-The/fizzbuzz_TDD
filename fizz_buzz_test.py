import unittest
from fizz_buzz import *

class TestCompare(unittest.TestCase):
    
    def test_fizz_buzz_3_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(3)) 
    
    def test_fizz_buzz_6_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(6)) 

    def test_fizz_buzz_9_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(9))

    def test_fizz_buzz_12_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(12)) 

    def test_fizz_buzz_18_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(18)) 
    
    def test_fizz_buzz_297_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(297))
    
    def test_fizz_buzz_59997_return_fizz(self):
        self.assertEqual("Fizz", fizz_buzz(59997))
   
    def test_fizz_buzz_5_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(5))

    def test_fizz_buzz_10_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(10))

    def test_fizz_buzz_20_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(20))

    def test_fizz_buzz_25_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(25))

    def test_fizz_buzz_50_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(50))

    def test_fizz_buzz_500_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(500))

    def test_fizz_buzz_5256564615_return_buzz(self):
        self.assertEqual("Buzz", fizz_buzz(5))

    def test_fizz_buzz_15_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15))
    
    def test_fizz_buzz_15_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(30))

    def test_fizz_buzz_45_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(45))

    def test_fizz_buzz_60_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(60))

    def test_fizz_buzz_75_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(75))

    def test_fizz_buzz_90_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(90))

    def test_fizz_buzz_150_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(150))

    def test_fizz_buzz_150000_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(150000))

    def test_fizz_buzz_15x99999_return_fizzbuzz(self):
        self.assertEqual("FizzBuzz", fizz_buzz(15*99999))

    def test_fizz_buzz_7_return_7(self):
        self.assertEqual("7", fizz_buzz(7))

    def test_fizz_buzz_multiples_15_return_fizz_buzz(self):
        for multi_15 in range(0, 1000000, 15):
            self.assertEqual("FizzBuzz", fizz_buzz(multi_15))

    def test_fizz_buzz_multiples_3_return_fizz(self):
        for multi_3 in range(0, 1000000, 3):
            if multi_3 % 15 == 0:
                continue
            self.assertEqual("Fizz", fizz_buzz(multi_3))
    
    def test_fizz_buzz_multiples_5_return_buzz(self):
        for multi_5 in range(0, 1000000, 5):
            if multi_5 % 15 == 0:
                continue
            self.assertEqual("Buzz", fizz_buzz(multi_5))


if __name__ == '__main__':
    unittest.main()