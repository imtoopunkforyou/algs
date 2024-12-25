"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


def add_two_numbers(
    l1: list[int] | None,
    l2: list[int] | None,
) -> list[int] | None:
    if not (l1 and l2):
        return None
    sum_of_l1 = 0
    for idx in range(len(l1)):
        if idx == 0:
            sum_of_l1 += l1[idx]
            continue
        sum_of_l1 += l1[idx] * (10 ** idx)

    sum_of_l2 = 0
    for idx in range(len(l2)):
        if idx == 0:
            sum_of_l2 += l2[idx]
            continue
        sum_of_l2 += l2[idx] * (10 ** idx)

    sum_of_both = sum_of_l1 + sum_of_l2
    result = []
    for i in range(len(str(sum_of_both))):
        num = sum_of_both % 10
        sum_of_both = sum_of_both // 10
        result.append(num)

    return result


if __name__ == '__main__':
    assert add_two_numbers([2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert add_two_numbers([0], [0]) == [0]
    assert add_two_numbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]
