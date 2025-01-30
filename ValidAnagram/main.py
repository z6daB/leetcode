# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        dct_first = {}
        dct_second = {}
        for i in range(n):
            dct_first[s[i]] = dct_first.get(s[i], 0) + 1
            dct_second[t[i]] = dct_second.get(t[i], 0) + 1
        return dct_first == dct_second
