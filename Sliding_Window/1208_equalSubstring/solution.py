class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, current_cost, max_length = 0, 0, 0
        
        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            current_cost += cost
            
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
        
            max_length = max(max_length, right - left + 1)
        
        return max_length
    

sol = Solution()
s = "abcd" 
t = "bcdf"
max_cost = 3

print(sol.equalSubstring(s, t, max_cost))