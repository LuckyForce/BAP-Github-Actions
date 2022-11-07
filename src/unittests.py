# Unit Tests
import unittest
import calculator

class TestStringMethods(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(calculator.calculate("5", "3", "+"), 8)

    def test_minus(self):
        self.assertEqual(calculator.calculate("5", "3", "-"), 2)

    def test_multiply(self):
        self.assertEqual(calculator.calculate("5", "3", "*"), 15)
    
    def test_divide(self):
        self.assertEqual(calculator.calculate("15", "3", "/"), 5)

if __name__ == '__main__':
    unittest.main()