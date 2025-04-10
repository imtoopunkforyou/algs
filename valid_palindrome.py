"""
https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""


def is_palindrome(s: str) -> bool:
    def _prepare_default_str(default) -> str:
        result = ''
        for symbol in default:
            if symbol.isalpha() or symbol.isdigit():
                result += symbol.lower()
        return result
    default_str = _prepare_default_str(s)

    return default_str == default_str[::-1]


if __name__ == '__main__':
    assert is_palindrome('A man, a plan, a canal: Panama')
    assert is_palindrome('race a car') is False
    assert is_palindrome(' ')
    assert is_palindrome('0P') is False
