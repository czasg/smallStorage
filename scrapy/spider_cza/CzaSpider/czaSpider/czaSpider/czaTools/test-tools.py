import os
import unittest

from img2num import img2num


class TestKNN(unittest.TestCase):
    def test_img(self):
        res = img2num(os.path.dirname(__file__)+os.sep+"2710386495.png")
        self.assertEqual(res, [int(i) for i in "2710386495"])

if __name__ == '__main__':
    unittest.main()