import unittest
import calc

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(12, 8), 20)

if __name__ == '__main__':
    unittest.main()
