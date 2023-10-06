# Final Value of Variable After Performing Operations

# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Set value of X as 0
        X = 0
        for operation in operations:
            if "++" in operation:
                X += 1
            else:
                X -= 1
        return X
        