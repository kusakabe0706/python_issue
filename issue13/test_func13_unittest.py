import unittest
from func13 import add

class TestAddFunction(unittest.TestCase):

    def test_add_normal(self):
        # 3 + 5 + 7 = 15 になるかテスト (EXPECT_EQの代わり)
        self.assertEqual(add(3, 5, 7), 15)

    def test_add_negative(self):
        self.assertEqual(add(-1, -2, -3), -6)

    def test_add_zero(self):
        self.assertEqual(add(0, 0, 0), 0)

if __name__ == "__main__":
    unittest.main()