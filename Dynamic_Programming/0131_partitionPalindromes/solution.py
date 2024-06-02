class Solution:
    def partition(self, s: str):
        results = []
        n = len(s)
        
        # Create a DP table to store palindromes in O(n * n) space
        dp = [[False] * n for _ in range(n)]
        
        # Diagonals (single characters) are palindromes
        for i in range(n):
            dp[i][i] = True
            
        # Fill the DP table for substrings containing palindromes where
        # dp[i][j] represents s[i:j+1] is a valid palindrome
        for length in range(2, n+1): # Current length of substring
            for i in range(n - length + 1):
                # j is the ending index for the particular starting position
                j = i + length - 1
                
                # Check characters directly if len == 2
                if length == 2:
                    dp[i][j] = (s[i] == s[j])
                # Check start and end characters as well as the characters between
                else: 
                    dp[i][j] = (s[i] == s[j]) and (dp[i+1][j-1])
       
        def partitionHelper(start, curr):
            if start == n:
                results.append(curr.copy())
                return
            
            for i in range(start, n):
                if dp[start][i]:
                    curr.append(s[start:i+1])
                    partitionHelper(i+1, curr)
                    curr.pop()
        
        partitionHelper(0, [])
        return results

solution = Solution()
s = "aab"

print(solution.partition(s))