# Shuffle String

# https://leetcode.com/problems/shuffle-string/ 

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Create a list of the same length as s to store the shuffled characters
        shuffled = [None] * len(s)

        # Iterate through the characters in s and their corresponding indices
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]

        # Join the characters in the shuffled list to form the shuffled string
        shuffled_string = "".join(shuffled)

        return shuffled_string