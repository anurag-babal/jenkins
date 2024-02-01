import unittest
from sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        result = sum(20, 35)
        self.assertEqual(result, 55)

if __name__ == '__main__':
    unittest.main()
