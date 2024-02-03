# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1 = l1[::-1]
        l2 = l2[::-1]
        first_num = ''
        second_num = ''
        for num in l1:
            first_num += str(num)
        for num in l2:
            second_num += str(num)
        result = int(first_num) + int(second_num)
        finish = []
        for j in str(result):
            finish.append(int(j))
        return finish[::-1]

sol = Solution()
print(sol.addTwoNumbers([2,4,3], [5,6,4]))
