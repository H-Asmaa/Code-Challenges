from typing import List

"""
A LeetCode task to learn how to remove duplicates in an array.
"""


class Solution:
    def runningSum(self, nums: List[int]) -> int:
        """A method that returns an array of the running sums."""
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

nums = [1, 6, 2, 5, 2, 3]
running_sum = Solution().runningSum(nums)
print(running_sum)
