# import sys
from string_profiler import profile_function, plot_runtimes
import matplotlib.pyplot as plt

def has_repeats(s):
    """ Check if the given substring has repeating characters. """
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

def lengthOfLongestSubstringNaive(s):
    """ Find the longest substring without repeating characters using a naive O(n^3) approach. """
    n = len(s)
    longest = 0

    for start in range(n):
        for end in range(start + 1, n + 1):
            substr = s[start:end]
            if not has_repeats(substr):
                longest = max(longest, len(substr))

    return longest


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_string = sys.argv[1]
        print("Length of the longest substring without repeating characters:", lengthOfLongestSubstringNaive(input_string))
    else:
        print("Please provide a string as an argument.")
    
    # To profile
    # results = profile_function(lengthOfLongestSubstringNaive, 100)    
    # plot_runtimes(results, fitDegree=1, title='Runtime of naive_solution')
    # plt.show()  
    
    