"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


def str_in_str(haystack: str, needle: str) -> int:
    as_none = -1

    first_simbol = needle[0]
    for simbol_idx in range(len(haystack)):
        if haystack[simbol_idx] == first_simbol:
            current = haystack[simbol_idx:simbol_idx+len(needle):1]
            if current == needle:
                return simbol_idx
            else:
                simbol_idx += len(needle)

    return as_none


if __name__ == '__main__':
    assert 0 == str_in_str(haystack='sadbutsad', needle='sad')
    assert -1 == str_in_str(haystack='leetcode', needle='leeto')
