class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n
        
        
        left_product = 1
        for i in range(n):
            result[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
            
        return result
        
s = Solution()
nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))
            
        