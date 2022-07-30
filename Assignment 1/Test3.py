import unittest

class TestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('usama'.upper(), 'USAMA')

if __name__ == '__main__':
    unittest.main()

    

