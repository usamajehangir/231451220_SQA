import unittest

class TestCase(unittest.TestCase):
    def test_lower(self):
        self.assertEqual('USAMA'.lower(), 'usama')

if __name__ == '__main__':
    unittest.main()
