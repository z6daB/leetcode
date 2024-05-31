class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return list(ans)


sol = Solution()
print(sol.singleNumber(nums=[1, 2, 1, 3, 2, 5]))
