"""
https://leetcode.com/problems/find-greatest-common-divisor-of-array/

Given an integer array nums,
return the greatest common divisor of the smallest number
and largest number in nums.
The greatest common divisor of
two numbers is the largest positive integer
that evenly divides both numbers.

Example 1:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

Example 2:
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

Example 3:
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

Constraints:
2 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""


def find_GCD(nums: list[int]) -> int:
    nums.sort()
    b, a = nums[0], nums[-1]

    if a == 0 or b == 0:
        return a + b

    while True:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r


def find_GCD_brute_force(nums: list[int]) -> int:
    gcd = 1
    nums.sort()
    a, b = nums[0], nums[-1]

    for i in range(2, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            if i > gcd:
                gcd = i

    return gcd


if __name__ == '__main__':
    assert 2 == find_GCD([2, 5, 6, 9, 10])
    assert 1 == find_GCD([7, 5, 6, 8, 3])
    assert 3 == find_GCD([3, 3])

    assert 2 == find_GCD_brute_force([2, 5, 6, 9, 10])
    assert 1 == find_GCD_brute_force([7, 5, 6, 8, 3])
    assert 3 == find_GCD_brute_force([3, 3])
