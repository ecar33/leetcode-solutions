def longest_substring(s, k):
    # Base case: If the string is shorter than k, then no substring
    # can satisfy the condition
    if len(s) < k:
        return 0

    # Frequency count for all characters in the string
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find the first character that does not meet the frequency requirement
    for i in range(len(s)):
        if frequency[s[i]] < k:
            # Use this character to split the string into two parts
            # and make recursive calls for each part
            # Skip all occurrences of this character and find the longest substring in both parts
            next_part = i + 1
            while next_part < len(s) and frequency[s[next_part]] < k:
                next_part += 1
            # Recursive call on the left of the divider and on the right starting after any consecutive dividers
            return max(longest_substring(s[:i], k), longest_substring(s[next_part:], k))

    # If no dividers were found, the entire string meets the requirement
    return len(s)

# Example usage
input_string = "aaab"
k_value = 3
print(f"The length of the longest substring where each character appears at least {k_value} times is: {longest_substring(input_string, k_value)}")
