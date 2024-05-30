import numpy as np

def matrixScore(grid):
    grid = np.array(grid)
    
    m, n = grid.shape
    
    # Flip rows if the first element is 0
    for i in range(m):
        if grid[i][0] == 0:
            grid[i] = 1 - grid[i]  # Flips all elements in the row
    
    grid = grid.T
    
    # Flip columns if there are more 0s than 1s
    for j in range(n):
        if np.sum(grid[j]) < m / 2:
            grid[j] = 1 - grid[j]  # Flips all elements in the column
    
                
    # Transpose back to original layout and calculate the score
    grid = grid.T
    # Convert binary rows to decimal numbers and sum up for the score
    return np.sum([int("".join(map(str, row)), 2) for row in grid])
            
    
    


grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(matrixScore(grid))