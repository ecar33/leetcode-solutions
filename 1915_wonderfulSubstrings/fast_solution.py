from collections import defaultdict

class Solution:    
    # Fast O(n) solution
    
    def wonderfulSubstrings(self, word: str) -> int:
        
        # Map to store count of each bitmask encountered
        prefix_count = defaultdict(int)
        
        # Start with empty prefix having a bitmask of 1
        prefix_count[0] = 1
        
        current_bitmask = 0
        wonderful_count = 0
        
        for char in word:
            # Position of current character relative to 'a'
            bit_index = ord(char) - ord('a')
            
            # Update running bitmask
            current_bitmask ^= 1 << bit_index
            
            # Check if this bitmask has been seen before
            wonderful_count += prefix_count[current_bitmask]
            
            # Check for bitmasks that differ by exactly one bit
            for i in range(10):
                toggle_one_bit = current_bitmask ^ (1 << i)
                wonderful_count += prefix_count[toggle_one_bit]

            prefix_count[current_bitmask] += 1
        
        return wonderful_count
            
        
       

        



def main():
    solution = Solution()
    str = 'ab'
    print(solution.wonderfulSubstrings(str))
    
    
    
if __name__ == '__main__':
    main()