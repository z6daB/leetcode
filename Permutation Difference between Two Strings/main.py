class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i in s:
            total += abs(s.index(i) - t.index(i))
        return total
