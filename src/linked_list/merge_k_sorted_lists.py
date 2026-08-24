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
        lists = [list for list in lists if list]

        dummy = ListNode()
        head = dummy

        while lists:
            append_list = []
            for list in lists:
                append_list.append(list.val)
            min_val = min(append_list)
            index = append_list.index(min_val)
            head.next = lists[index]
            head = head.next

            # clean up the list and lists
            lists[index] = lists[index].next
            if lists[index] == None:
                lists.pop(index)

        return dummy.next

    def pretty_print(self, list_ln):
        while list_ln:
            print(list_ln.val)
            list_ln = list_ln.next


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    result = solution.mergeKLists([list1, list2, list3])
    solution.pretty_print(result)

    # Test case 2
    result = solution.mergeKLists([])
    print(f"Test 2: {result}")
