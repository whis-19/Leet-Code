# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root) -> bool:
        if not root:
            return False
        if root.val == 0:
            return False
        if root.val == 1:
            return True
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        return root.val == 2 and (left or right) or (left and right)