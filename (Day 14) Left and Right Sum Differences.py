# Left and Right Sum Differences

# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        answer = [0] * n

        # Calculate the left_sum for each element
        left_sum[0] = 0
        for i in range(1, n):
            left_sum[i] = left_sum[i - 1] + nums[i - 1]

        # Calculate the right_sum for each element
        right_sum[n - 1] = 0
        for i in range(n - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i + 1]

        # Calculate the answer using left_sum and right_sum
        for i in range(n):
            answer[i] = abs(left_sum[i] - right_sum[i])

        return answer