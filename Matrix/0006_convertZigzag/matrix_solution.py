class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        # Calculating more accurate column count
        cycle_len = 2 * numRows - 2
        full_cycles = len(s) // cycle_len
        remainder = len(s) % cycle_len

        # Each full cycle occupies fewer columns, typically one per row except the first and last row
        cols = full_cycles * (numRows - 1)
        if remainder > 0:
            # Each character in the remainder could potentially start a new column until numRows
            cols += min(numRows, remainder)

        # Create a matrix with empty strings
        matrix = [['' for _ in range(cols)] for _ in range(numRows)]
        row, col = 0, 0
        down = True
        
        for char in s:
            matrix[row][col] = char
            
            if down:
                if row == numRows - 1:
                    row -= 1
                    col += 1
                    down = False
                else: 
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
                    col += 1
        
        final_string = []
        
        for row in range(numRows):
            for col in range(cols):
                final_string.append(matrix[row][col])
        
        return ''.join(final_string)
            
    

sol = Solution()
numRows = 4
s = "ABCDE"
print(sol.convert(s, numRows))