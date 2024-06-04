# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         letters = {}
#         for char in s:
#             if char not in letters:
#                 letters[char] = 1
#             else:
#                 letters[char] += 1
#         result = 0
#         odd = 0
#
#         if len(letters) == 1:
#             return letters[s[0]]
#         for i in letters.values():
#             if i > 1:
#                 if i % 2 == 0:
#                     result += i
#                 else:
#                     result += i - 1
#                     odd += 1
#             else:
#                 odd += 1
#
#         if odd > 0:
#             result += 1
#
#         return result

class Solution:
    def longestPalindrome(self, s: str) -> int:
        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)
        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)


