"""
LeetCode 19: Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        Remove the nth node from the end of the list.

        Args:
            head: ListNode - head of the linked list
            n: int - position from end to remove

        Returns:
            ListNode - head of the modified list

        Time Complexity: O(L) where L is length of list
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.removeNthFromEnd(head, 2)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    head = ListNode(1)
    result = solution.removeNthFromEnd(head, 1)
    print(f"Test 2: {result}")
