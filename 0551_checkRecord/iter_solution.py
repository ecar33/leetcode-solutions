class Solution:
    def checkRecord(self, s: str) -> bool:
        total_absences = 0
        consecutive_lates = 0
        
        for char in s:
            if char == 'A':
                total_absences += 1
                consecutive_lates = 0  # Reset consecutive lates
            elif char == 'L':
                consecutive_lates += 1
            else:  # char == 'P'
                consecutive_lates = 0  # Reset consecutive lates
            
            if total_absences >= 2 or consecutive_lates >= 3:
                return False

        return True

            
                
s = "AA"
sol = Solution()

print(sol.checkRecord(s))