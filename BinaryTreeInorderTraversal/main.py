# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        def search(node: Optional[TreeNode]):
            if not node:
                return
            search(node.left)
            if node.val is not None:
                result.append(node.val)
            search(node.right)

        search(root)
        return result
