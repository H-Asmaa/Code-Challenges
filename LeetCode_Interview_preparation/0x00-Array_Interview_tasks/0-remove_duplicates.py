from typing import List

"""
A LeetCode task to learn how to remove duplicates in an array.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """A method that returns the number of unique
        elements in the array nums."""
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


nums = [1, 1, 2, 2, 2, 3]
k = Solution().removeDuplicates(nums)
print(k)
