def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
            return 0

    left = 0
    right = 0
    max_length = 0
    last_seen = {}

    while right < len(s):
        current_char = s[right]
        
        if current_char not in last_seen or last_seen[current_char] < left:
            last_seen[current_char] = right
        else:
            left = last_seen[current_char] + 1
            last_seen[current_char] = right
        
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
        right += 1
    
    return max_length
s = "abcabcbb"

print(lengthOfLongestSubstring(s))
    