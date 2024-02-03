class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return(list((i, j)))

sol = Solution()
print(sol.twoSum([1, 2, 3], 4))