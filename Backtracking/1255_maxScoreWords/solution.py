from typing import List
from string import ascii_lowercase
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def backtrack(index, current_score, available_letters):
            nonlocal max_score
            if index == len(sorted_words):
                max_score = max(max_score, current_score)
                return
            word, word_score = sorted_words[index]
            # Calculate the count of each letter in the current word
            word_count = Counter(word)
            # Check if the word can be formed with the available letters
            if all(available_letters[c] >= word_count[c] for c in word_count):
                # Create a new counter to update available letters
                new_available_letters = available_letters.copy()
                # Decrement the count of letters used in the current word
                for char in word:
                    new_available_letters[char] -= 1
                # Recurse with this word included in the score
                backtrack(index + 1, current_score + word_score, new_available_letters)
            # Recurse without including this word
            backtrack(index + 1, current_score, available_letters)

        def create_score_map():
            return {char: score[index] for index, char in enumerate(ascii_lowercase)}

        def compute_word_score(word):
            return sum(score_map[char] for char in word if char in score_map)

        # Create the score map from letters to their scores
        score_map = create_score_map()
        # Create a frequency count of available letters
        available_letters = Counter(letters)
        # Compute scores for each word
        word_scores = [(word, compute_word_score(word)) for word in words]
        # Sort words by their scores in descending order
        sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)
        # Initialize maximum score
        max_score = 0
        # Start backtracking from the initial state
        backtrack(0, 0, available_letters)
        return max_score

# Example usage
s = Solution()
words = ["xxxz", "ax", "bx", "cx"]
letters = ["z", "a", "b", "c", "x", "x", "x"]
score = [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]

print(s.maxScoreWords(words, letters, score))  # Expected output should reflect the maximum score
