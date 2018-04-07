import unittest
from bubble_sort import bubble_sort
import random



class SortAlgorithmsTest(unittest.TestCase):

    def setUp(self):
        random.seed(42)
        self.sl = [i for i in range(100)]
        self.test_list = self.sl
        random.shuffle(self.sl)

    def test_bubble_sort(self):
        ol = bubble_sort(self.sl)
        self.assertEqual(self.test_list, ol)

if __name__ == '__main__':
    unittest.main()
