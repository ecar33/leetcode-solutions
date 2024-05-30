class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
    
        def generate_subsets( nums: List[int], index: int, current_XOR: int) -> int:
            # Return current_XOR when all elements in nums are already considered
            if index == len(nums): return current_XOR
            
            # Calculate sum of subset xor with current element
            with_element = generate_subsets(nums, index + 1, current_XOR ^ nums[index])
            
            # Calculate sum of subset xor without current element
            without_element = generate_subsets(nums, index + 1, current_XOR)
            
            # Return sum of xor totals
            return with_element + without_element

        return generate_subsets(nums, 0, 0)