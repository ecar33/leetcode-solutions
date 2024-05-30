import re

class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(' +', ' ', s.strip()) # Normalize spaces
        return " ".join(reversed(s.split(' '))) # Split, reverse, and join
    
    

s = Solution()
string = "a good   example"
print(s.reverseWords(string))