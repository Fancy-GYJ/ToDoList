import random
import unittest

"""
单独执行测试用例: python3 -m unittest
test_number.py
"""


class TestSequenceFunctions(unittest.TestCase):
    """
     setUp() 和 tearDown() 方法分别在各测试前后运行,并且名字以 test_ 开头的函数都作为测试
 执行。

 """

    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
            for element in random.sample(self.seq, 5):
                self.assertTrue(element in self.seq)


    def tearDown(self):
        del self.seq