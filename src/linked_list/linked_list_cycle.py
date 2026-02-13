"""
LeetCode 141: Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true

Example 2:
Input: head = [1,2], pos = 0
Output: true

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        """
        Detect if a linked list has a cycle.

        Args:
            head: ListNode - head of the linked list

        Returns:
            bool - true if cycle exists

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1 (with cycle)
    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle
    result = solution.hasCycle(head)
    print(f"Test 1: {result}")

    # Test case 2 (no cycle)
    head = ListNode(1, ListNode(2))
    result = solution.hasCycle(head)
    print(f"Test 2: {result}")
