# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev = 0
        
        # Iterate through the string from right to left
        for c in s[::-1]:
            current = roman[c]
            
            # If the current numeral is smaller than the previous one, subtract it
            if current < prev:
                total -= current
            else:
                total += current
                
            prev = current
        
        return total
