# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recur(root, 0)

    def recur(self, node, depth):
        if not node: return depth

        depth += 1
        l_d = depth
        r_d = depth
        if node.left:
            l_d = self.recur(node.left, depth)
        if node.right:
            r_d = self.recur(node.right, depth)
        return max(l_d, r_d)
