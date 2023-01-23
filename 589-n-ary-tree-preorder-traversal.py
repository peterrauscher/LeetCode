"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def helper(node, arr):
    if node == None:
        return
    arr.append(node.val)
    for e in node.children:
        helper(e, arr)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        traversal = []
        helper(root, traversal)
        return traversal