"""
LeetCode 143: Reorder List

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        Reorder list in alternating first and last pattern.

        Args:
            head: ListNode - head of the linked list

        Returns:
            None - modifies the list in-place

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def reverse_list_in_place(head_ln):
            current_ln = head_ln
            result_head = None

            while current_ln != None:
                # swap current node and next
                next_ln = current_ln.next

                current_ln.next = result_head
                result_head = current_ln

                current_ln = next_ln
            return result_head
    
        head_ref = head

        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # break the list to two
        second_half = slow.next
        slow.next = None

        reversed_ln = reverse_list_in_place(second_half)

        while reversed_ln:
            head_next = head.next
            reversed_ln_next = reversed_ln.next

            head.next = reversed_ln
            reversed_ln.next = head_next

            head = head_next
            reversed_ln = reversed_ln_next
        
        return head_ref

    def pretty_print(self, list_ln):
        while list_ln:
            print(list_ln.val)
            list_ln = list_ln.next


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    ln = solution.reorderList(head)
    solution.pretty_print(ln)

    # Test case 2
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ln = solution.reorderList(head)
    solution.pretty_print(ln)
