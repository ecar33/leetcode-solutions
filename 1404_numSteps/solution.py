class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        count = 0
            
        while s != 1:
            if (s & 1):
                s += 1
            else:
                s >>= 1
            count += 1
        return count
        
        
        
           
        
sol = Solution()
s = "111110100"
print(sol.numSteps(s))