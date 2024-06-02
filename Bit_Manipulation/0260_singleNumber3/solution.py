from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        else:
            cum_xor = 0
            for num in nums:
                cum_xor ^= num
            
            first_set_bit = cum_xor & -cum_xor
            
            group_1 = 0
            group_2 = 0
            
            for num in nums:
                if first_set_bit & num:
                    group_1 ^= num
                else:
                    group_2 ^= num
            
            return group_1, group_2

s = Solution()
nums = [1,2,1,3,2,5]

print(s.singleNumber(nums))