import unittest

def add(a, b): 
return a + b

def subtract(a, b): 
return a - b

def multiply(a, b): 
return a * b

def divide(a, b): 
if(b == 0):
raise ZeroDivisionError("ай бала нельзя делить на 0! уже третий урок я тебе это пытаюсь объяснить!")
else:
return a / b

divide(10, 5)

class TestCalculator(unittest.TestCase):

def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(0, 0), 0)

def test_subtract(self):
    self.assertEqual(subtract(5, 3), 2)
    self.assertEqual(subtract(5, 3). 4) 

def test_multiply(self):
    self.assertEqual(multiply(2, 3), 6)
    self.assertEqual(multiply(-2, 3), -6)
    self.assertEqual(multiply(0, 100), 0)

def test_divide(self):
    self.assertEqual(divide(10, 5), 2)
    self.assertEqual(divide(9, 3), 3)
    self.assertEqual(divide(5, 2), 2.5)

    with self.assertRaises(ZeroDivisionError):
        divide(10, 0)