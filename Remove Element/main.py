class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


sol = Solution()
print(sol.removeElement(nums=[3, 2, 2, 3], val=3))
# Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
