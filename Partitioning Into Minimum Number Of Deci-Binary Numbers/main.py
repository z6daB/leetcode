class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(map(int, n)))


sol = Solution()
print(sol.minPartitions(n="32"))