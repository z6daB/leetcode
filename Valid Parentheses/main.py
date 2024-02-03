# 20. Valid Parentheses
# Given a string s containing just the characters ( ) [] { } determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type
#
# Input: s = "()"
# Output: true
#
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "(]"
# Output: false

class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in closeToOpen:
                # проверка первого и последнего элемента списка
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True


solution = Solution()
print(solution.isValid('([])'))
