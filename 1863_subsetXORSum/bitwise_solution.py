class Solution:
    def subsetXORSum(self, nums) -> int:
        n = len(nums)
        total_xor = 0
        for i in range(1 << n):
            subset_xor = 0
            for j in range(n):
                if i & (1 << j):
                    subset_xor ^= nums[j]
            total_xor += subset_xor
        return total_xor
    
s = Solution()
nums = [3,4,5,6,7,8]
print(s.subsetXORSum(nums))