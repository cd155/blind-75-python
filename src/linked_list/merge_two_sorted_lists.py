"""
LeetCode 21: Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the
nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted linked lists.

        Args:
            list1: ListNode - head of first list
            list2: ListNode - head of second list

        Returns:
            ListNode - head of merged list

        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = solution.mergeTwoLists(list1, list2)
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    result = solution.mergeTwoLists(None, None)
    print(f"Test 2: {result}")
