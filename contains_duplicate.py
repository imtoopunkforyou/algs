"""
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


def contains_duplicate(nums: list[int]) -> bool:
    for idx in range(0, len(nums) - 1):
        for idx_next in range(idx + 1, len(nums)):
            if nums[idx] == nums[idx_next]:
                return True

    return False


def contains_duplicate_use_set(nums: list[int]) -> bool:
    if len(set(nums)) < len(nums):
        return True

    return False


if __name__ == '__main__':
    assert True is contains_duplicate([1, 2, 3, 1])
    assert False is contains_duplicate([1, 2, 3, 4])
    assert True is contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

    assert True is contains_duplicate_use_set([1, 2, 3, 1])
    assert False is contains_duplicate_use_set([1, 2, 3, 4])
    assert True is contains_duplicate_use_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
