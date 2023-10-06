# Kids with the greatest number of candies

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Max no of candies with kids
        max_candies = max(candies)
        # create empty result list
        result = []
        # Iterate through kids candies
        for kid_candies in candies:
            # Check the sum after giving extra candies
            if extraCandies + kid_candies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result