"""
LeetCode 295: Find Median from Data Stream

The median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far.

Example 1:
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
       [[], [1], [2], [], [3], []]
Output: [null, null, null, 1.5, null, 2.0]

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
"""


class MedianFinder:
    def __init__(self):
        """
        Initialize the MedianFinder data structure.

        Time Complexity: O(1)
        Space Complexity: O(n) where n is the number of elements added
        """
        # TODO: Implement initialization
        pass

    def addNum(self, num):
        """
        Add a number to the data structure.

        Args:
            num: int - number to add

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # TODO: Implement addNum
        pass

    def findMedian(self):
        """
        Find the median of all elements.

        Returns:
            float - median value

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # TODO: Implement findMedian
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(f"Median: {medianFinder.findMedian()}")  # 1.5
    medianFinder.addNum(3)
    print(f"Median: {medianFinder.findMedian()}")  # 2.0
