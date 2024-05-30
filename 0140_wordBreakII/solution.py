from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        n = len(s)
        def backtrack(start):
            if start == n:
                return [[]]
            elif start in memo:
                return memo[start]

            memo[start] = []
            for end in range(start+1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    for sublist in backtrack(end):
                        memo[start].append([word] + sublist)
            
            return memo[start]

    
        results = [' '.join(words) for words in backtrack(0)]
        return results


sol = Solution()
s = "catsanddog" 
wordDict = ["cat","cats","and","sand","dog"]

print(sol.wordBreak(s, wordDict))