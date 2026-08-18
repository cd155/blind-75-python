"""
LeetCode 206: Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Constraints:
- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        """
        Reverse a singly linked list.

        Args:
            head: ListNode - head of the linked list

        Returns:
            ListNode - head of the reversed list

        Time Complexity: O(n)
        Space Complexity: O(1) iterative, O(n) recursive
        """
        current_ln = head
        result_head = None
        while current_ln != None:
            result_head = ListNode(current_ln.val, result_head)
            current_ln = current_ln.next
        return result_head

    def reverse_list_in_place(self, head):
        current_ln = head
        result_head = None

        while current_ln != None:
            # swap current node and next
            next_ln = current_ln.next

            current_ln.next = result_head
            result_head = current_ln

            current_ln = next_ln
        return result_head


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseList(head)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    head = ListNode(1, ListNode(2))
    result = solution.reverseList(head)
    print(f"Test 2: {result.val if result else None}")
