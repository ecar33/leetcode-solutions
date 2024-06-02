class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def distributeCoins(self, root):
        def dfs(node):
            if not node:
                return 0
            
            left_coins = dfs(node.left)
            right_coins = dfs(node.right)
            total_coins = (node.val - 1) + left_coins + right_coins
            
            nonlocal moves
            moves += abs(total_coins)
            
            return total_coins
        
        moves = 0
        dfs(root)
        return moves
        
            
    
    
s = Solution()
root = TreeNode(3, TreeNode(0), TreeNode(2, TreeNode(0), TreeNode(0)))
print(s.distributeCoins(root))
        