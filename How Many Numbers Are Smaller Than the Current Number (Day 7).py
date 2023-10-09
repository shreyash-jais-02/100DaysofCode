#How Many Numbers Are Smaller Than the Current Number

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # Initialize a list to store the count of smaller numbers for each element
        counts = []
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            count = 0  # Initialize count for the current element
            
            # Compare the current element with all other elements in nums
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    count += 1  # Increment count if nums[j] is smaller than nums[i]
            
            counts.append(count)  # Append the count to the counts list
        
        return counts