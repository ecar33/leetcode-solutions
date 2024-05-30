def largestLocal(grid):
    n = len(grid)
    maxLocal = [[0] * (n - 2) for _ in range(n-2)]
    
    for i in range(n-2):
        for j in range(n-2):
            max_val = 0
            # 3x3 matrix centered at (i+1, j+1)
            for x in range(3):
                for y in range(3):
                    max_val = max(max_val, grid[i + x][j + y])
                    
            maxLocal[i][j] = max_val
    return maxLocal


grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(largestLocal(grid))