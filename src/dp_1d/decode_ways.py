"""
LeetCode 91: Decode Ways

A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the
reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Given a string s containing only digits, return the number of ways to decode it.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3

Constraints:
- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s)
"""


class Solution:
    def numDecodings(self, s):
        """
        Count the number of ways to decode the string.

        Args:
            s: Encoded string of digits

        Returns:
            Number of ways to decode

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        size = len(s)
        num_to_count_array = [0]*size

        if int(s[0]) != 0:
            num_to_count_array[0] = 1

        for i in range(1, size):
            if int(s[i]) != 0:
                num_to_count_array[i] = num_to_count_array[i-1]

            if 10<=int(s[i-1:i+1])<=26:
                if i == 1:
                    num_to_count_array[i] += 1
                else:
                    num_to_count_array[i] += num_to_count_array[i-2]
        return num_to_count_array

    # decode anything with a hash table
    def decodings(self, s):
        decode_hash = {'1': 'a', '2': 'aa', '11': 'c', '22': 'cc'}
        max_length_value = max(len(k) for k in decode_hash.keys)
        size = len(s)
        num_to_count_array = [0]*size

        for i in range(0, size):
            for j in range(0, max_length_value):
                start = i - j
                if start >= 0:
                    sub_string = s[start: i+1]
                    if sub_string in decode_hash:
                        if start == 0:
                            num_to_count_array[i] += 1
                        else:
                            num_to_count_array[i] += num_to_count_array[start-1] 
        return num_to_count_array[-1]


# Example usage (for testing locally)
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result = solution.numDecodings("12")
    print(f"Test 1: {result}")

    # Test case 2
    result = solution.numDecodings("226")
    print(f"Test 2: {result}")

    # Test case 3
    result = solution.numDecodings("01")
    print(f"Test 3: {result}")

    # Test case 4
    result = solution.numDecodings("100")
    print(f"Test 4: {result}")

    # Test case 5
    result = solution.decodings("1122")
    print(f"Test 5: {result}")