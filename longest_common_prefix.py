"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ''.

Example 1:
Input: strs = ['flower','flow','flight']
Output: 'fl'

Example 2:
Input: strs = ['dog','racecar','car']
Output: ''
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longest_common_prefix(strs: list[str]) -> str:
    result_prefix = ''
    first_word = strs[0]
    smallest_len = len(first_word)

    for idx in range(0, len(first_word), 1):
        current_prefix = result_prefix + first_word[idx]
        for word in strs:
            if smallest_len > len(word):
                smallest_len = len(word)
            if word.startswith(current_prefix):
                result = True
            else:
                result = False
                return result_prefix[:smallest_len]
        if result:
            result_prefix = current_prefix

    return result_prefix[:smallest_len]

if __name__ == '__main__':
    assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'
    assert longest_common_prefix(['dog', 'racecar', 'car']) == ''
    assert longest_common_prefix(['reflower', 'flow', 'flight']) == ''
    assert longest_common_prefix(['aaa', 'aa', 'aaa']) == 'aa'
    assert longest_common_prefix(['aa', 'aaa', 'aaa']) == 'aa'
    assert longest_common_prefix(['c', 'acc', 'ccc']) == ''
