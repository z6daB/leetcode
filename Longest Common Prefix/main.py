class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_lenght = min(len(char) for char in strs)
        pref = ""
        for i in range(min_lenght):
            current = strs[0][i]
            print(current)
            for string in strs:
                if string[i] != current:
                    return pref
            pref += current
        return pref


sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
