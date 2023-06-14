# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.minHelper(root, float('-inf'), float('inf'))
    
    def minHelper(self, root, lowest, highest):
        if not root:
            return highest - lowest
        return min(self.minHelper(root.left, lowest, root.val), self.minHelper(root.right, root.val, highest))