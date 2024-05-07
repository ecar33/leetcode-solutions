class Solution:
    
    # Original O(n^2) slow solution which iterates over every substring and checks for a set bit
    
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0 # Initialize wonderful substring count
        
        for left in range(len(word)):
            bit_vector = 0
            for right in range(left, len(word)):
                # Update bit vector by toggling bit corresponding to char
                bit_index = ord(word[right]) - ord('a')
                bit_vector ^= (1 << bit_index) 
                
                # Check if current substring is wonderful               
                if ((bit_vector == 0) or (bit_vector & (bit_vector - 1)) == 0):
                    count += 1
                    print(f'Wonderful substring: {word[left:right+1]}')
                
        return count
        
        
       

        



def main():
    solution = Solution()
    str = 'aabb'
    solution.wonderfulSubstrings(str)
    
    
    
if __name__ == '__main__':
    main()