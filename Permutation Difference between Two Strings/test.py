import unittest
from main import Solution


class TestStr(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first(self):
        self.assertEqual(self.solution.findPermutationDifference(s="abc", t="bac"), 2)

    def test_second(self):
        self.assertEqual(self.solution.findPermutationDifference(s="abcde", t="edbac"), 12)


if __name__ == '__main__':
    unittest.main()
