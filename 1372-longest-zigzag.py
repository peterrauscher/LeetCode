from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigZagHelper(root, goLeft, visited):
            if root is None:
                return visited
            return max(
                zigZagHelper(root.left, False, visited + 1 if goLeft else 1),
                zigZagHelper(root.right, True, visited + 1 if not goLeft else 1),
            )

        return zigZagHelper(root, None, 0) - 1


s = Solution()
t = TreeNode(
    1,
    None,
    TreeNode(
        1,
        TreeNode(1, None, None),
        TreeNode(
            1,
            TreeNode(1, None, TreeNode(1, None, TreeNode(1, TreeNode(1, None, None)))),
            TreeNode(1, None, None),
        ),
    ),
)
print(s.longestZigZag(t))
