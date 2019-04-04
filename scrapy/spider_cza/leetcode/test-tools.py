import unittest

from . import First, FirstTestSet


class Test(unittest.TestCase):
    def test_First(self):
        res1 = First.solution1(FirstTestSet["nums"], FirstTestSet["target"])
        self.assertEqual(res1, FirstTestSet["res"])
        res2 = First.solution2(FirstTestSet["nums"], FirstTestSet["target"])
        self.assertEqual(res2, FirstTestSet["res"])


if __name__ == '__main__':
    unittest.main()
