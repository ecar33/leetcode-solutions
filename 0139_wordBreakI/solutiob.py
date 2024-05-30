from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        n = len(s)
    
        def backtrack(start):
            if start == n:
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, n + 1):
                if s[start:end] in wordDict and backtrack(end):
                    memo[start] = True
                    return True
                
            memo[start] = False
            return False

        return backtrack(0)
        
        
        




s = "leetcode" 
wordDict = ["leet","code"]
solution = Solution()

print(solution.wordBreak(s, wordDict))
        
        