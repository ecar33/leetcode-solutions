class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root, target):
        def dfs_remove_leaf(node, target):
            if not node:
                return None
            
            node.left = self.dfs_remove_leaf(node.left)
            node.right = self.dfs_remove_left(node.right)
            
            if node.val == target and not node.left and not node.right:
                nonlocal changes
                changes = True
                return None
            return node
        
        changes = True
        while changes:
            changes = False
            root = dfs_remove_leaf(root, target)
            
        return root


root = TreeNode(1, TreeNode(2, TreeNode(2), TreeNode(3, TreeNode(2), TreeNode(4))))
target = 2

s = Solution
print(s.removeLeafNodes(root, 2))
