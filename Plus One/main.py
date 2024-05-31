class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            number = ''
            for i in digits:
                number += str(i)
            number = int(number)
            number += 1
            digits = []
            for j in str(number):
                digits.append(int(j))
        return digits


sol = Solution()
print(sol.plusOne(digits=[1, 9, 9, 9]))
