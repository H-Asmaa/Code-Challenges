## TASK 0 : Remove Duplicates from Sorted Array

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
Return `k`.

> The judge will test your solution with the following code:

```python
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

**EXAMPLE 1**

**Input**: nums = `[1,1,2]`

**Output**: 2, nums = `[1,2,_]`

**Explanation**: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**EXAMPLE 2**

**Input**: nums = `[0,0,1,1,1,2,2,3,3,4]`

**Output**: 5, nums = `[0,1,2,3,4,_,_,_,_,_]`

**Explanation**: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**CONSTRAINTS**:

- `1 <= nums.length <= 3 \* 104`
- `-100 <= nums[i] <= 100`
- `nums is sorted in non-decreasing order.`




## TASK 1 : Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.



**EXAMPLE 1**

**Input**: nums = [1,2,3,4]

**Output**: [1,3,6,10]

Explanation:

    Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

**EXAMPLE 2**

**Input**: nums = [1,1,1,1,1]

**Output**: [1,2,3,4,5]

Explanation:

    Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

**EXAMPLE 3**

**Input**: nums = [3,1,2,10,1]

**Output**: [3,4,6,16,17]


**CONSTRAINTS**:

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`




## TASK 2 : Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.




**EXAMPLE 2**

**Input**: accounts = [[1,2,3],[3,2,1]]

**Output**: 6

Explanation:

    1st customer has wealth = 1 + 2 + 3 = 6

    2nd customer has wealth = 3 + 2 + 1 = 6

    Both customers are considered the richest with a wealth of 6 each, so return 6.

**EXAMPLE 2**

**Input**: accounts = [[1,5],[7,3],[3,5]]

**Output**: 10

Explanation:

    1st customer has wealth = 6

    2nd customer has wealth = 10

    3rd customer has wealth = 8

    The 2nd customer is the richest with a wealth of 10.

**EXAMPLE 2**

**Input**: accounts = [[2,8,7],[7,1,3],[1,9,5]]

**Output**: 17



**CONSTRAINTS**:

- `m == accounts.length`
- `n == accounts[i].length`
- `1 <= m, n <= 50`
- `1 <= accounts[i][j] <= 100`

**GREAT SOLUTION**:
```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
    highest = 0
    for x in accounts:
        highest = max(sum(x),highest)
    return highest
```
