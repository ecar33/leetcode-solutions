class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root, target):
        def dfs_remove_leaf(node):
            if not node:
                return None
            
            # Recursively call on the left and right children
            node.left = dfs_remove_leaf(node.left)
            node.right = dfs_remove_leaf(node.right)
            
            # If the current node is a leaf and its value is the target, remove it
            if node.val == target and not node.left and not node.right:
                return None
            
            return node
        
        return dfs_remove_leaf(root)

def print_tree(node, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

root = TreeNode(1, TreeNode(3, TreeNode(2), TreeNode(3, TreeNode(2), TreeNode(4))), TreeNode(3))
target = 2

s = Solution()
new_root = s.removeLeafNodes(root, 2)
print(print_tree(new_root))
