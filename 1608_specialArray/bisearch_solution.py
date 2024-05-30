from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n+1):
            low = 0
            high = n
        
            while low < high:
                mid = (high + low) // 2
                if nums[mid] >= x:
                    high = mid
                else:
                    low = mid + 1
            if n - low == x:
                return x
        # If we reach here, then the element was not present
        return -1

s = Solution()
nums = [3, 5]

print(s.specialArray(nums))


