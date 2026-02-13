"""
Tests for LeetCode 271: Encode and Decode Strings
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

# Import using importlib to avoid conflicts with built-in modules
import importlib.util
spec = importlib.util.spec_from_file_location("encode_and_decode_strings", src_path / "string" / "encode_and_decode_strings.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
Codec = module.Codec


class TestEncodeAndDecodeStrings:
    """Test cases for Encode and Decode Strings problem"""

    def test_example_1(self):
        """Test case from example 1"""
        codec = Codec()
        strs = ["Hello", "World"]
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        assert decoded == strs

    def test_example_2(self):
        """Test case from example 2"""
        codec = Codec()
        strs = [""]
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        assert decoded == strs
