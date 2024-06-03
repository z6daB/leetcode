class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        last = 0
        while first < len(s) and last < len(t):
            if s[first] == t[last]:
                last += 1
            first += 1
        return len(t) - last
