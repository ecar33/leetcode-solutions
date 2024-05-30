from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        strs = sorted(strs, key=len)
        shortest_str = strs[0]
        n = len(shortest_str)
        for i in range(n): 
            if all(shortest_str[i] == str[i] for str in strs):
                longest_prefix += shortest_str[i] 
            else:
                return longest_prefix   
        return longest_prefix
            
s = Solution()
strs = ["cir", "car"]
print(s.longestCommonPrefix(strs))