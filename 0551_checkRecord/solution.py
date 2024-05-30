class Solution:
    def checkRecord(self, s: str) -> bool:
        
        def recurse_string(n, total_absences, consecutive_lates):
            if total_absences >= 2 or consecutive_lates >= 3: return False
            if n == -1: return True
            
            current = s[n]
            if current == "P":
                return recurse_string(n-1, total_absences, 0)
            elif current == "A":
                return recurse_string(n-1, total_absences + 1, 0)
            elif current == "L":
                return recurse_string(n-1, total_absences, consecutive_lates + 1)
        
        return recurse_string(len(s) - 1, 0, 0)
            
                
s = "AA"
sol = Solution()

print(sol.checkRecord(s))