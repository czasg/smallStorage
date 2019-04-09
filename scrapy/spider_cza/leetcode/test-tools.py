import unittest

from . import First, FirstTestSet  # pass
from . import Second, SecondTestSet  # pass
from . import Third, ThirdTestSet  # pass
from . import Fourth, FourthTestSet  # pass


class Test(unittest.TestCase):
    def test_fourth(self):
        res1 = Fourth.solution1(FourthTestSet["str"])
        self.assertEqual(res1, FourthTestSet["res"])

    def test_third(self):
        res1 = Third.solution1(ThirdTestSet["s1"])
        self.assertEqual(res1, ThirdTestSet["res"])

    def test_Second(self):
        res1 = Second.solution1(SecondTestSet["l1"], SecondTestSet["l2"])
        self.assertEqual(res1, SecondTestSet["res"])

    def test_First(self):
        res1 = First.solution1(FirstTestSet["nums"], FirstTestSet["target"])
        self.assertEqual(res1, FirstTestSet["res"])
        res2 = First.solution2(FirstTestSet["nums"], FirstTestSet["target"])
        self.assertEqual(res2, FirstTestSet["res"])


if __name__ == '__main__':
    unittest.main()
