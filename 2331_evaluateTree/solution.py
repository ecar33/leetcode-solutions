# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Post order traversal which evaluated children then propogates up boolean values from leaves
    def evaluateTree(self, root) -> bool:
        if not root.left and not root.right:
            return root.val == 1

        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        if root.val == 3: # AND operation against children
            return left_val and right_val
        elif root.val == 2: # OR operation against children
            return left_val or right_val






s = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1)))
print(s.evaluateTree(root))