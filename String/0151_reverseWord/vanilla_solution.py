class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Normalize spaces and remove leading/trailing spaces
        words = []
        current_word = []
        in_word = False

        for char in s:
            if char == ' ':
                if in_word:
                    words.append(''.join(current_word))
                    current_word = []
                    in_word = False
            else:
                current_word.append(char)
                in_word = True

        # Append the last word if there is one
        if current_word:
            words.append(''.join(current_word))
        
        # Step 2: Reverse words and join them with a single space
        return ' '.join(reversed(words))

# Example usage:
sol = Solution()
input_str = "  hello world!  "
print(sol.reverseWords(input_str))  # Output: "world! hello"
