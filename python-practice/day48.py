# Question: Day 48: Write unit tests for a mathematical function using unittest module.
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_mixed(self):
        self.assertEqual(add(5, -3), 2)

if __name__ == '__main__':
    unittest.main()
