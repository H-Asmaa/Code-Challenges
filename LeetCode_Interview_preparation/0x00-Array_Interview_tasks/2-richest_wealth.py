from typing import List

"""
A LeetCode task to learn how to get the highest sum of arrays
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """A method that returns the wealth that the richest customer has."""
        sum_array = []
        tmp_sum = 0
        for i in accounts:
            for j in i:
                tmp_sum += j
            sum_array.append(tmp_sum)
            tmp_sum = 0
        sum_array.sort()
        return sum_array[-1]

accounts = [[1,2,3],[3,2,1]]
Highest = Solution().maximumWealth(accounts)
print(Highest)
