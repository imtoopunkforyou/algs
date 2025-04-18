"""
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


def plus_one(digits: list[int]) -> list[int]:
    last_digit = digits[-1]
    is_simple_way = False if last_digit == 9 else True
    if is_simple_way:
        last_digit = digits.pop()
        digits.append((last_digit+1))
    else:
        for idx in range(len(digits)-1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                break

    if digits[0] == 0:
        digits.insert(0, 1)

    return digits


if __name__ == '__main__':
    assert plus_one([1, 2, 3]) == [1, 2, 4]
    assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one([9, 8, 9]) == [9, 9, 0]
    assert plus_one([9]) == [1, 0]
