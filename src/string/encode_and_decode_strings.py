"""
LeetCode 271: Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent
over the network and is decoded back to the original list of strings.

Implement the encode and decode methods.

Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]

Example 2:
Input: dummy_input = [""]
Output: [""]

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ASCII characters.
"""


class Codec:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.

        Args:
            strs: List[str] - list of strings

        Returns:
            str - encoded string

        Time Complexity: O(n) where n is total characters
        Space Complexity: O(n)
        """
        # TODO: Implement encode
        pass

    def decode(self, s):
        """
        Decodes a single string to a list of strings.

        Args:
            s: str - encoded string

        Returns:
            List[str] - decoded list of strings

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        # TODO: Implement decode
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    codec = Codec()

    # Test case 1
    strs = ["Hello", "World"]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print(f"Test 1: {decoded}")

    # Test case 2
    strs = [""]
    encoded = codec.encode(strs)
    decoded = codec.decode(encoded)
    print(f"Test 2: {decoded}")
