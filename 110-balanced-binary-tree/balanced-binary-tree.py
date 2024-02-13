# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root) -> int:
        if root is None: return 0
        return max(1 + self.depth(root.left), 1 + self.depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)