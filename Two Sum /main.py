class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp_set = nums[i + 1:]
            if target - nums[i] in temp_set:
                return i, nums[i + 1:].index(target - nums[i]) + i + 1
sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9))