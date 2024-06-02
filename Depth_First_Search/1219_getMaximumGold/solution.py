def dfs(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y] or grid[x][y] == 0:
        return 0
    
    visited[x][y] = True
    current_value = grid[x][y]
    
    up = dfs(grid, x-1, y, visited)
    down = dfs(grid, x+1, y, visited)
    left = dfs(grid, x, y-1, visited)
    right = dfs(grid, x, y+1, visited)
    
    total = current_value + max(up, down, left, right)
    visited[x][y] = False
    
    return total
    
def getMaximumGold(grid):
    max_gold = 0
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                max_gold = max(max_gold, dfs(grid, i, j, visited))
    return max_gold


grid = [[0,6,0],[5,8,7],[0,9,0]]
print(getMaximumGold(grid))