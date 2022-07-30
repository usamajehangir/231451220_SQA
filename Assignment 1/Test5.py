import unittest
import calc

class TestCase(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 2), 8)

if __name__ == '__main__':
    unittest.main()
