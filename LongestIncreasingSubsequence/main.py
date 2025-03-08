class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_value = 1
        for i in range(1, len(nums)):
            sub = [dp[k] for k in range(i) if nums[k] < nums[i]]
            dp[i] = 1 + max(sub, default=0)
            if dp[i] > max_value:
                max_value = dp[i]
        return max_value
