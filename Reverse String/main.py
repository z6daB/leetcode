class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        return s


sol = Solution()
print(sol.reverseString(s=["h", "e", "l", "l", "o"]))
