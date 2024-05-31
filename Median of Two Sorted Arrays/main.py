class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 != 0:
            midle = nums[int(len(nums) // 2)]
            return midle
        else:
            return (nums[int(len(nums) / 2)] + nums[int((len(nums) - 1) // 2)]) / 2

sol = Solution()
print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.