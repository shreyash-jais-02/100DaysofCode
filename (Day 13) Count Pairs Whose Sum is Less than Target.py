# Count Pairs Whose Sum is Less than Target

# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums, target):
        n = len(nums)
        count = 0
        nums.sort()
        
        left = 0
        right = n - 1
        
        while left < right:
            if nums[left] + nums[right] < target:
                # All pairs with left index in [left, right] also satisfy the condition
                count += right - left
                left += 1
            else:
                # If the sum is greater or equal to the target, decrease the right index
                right -= 1
        
        return count
