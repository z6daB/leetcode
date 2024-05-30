class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[c] = nums[r]
                c += 1
        return c