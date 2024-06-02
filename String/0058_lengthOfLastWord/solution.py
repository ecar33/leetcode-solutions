class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().rsplit()[-1])        


s = Solution()
string =  "   fly me   to   the moon  "
print(s.lengthOfLastWord(string))