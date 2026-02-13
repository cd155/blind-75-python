"""
LeetCode 23: Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Example 2:
Input: lists = []
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists.

        Args:
            lists: List[ListNode] - array of sorted linked lists

        Returns:
            ListNode - head of merged list

        Time Complexity: O(N log k) where N is total nodes
        Space Complexity: O(k) for heap
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    result = solution.mergeKLists([list1, list2, list3])
    print(f"Test 1: {result.val if result else None}")

    # Test case 2
    result = solution.mergeKLists([])
    print(f"Test 2: {result}")
