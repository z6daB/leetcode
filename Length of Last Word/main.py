class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len((s.split())[-1])


sol = Solution()
print(sol.lengthOfLastWord(s="luffy is still joyboy    "))
