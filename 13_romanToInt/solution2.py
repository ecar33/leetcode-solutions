def romanToInt(s: str) -> int:
    hmap = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }

    i = 0
    ans = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in hmap: # Use string slicing which is OOB safe
            ans += hmap[s[i:i+2]]
            i += 2  # Skip the next character as well
        elif s[i] in hmap:
            ans += hmap[s[i]]
            i += 1
        else:
            i += 1  # Safeguard to avoid infinite loop on unexpected character
    return ans


print(romanToInt('MCMXCIV'))
