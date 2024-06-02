class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # The value of the node
        self.left = left     # Reference to the left child TreeNode
        self.right = right   # Reference to the right child TreeNode

    
class Solution:
    def longestZigZag(self, root):
        self.max_length = 0

        def dfs(node, is_left, length):
            if not node:
                return
            
            self.max_length = max(self.max_length, length)
            
            if is_left:
                dfs(node.right, False, length + 1)
            else:
                dfs(node.left, True, length + 1)
        
            dfs(node.left, True, 1)
            dfs(node.right, False, 1)
        
        dfs(root, True, 0)
        dfs(root, False, 0)
        
        return self.max_length - 1


if __name__ == "__main__":
    # Create nodes
    node11 = TreeNode(1)  # This will be the right child of node8
    node8 = TreeNode(1, None, node11)  # Left child of node5
    node9 = TreeNode(1)  # Right child of node5
    node5 = TreeNode(1, node8, node9)  # Right child of the root's left child
    node2 = TreeNode(1, None, node5)  # Left child of the root
    node3 = TreeNode(1)  # Right child of the root
    root = TreeNode(1, node2, node3)  # Root node
    # Create a Solution object and use it to perform DFS
    solution = Solution()
    print(solution.longestZigZag(root))