# Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we will have to create a dictionary of the elements in the array
        num_indices = {}
        #iterating through the list of numbers
        for index, num in enumerate(nums) :
            complement = target - num
            if complement in num_indices:
                return[num_indices[complement], index]
            num_indices[num] = index