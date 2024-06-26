from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water_count = 0
        max_left = [0] * n
        max_right = [0] * n
        
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        
        for i in range(n):
            water_count += min(max_left[i], max_right[i]) - height[i]
        return water_count

s = Solution()
height = [4,2,0,3,2,5]

print(s.trap(height))