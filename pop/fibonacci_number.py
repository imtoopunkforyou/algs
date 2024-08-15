"""
https://leetcode.com/problems/two-sum/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the two preceding ones, starting from 0 and 1.
That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:
0 <= n <= 30
"""


def fib_recursion(n: int):
    if n < 2:
        return n
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


def fib_sequentially(n: int):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a % 10


if __name__ == '__main__':
    assert 3 == fib_recursion(4)
    assert 2 == fib_recursion(3)
    assert 1 == fib_recursion(1)
    assert 0 == fib_recursion(0)

    assert 3 == fib_sequentially(4)
    assert 2 == fib_sequentially(3)
    assert 1 == fib_sequentially(1)
    assert 0 == fib_sequentially(0)
