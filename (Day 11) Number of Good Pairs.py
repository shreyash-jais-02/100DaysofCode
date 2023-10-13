# Number of Good Pairs

# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums):
        count = Counter(nums)
        good_pairs = 0

        for key, value in count.items():
            if value > 1:
                good_pairs += (value * (value - 1)) // 2

        return good_pairs