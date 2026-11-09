# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        depth = 1
        if root is None:
            return []
        self.helper(root.left, depth, d)
        self.helper(root.right, depth, d)
        length = len(d.items()) + 1
        res = [] * (length)
        res.append([root.val])
        
        print(length)
        for i in range(length):
            if len(d[i]) > 0:
                res.append(d[i])
            # res[i] = d[i]
        return res
        

    def helper(self, node, depth, d):
        
        if not node:
            # d[depth].append(node)
            return
        d[depth].append(node.val)
        self.helper(node.left, depth+1, d)
        self.helper(node.right, depth+1, d)
        

        