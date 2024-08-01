"""
https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time
complexity and with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:
1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


def qsort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[len(nums) // 2]
        less = [i for i in nums if i < pivot]
        greather = [i for i in nums if i > pivot]
        eq = [i for i in nums if i == pivot]

        return qsort(less) + [pivot] + eq[1:] + qsort(greather)


if __name__ == '__main__':
    assert [1, 2, 3, 5] == qsort([5, 2, 3, 1])
    assert [0, 0, 1, 1, 2, 5] == qsort([5, 1, 1, 2, 0, 0])
