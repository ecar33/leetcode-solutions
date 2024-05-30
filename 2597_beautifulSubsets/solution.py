from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums, k) -> int:
        def backtrack(start):
            nonlocal total_count
            
            if start > 0:
                total_count += 1
            
            for i in range(start, len(nums)):
                if cnt[nums[i] + k] > 0 or cnt[nums[i] - k] > 0:
                    continue
                
                cnt[nums[i]] += 1
                backtrack(i + 1)
                cnt[nums[i]] -= 1                    
        
        
        nums.sort()
        cnt = defaultdict(int)
        total_count = 0
        backtrack(0)
        return total_count

nums = [2, 4, 6]
k = 2
s = Solution()
print(s.beautifulSubsets(nums, k))