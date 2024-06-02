class Solution:
    def partition(self, s: str):
        results = []
        n = len(s)
        
        def isPalindrome(sub):
            return sub == sub[::-1]
       
        def partitionHelper(start, curr):
            if start == n:
                results.append(curr.copy())
                return
            
            for i in range(start, n):
                sub = s[start:i+1]
                
                if isPalindrome(sub):
                    curr.append(sub)
                    partitionHelper(i+1, curr)
                    curr.pop()
        
        partitionHelper(0, [])
        return results

solution = Solution()
s = "aab"

print(solution.partition(s))