def largestLocal(grid):
        n = len(grid)
        filtered_matrix = [[0] * (n - 2) for _ in range(n - 2)]
        
        for i in range(n - 2): 
            for j in range(n - 2):
                submatrix = [row[j:j+3] for row in grid[i:i+3]]
                filtered_matrix[i][j] = max(max(row) for row in submatrix)
        
        return filtered_matrix
    
    
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(largestLocal(grid))