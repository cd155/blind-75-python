"""
LeetCode 207: Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false

Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        Determine if all courses can be finished given prerequisites.

        Args:
            numCourses: int - number of courses
            prerequisites: List[List[int]] - prerequisite pairs

        Returns:
            bool - true if all courses can be finished

        Time Complexity: O(V + E) where V is courses and E is prerequisites
        Space Complexity: O(V + E)
        """
        # TODO: Implement solution
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.canFinish(2, [[1, 0]])
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.canFinish(2, [[1, 0], [0, 1]])
    print(f"Test 2: {result}")
