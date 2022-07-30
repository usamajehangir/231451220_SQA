import unittest
import calc

class TestCases(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(12, 8), 20)

    def test_multiply(self):
        self.assertEqual(calc.multiply(3, 10), 30)

    def test_upper(self):
        self.assertEqual('usama'.upper(), 'USAMA')

    def test_lower(self):
        self.assertEqual('USAMA'.lower(), 'usama')

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 2), 8)

if __name__ == '__main__':
    unittest.main()
