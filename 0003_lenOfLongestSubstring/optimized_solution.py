import sys
from string_profiler import profile_function, plot_runtimes
import matplotlib.pyplot as plt

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0  # Return 0 if the string is empty, as there's no substring.

    """ Initialize window pointers and support variables. """
    left = 0  
    right = 0  
    max_length = 0  
    last_seen = {}  

    """ Iterate over the string using the right pointer. """
    while right < len(s):
        current_char = s[right]  

        """ Check if the character is already seen and is within the current window. """
        if current_char in last_seen and last_seen[current_char] >= left:
            left = last_seen[current_char] + 1  
        
        """ Update the last seen index of the current character """
        last_seen[current_char] = right

        """ Calculate the current length of the window and update max_length if necessary. """
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
        
        """ Move the right pointer to the next character. """
        right += 1
    
    return max_length 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        print("Length of the longest substring without repeating characters:", lengthOfLongestSubstring(input_string))
    else:
        print("Please provide a string as an argument.")
    

    # To profile
    # results = profile_function(lengthOfLongestSubstring, 1000)    
    # plot_runtimes(results, fitDegree=1, title='Runtime of optimized_solution')
    # plt.show()  