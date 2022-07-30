import unittest
import calc

class TestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 10), 30)

if __name__ == '__main__':
    unittest.main()

