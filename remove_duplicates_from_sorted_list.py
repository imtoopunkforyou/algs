"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __hash__(self):
        basis = self.val

        return hash(basis)

    def __eq__(self, other):
        return self.val == other.val


def delete_duplicates(head: ListNode | None) -> ListNode | None:
    if head is None:
        return head

    current = head
    while current.next:
        if current.val != current.next.val:
            current = current.next
        else:
            current.next = current.next.next

    return head


if __name__ == '__main__':
    assert delete_duplicates(ListNode(1, ListNode(1, ListNode(2, None)))) == ListNode(1, ListNode(2, None))