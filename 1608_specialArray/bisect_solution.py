from typing import List
from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(n+1):
            idx = bisect_left(nums, x)
            if n - idx == x:
                return x
        # If we reach here, then the element was not present
        return -1

s = Solution()
nums = [3, 5]

print(s.specialArray(nums))


