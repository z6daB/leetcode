from typing import List

# I variant
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [nums[0]]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            dp.append(max(nums[i] + dp[i-1], nums[i]))
            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum

# II variant
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        max_sum = float('-inf')
        for i in range(len(nums)):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum
