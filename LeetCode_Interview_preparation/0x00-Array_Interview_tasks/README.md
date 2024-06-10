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

Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

**EXAMPLE 2**

**Input**: nums = [1,1,1,1,1]

**Output**: [1,2,3,4,5]

Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

**EXAMPLE 3**

**Input**: nums = [3,1,2,10,1]

**Output**: [3,4,6,16,17]


**CONSTRAINTS**:

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`
