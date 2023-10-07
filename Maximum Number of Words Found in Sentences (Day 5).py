# Maximum Number of Words Found in Sentences

# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            words = sentence.split()  # Split the sentence into words
            word_count = len(words)   # Count the number of words in the sentence
            max_words = max(max_words, word_count)  # Update the maximum word count
        
        return max_words
