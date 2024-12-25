"""
https://leetcode.com/problems/palindrome-number/

Palindrome Number.

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
             Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""


def is_palindrome(x: int) -> bool:
    def _get_number_len(number, number_len=0):
        new_number = number // 10
        if new_number:
            number_len += 1
            return _get_number_len(new_number, number_len)
        return number_len + 1

    if x < 0:
        return False
    elif 0 < x < 10:
        return True

    x_len = _get_number_len(x)
    digits_and_zeros = []
    y = x
    for i in range(x_len, 0, -1):
        a = (y % 10, 10 ** (i - 1))
        y = y // 10
        digits_and_zeros.append(a)

    numbers_for_sum = [x*y for x, y in digits_and_zeros]

    palindrome = sum(numbers_for_sum)

    return palindrome == x


if __name__ == '__main__':
    assert is_palindrome(121)
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False
