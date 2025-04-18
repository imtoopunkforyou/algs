"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


class TreeNode:
    def __init__(self, val: int = 0, left: int = None, right: int = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0

    return max(
        max_depth(root.left),
        max_depth(root.right),
    ) + 1


if __name__ == '__main__':
    ...
