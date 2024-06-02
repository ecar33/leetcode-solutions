class Solution:
    def scoreOfString(self, s: str) -> int:
        s = s.lower()
        n = len(s)
        score = 0
        
        for i in range(1, n):
            score += abs(ord(s[i-1]) - ord(s[i]))
        return score
            
            

sol = Solution()
s = "zaz"
print(sol.scoreOfString(s))
