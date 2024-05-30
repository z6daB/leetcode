class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            start = haystack.index(needle)
            end = start + len(needle)
            if haystack[start:end] == needle:
                return start

        else:
            return -1


sol = Solution()
print(sol.strStr(haystack="sadbutsad", needle="sad"))
