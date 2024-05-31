class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        nums.append(target)
        nums.sort()
        return nums.index(target)


sol = Solution()
print(sol.searchInsert(nums=[1, 3, 5, 6], target=7))
