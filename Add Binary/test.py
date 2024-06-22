import unittest
from main import Solution


class TestBinary(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_binary(self):
        self.assertEqual(self.solution.addBinary(a="11", b="1"), "100")

    def test_func(self):
        self.assertEqual(self.solution.addBinary(a="1010", b="1011"), "10101")


if __name__ == '__main__':
    unittest.main()
