# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree_visual(self, level=0, prefix=""):
        if self.val is None:
            print("Tree is empty.")
            return
        if self.right:
            self.right.print_tree_visual(level + 1, "    " * level + "    /")
        print("  " * level + f"{prefix} {self.val}")
        if self.left:
            self.left.print_tree_visual(level + 1, "    " * level + "    \\")
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        middle = len(nums) // 2

        root = TreeNode(nums[middle])

        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:])

        return root


sol = Solution()
sol.sortedArrayToBST(nums=[3, 1])
